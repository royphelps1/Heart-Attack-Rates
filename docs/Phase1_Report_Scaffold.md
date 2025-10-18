
# DSCI 511 – Term Project (Phase 1): Scoping a Dataset

> **Team:** Roy Phelps, Shad Scarboro, Leland Weeks, Evan Wessel  
> **Dataset:** `heart_attack_china.csv` (239,266 x 28)  
> **Repo:** (link to your GitHub repo)

## 1) Abstract (diverse audience)
A brief, non-technical summary (3–5 sentences): what topic, why it matters, and what this dataset
enables (e.g., risk factors associated with heart attacks across regions).

## 2) Team Background & Roles
- Member → skill focus → growth goals  
- Who will handle data acquisition, cleaning, enrichment, notebook infra, and README/data dictionary?

## 3) Topic & Intended Uses
- Research question(s) / example applications (EDA, association analysis, baseline prediction)  
- Why this dataset is suitable for Phase-1 (size, features, label, region fields)

## 4) Data Sample & Dictionary
Paste a small sample (10–20 rows) and link to our docs.

```python
import pandas as pd
pd.set_option("display.max_columns", None)
df = pd.read_csv("data/raw/heart_attack_china.csv", low_memory=False)
df.head(10)
```

- **Data dictionary:** see `docs/data_dictionary.md`
- **Normalized flags & encodings (what we add in Phase 1):** see `docs/normalized_flags.md`

## 5) Provenance & Access
- Source, license/terms, de-identification.  
- How others can obtain or access (file location in repo and any usage notes).

## 6) Limitations & Improvements
- **Missingness & cleanliness:** Some categorical fields (e.g., `Education_Level`) may contain missing values; we will standardize text categories (trim/case) and apply simple imputations (categorical → "Unknown"/mode; numeric → median).
- **Type casting:** Ensure `Age`, `Blood_Pressure`, and `CVD_Risk_Score` are numeric; review outliers.
- **Normalization (Phase 1):** Convert existing text fields into booleans/ordinals (e.g., `has_hypertension`, `has_diabetes`, `has_dyslipidemia`, `is_smoker`, `is_obese`, `tcm_use`, `is_rural`; plus ordinal encodings for pollution, activity, diet, access, hospital availability, income). Documented in `docs/normalized_flags.md`.
- **Leakage caution:** Keep `CVD_Risk_Score` for EDA but **exclude from baseline modeling** in Phase 2 unless proven safe.
- **(Optional, later) Time fields:** We may add a synthetic `record_date` **after** Phase 1 if needed for time-based visuals.

## 7) Enrichment Plan (Optional for Phase-1)
- Possible joins after Phase-1 write-out: public health indicators (population, PM2.5, hospital beds/1k, GDP per capita).
- Keys needed: province/city standardization for reliable joins.

## 8) Reproducibility
How to rebuild processed data from raw:

**Inputs**
- `data/raw/heart_attack_china.csv`

**Steps (Phase 1)**
1) **Normalize flags & ordinals** per `docs/normalized_flags.md`
2) **Type cast** `Age`, `Blood_Pressure`, `CVD_Risk_Score` to numeric (with coercion); review outliers
3) **Standardize categories** (trim/case)
4) **Handle missingness** (categorical → "Unknown"/mode; numeric → median)
5) **Sanity checks** (class balance for `Heart_Attack`, value ranges, category counts)
6) **Write out** → `data/processed/heart_attack_china_enriched.csv`

**Folder layout & commands**
- See `README.md` for project structure and “how to run” instructions.
- Documentation for the mappings lives in `docs/normalized_flags.md`.

## Appendix A: Figures/Tables to Include Later

## Appendix A: Figures/Tables to Include Later
- Size tables, missingness heatmap, distributions, bivariate plots.
- Model baselines (if done later).

---

**Grading alignment (Phase-1):** Team, topic/uses, sample, audience, limits & improvements,
provenance & access. (See project handout.)

