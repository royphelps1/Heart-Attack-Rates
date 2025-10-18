# Normalized Flags (Phase 1)

**Purpose**  
We are turning text columns in the raw data into clean flags and simple ordered numbers. We are not creating new medical facts. We are only making the data easier to analyze.

**Source file:** `data/raw/heart_attack_china.csv`  
**Output file:** `data/processed/heart_attack_china_enriched.csv`  

---

## Boolean flags we will add
These come directly from existing columns:

- **has_hypertension** → `Hypertension == "Yes"`
- **has_diabetes** → `Diabetes == "Yes"`
- **has_dyslipidemia** → `Cholesterol_Level == "High"` *(working rule for Phase 1)*
- **is_smoker** → `Smoking_Status == "Smoker"`
- **is_obese** → `Obesity == "Yes"`
- **tcm_use** → `TCM_Use == "Yes"`
- **is_rural** → `Rural_or_Urban == "Rural"`

---

## Ordinal columns we will encode
We will map text to simple ordered numbers (documented here and applied in the notebook):

- **Air_Pollution_Exposure:** Low = 0, Medium = 1, High = 2  
- **Physical_Activity:** Low = 0, Moderate = 1, High = 2  
- **Diet_Score:** Poor = 0, Moderate = 1, Healthy = 2  
- **Healthcare_Access:** Poor = 0, Moderate = 1, Good = 2  
- **Hospital_Availability:** Low = 0, Medium = 1, High = 2  
- **Income_Level:** Kept as categorical in Phase 1 for now

---

## Basic cleaning we will apply
- Cast to numeric: **Age**, **Blood_Pressure**, **CVD_Risk_Score** (coerce errors; review outliers).  
- Standardize text categories (trim spaces, consistent case).  
- Handle missing values:  
  - Categorical → `"Unknown"` (or mode; we will state which in the notebook)  
  - Numeric → median  
- Quick checks: class balance for **Heart_Attack**, value ranges (e.g., Blood_Pressure), and category counts.

---

## Note on `CVD_Risk_Score`
We will keep this column for EDA. If it mixes in outcome-related information, we will not use it in baseline models in Phase 2 to avoid leakage.

---

## Write-out
After normalization and checks, we write the result to:  
`data/processed/heart_attack_china_enriched.csv`

---

### Change log
- **2025-10-18**: Created `normalized_flags.md` to replace older “derived flags” wording.

---

### Where this is used
This document matches the notebook section **“5) Normalized Clinical & Lifestyle Flags (Phase 1)”** and serves as the reference for our team.

```

