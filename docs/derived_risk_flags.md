
# Derived Risk Flags – Guide + Code

Below are commonly used clinical cutoffs to derive binary flags and a composite lifestyle score.
These are **for demonstration/education** – please adjust to your project’s definitions and cite
guidelines where appropriate.

## New columns created

- `has_hypertension` – systolic ≥ 130 **OR** diastolic ≥ 80 (if your `Blood Pressure` splits into SBP/DBP columns, adjust).
- `has_diabetes` – `HbA1c >= 6.5` **OR** (if you have fasting glucose) `Glucose >= 126`.
- `has_dyslipidemia` – (`Cholesterol >= 240`) **OR** (`Triglycerides >= 200`) as a simple proxy.
- `lifestyle_risk_score` – points from: Smoking, Alcohol (heavy), Physical Activity (low), Sleep Hours (<6 or >10), Stress Level (high).

> Note: Replace column names below if your dataset uses different casing or names.

## Pseudo‑code / Python (Pandas)

```python
import pandas as pd

df = pd.read_csv("data/raw/heart_attack_china.csv", low_memory=False)

# --- Helper parsers (adjust these if your columns differ) ---
# Example: if Blood Pressure is a single string like "130/85", split it.
if "Blood Pressure" in df.columns and df["Blood Pressure"].dtype == object:
    bp_split = df["Blood Pressure"].str.extract(r'(?P<SBP>\d+)[^0-9]+(?P<DBP>\d+)').astype(float)
    df["SBP"] = bp_split["SBP"]
    df["DBP"] = bp_split["DBP"]

# --- Binary flags ---
df["has_hypertension"] = ((df.get("SBP", pd.Series([None]*len(df))).fillna(-1) >= 130) |
                          (df.get("DBP", pd.Series([None]*len(df))).fillna(-1) >= 80))

df["has_diabetes"] = ((df.get("HbA1c", 0) >= 6.5) |
                      (df.get("Glucose", 0) >= 126))

df["has_dyslipidemia"] = ((df.get("Cholesterol", 0) >= 240) |
                          (df.get("Triglycerides", 0) >= 200))

# --- Lifestyle risk score (0–5) ---
def yes_no_to_bool(s):
    if s.dtype == object:
        return s.str.strip().str.upper().map({"YES": True, "Y": True, "TRUE": True, "1": True}).fillna(False)
    return s.astype(bool).fillna(False)

smoking = yes_no_to_bool(df.get("Smoking", pd.Series([False]*len(df))))
# crude alcohol risk proxy: numeric drinks/week or categorical 'Heavy'
alcohol = df.get("Alcohol", 0)
if alcohol.dtype == object:
    alcohol_risk = alcohol.str.contains("heavy", case=False, na=False)
else:
    alcohol_risk = (alcohol >= 14)  # e.g., ≥14 drinks/week
activity = df.get("Physical Activity", pd.NA)
activity_low = None
if activity.dtype == object:
    activity_low = activity.str.contains("low|sedentary|none", case=False, na=False)
else:
    activity_low = (activity.fillna(0) < 150)  # minutes/week

sleep = df.get("Sleep Hours", pd.NA)
if sleep.dtype != object:
    sleep_risk = ((sleep < 6) | (sleep > 10)).fillna(False)
else:
    sleep_risk = sleep.str.contains(r"(<6|>10|short|long)", case=False, na=False)

stress = df.get("Stress Level", pd.NA)
if stress.dtype == object:
    stress_high = stress.str.contains("high|severe|very", case=False, na=False)
else:
    # assume a 1–10 scale if numeric
    stress_high = (stress.fillna(0) >= 7)

df["lifestyle_risk_score"] = (smoking.astype(int) + alcohol_risk.astype(int) +
                              activity_low.astype(int) + sleep_risk.astype(int) +
                              stress_high.astype(int))

# --- Optional: add synthetic record_date for demo trends (monthly buckets) ---
# For Phase-1 you can be transparent that this is synthetic.
import numpy as np
months = pd.date_range("2024-01-01", periods=12, freq="MS")
df["record_date"] = np.random.choice(months, size=len(df))

# Save processed data
df.to_csv("data/processed/heart_attack_china_enriched.csv", index=False)
```

## Notes
- If you have separate SBP/DBP columns already, remove the `split` step and rename in the code.
- If units differ (e.g., mmol/L), convert to mg/dL (or adjust thresholds).
- Be explicit in your report that flags are *constructed* for educational purposes.
```

