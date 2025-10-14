
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
Paste a small sample (10–20 rows) and link to your data dictionary.

```python
import pandas as pd
pd.set_option("display.max_columns", None)
df = pd.read_csv("data/raw/heart_attack_china.csv", low_memory=False)
df.head(10)
```
- **Data dictionary:** see `docs/data_dictionary.md`

## 5) Provenance & Access
- Source, license/terms, de-identification.  
- How others can obtain or access (file location in repo and any usage notes).

## 6) Limitations & Improvements
- Missingness, potential biases, lack of time fields, measurement units, etc.  
- Planned improvements: add `record_date` (synthetic), derive flags, optional external benchmarks.

## 7) Enrichment Plan (Optional for Phase-1)
- Geo present → potential joins with public health indicators (population, PM2.5, beds/1k, GDP/cap).  
- Document keys needed for joins (province/city standardization).

## 8) Reproducibility
How to rebuild processed data from raw:
```python
# scripts shown inline for Phase-1:
# 1) derive risk flags + synthetic record_date
# (Paste from docs_derived_risk_flags.md or import from a 'src/' script)
```
- Folder layout and exact commands to run.

## Appendix A: Figures/Tables to Include Later
- Size tables, missingness heatmap, distributions, bivariate plots.
- Model baselines (if done later).

---

**Grading alignment (Phase-1):** Team, topic/uses, sample, audience, limits & improvements,
provenance & access. (See project handout.)

