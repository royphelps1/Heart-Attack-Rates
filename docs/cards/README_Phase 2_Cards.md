# Phase-2 Notebook Reference Cards

---

## `02_make_dataset.ipynb` — *SBP-Only Mini Pipeline*
**Purpose:**  
Create a small, beginner-friendly preprocessing pipeline focused only on SBP cleaning.

**Inputs:**  
- `../data/raw/heart_attack_china.csv`

**Steps:**  
1. Rename `Blood_Pressure` → `SBP`  
2. Convert `SBP` to numeric  
3. Add `SBP_missing` flag  
4. Add `SBP_hypertensive` (`SBP ≥ 140` → 1 else 0)

**Outputs:**  
- `../data/processed/heart_attack_china_clean.csv`  
- `../data/processed/heart_attack_china_final.csv`

**Edit if:**  
- Column name differs → adjust `"Blood_Pressure"` rename  
- Hypertension threshold changes → update `140`

---

## `phase2_all_in_notebook.ipynb` — *Full Phase 2 Pipeline (Updated 12/5)*

**Purpose:**  
Produce all Phase-2 datasets used in the project:  
- Analysis-ready  
- Model-ready  
- WHO-enhanced  
- Air-quality-enhanced  

This pipeline now also integrates PM2.5 data from OpenAQ.

**Inputs:**  
- `../data/raw/heart_attack_china.csv`  
- WHO dataset: `../data/raw/who_health_china.csv`  
- Province → city mapping (embedded in notebook)  
- OpenAQ API (PM2.5)  
- OSM/Nominatim (OpenStreetMap) for city coordinates

**Steps:**  
1. Load and clean the raw heart-attack dataset  
2. Normalize string fields and categorical values  
3. Derive patient-level features:
   - `Gender_simple`  
   - Boolean flags for hypertension, diabetes, obesity, CKD, family history  
   - Risk-factor count  
4. Clean WHO dataset:
   - Filter to latest year  
   - Pivot to wide format  
   - Merge with patient-level data  
5. Geocode major cities for each province (Nominatim / OpenStreetMap)  
6. Query OpenAQ API:
   - Retrieve nearby PM2.5 station data  
   - Select most recent PM2.5 value per province  
   - Assign PM2.5 based on `Rural_or_Urban`  
7. Generate and save all Phase 2 processed datasets

**Outputs (Updated):**  
- `../data/processed/heart_attack_china_analysis_ready.csv`  
- `../data/processed/heart_attack_china_model_ready.csv`  
- `../data/processed/heart_attack_china_with_who_latest_by_sex.csv`  
- `../data/processed/heart_attack_china_with_air_quality.csv`  
- *Intermediate:* `../data/processed/province_air_quality.csv`

**Edit if:**  
- WHO file updates → adjust pivot logic  
- OpenAQ API limits or radius change → update query parameters  
- Province-to-city mappings change → edit the `cities = {}` dictionary  
