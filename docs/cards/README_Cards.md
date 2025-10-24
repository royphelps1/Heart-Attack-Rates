# 📘 Phase-2 Notebook Reference Cards

##  `02_make_dataset.ipynb` — *SBP-Only Mini Pipeline*
**Purpose:**  
Create a small, beginner-friendly Phase-2 output focused only on SBP cleaning.

**Inputs:**  
- `../data/raw/heart_attack_china.csv`

**Steps:**  
1. Rename `Blood_Pressure` → `SBP`  
2. Convert `SBP` to numeric  
3. Add `SBP_missing` flag  
4. Create `SBP_hypertensive` (`SBP ≥ 140` → 1 else 0)

**Outputs:**  
- `../data/processed/heart_attack_china_clean.csv`  
- `../data/processed/heart_attack_china_final.csv`

**Edit if:**  
- Column name differs → update `"Blood_Pressure"` rename line  
- Threshold changes → adjust the `140` in hypertensive rule  

---

##  `04_phase2_all_in_notebook.ipynb` — *All-in-One Cleaner for Analysis*
**Purpose:**  
Build two fully reusable datasets — analysis-ready and model-ready — directly inside Jupyter.  
Optional WHO context support (adds mean BP column).

**Inputs:**  
- `../data/raw/heart_attack_china.csv`  
- *(Optional)* `../data/external/who_health_china.csv`

**Steps:**  
1. Normalize column names  
2. Trim string whitespace  
3. Convert Yes/No → 1/0  
4. Derive engineered features:  
   - `SBP`, `SBP_missing`, `SBP_hypertensive`  
   - `Gender_simple` (M/F)  
   - `Smoker_flag`  
   - `Age_band` bins  
   - `RiskFactor_count` (Hypertension, Diabetes, Obesity, CKD, Family History, Previous HA)  
5. *(Optional)* Add `WHO_overall_mean_BP` (country-level context)

**Outputs:**  
- `../data/processed/heart_attack_china_analysis_ready.csv`  
- `../data/processed/heart_attack_china_model_ready.csv`

**Edit if:**  
- Risk factor column names differ → update list in `candidates`  
- You want new bins/features → change `bins`, `labels`, or `keep_cols`  
- WHO join by year/sex → replace mean aggregation with merge logic  
