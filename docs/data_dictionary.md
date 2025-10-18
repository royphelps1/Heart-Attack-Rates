# Data Dictionary – heart_attack_china.csv

This table lists the columns as detected, with inferred types and quick examples.

| Column                 | Type (inferred)   |   Missing % |   Unique | Range/Examples                                | Allowed values (top)                                                                                                                                   |
|:-----------------------|:------------------|------------:|---------:|:----------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Patient_ID             | numeric           |           0 |   239266 | 1 – 239266                                    |                                                                                                                                                        |
| Age                    | numeric           |           0 |       60 | 30 – 89                                       |                                                                                                                                                        |
| Gender                 | text/categorical  |           0 |        2 | Male, Female                                  | `Female` (119948), `Male` (119318)                                                                                                                     |
| Smoking_Status         | text/categorical  |           0 |        2 | Non-Smoker, Smoker                            | `Non-Smoker` (119697), `Smoker` (119569)                                                                                                               |
| Hypertension           | text/categorical  |           0 |        2 | No, Yes                                       | `No` (174557), `Yes` (64709)                                                                                                                           |
| Diabetes               | text/categorical  |           0 |        2 | No, Yes                                       | `No` (212794), `Yes` (26472)                                                                                                                           |
| Obesity                | text/categorical  |           0 |        2 | Yes, No                                       | `No` (167521), `Yes` (71745)                                                                                                                           |
| Cholesterol_Level      | text/categorical  |           0 |        3 | Normal, Low, High                             | `Normal` (80091), `High` (79620), `Low` (79555)                                                                                                        |
| Air_Pollution_Exposure | text/categorical  |           0 |        3 | High, Medium, Low                             | `Medium` (119593), `Low` (71654), `High` (48019)                                                                                                       |
| Physical_Activity      | text/categorical  |           0 |        3 | High, Low, Medium                             | `Low` (80086), `Medium` (79930), `High` (79250)                                                                                                        |
| Diet_Score             | text/categorical  |           0 |        3 | Moderate, Healthy, Poor                       | `Moderate` (79954), `Healthy` (79656), `Poor` (79656)                                                                                                  |
| Stress_Level           | text/categorical  |           0 |        3 | Low, Medium, High                             | `Low` (80120), `High` (79857), `Medium` (79289)                                                                                                        |
| Alcohol_Consumption    | text/categorical  |           0 |        2 | Yes, No                                       | `No` (167156), `Yes` (72110)                                                                                                                           |
| Family_History_CVD     | text/categorical  |           0 |        2 | No, Yes                                       | `No` (179740), `Yes` (59526)                                                                                                                           |
| Healthcare_Access      | text/categorical  |           0 |        3 | Good, Poor, Moderate                          | `Poor` (79912), `Moderate` (79711), `Good` (79643)                                                                                                     |
| Rural_or_Urban         | text/categorical  |           0 |        2 | Rural, Urban                                  | `Rural` (143507), `Urban` (95759)                                                                                                                      |
| Region                 | text/categorical  |           0 |        5 | Eastern, Central, Western, Northern, Southern | `Western` (48100), `Eastern` (47959), `Southern` (47826), `Central` (47694), `Northern` (47687)                                                        |
| Province               | text/categorical  |           0 |        8 | Beijing, Qinghai, Henan, Guangdong, Sichuan   | `Guangdong` (30162), `Beijing` (30064), `Shandong` (30025), `Shanghai` (29932), `Qinghai` (29917), `Sichuan` (29850), `Henan` (29767), `Gansu` (29549) |
| Hospital_Availability  | text/categorical  |           0 |        3 | Low, High, Medium                             | `High` (79848), `Medium` (79829), `Low` (79589)                                                                                                        |
| TCM_Use                | text/categorical  |           0 |        2 | Yes, No                                       | `No` (143949), `Yes` (95317)                                                                                                                           |
| Employment_Status      | text/categorical  |           0 |        3 | Unemployed, Employed, Retired                 | `Retired` (79872), `Unemployed` (79756), `Employed` (79638)                                                                                            |
| Education_Level        | text/categorical  |           0 |        4 | Primary, Secondary, Higher, None              | `Higher` (59942), `Primary` (59901), `Secondary` (59806), `None` (59617)                                                                               |
| Income_Level           | text/categorical  |           0 |        3 | Low, Middle, High                             | `High` (80149), `Low` (79797), `Middle` (79320)                                                                                                        |
| Blood_Pressure         | numeric           |           0 |       90 | 90 – 179                                      |                                                                                                                                                        |
| Chronic_Kidney_Disease | text/categorical  |           0 |        2 | Yes, No                                       | `No` (203597), `Yes` (35669)                                                                                                                           |
| Previous_Heart_Attack  | text/categorical  |           0 |        2 | No, Yes                                       | `No` (215306), `Yes` (23960)                                                                                                                           |
| CVD_Risk_Score         | numeric           |           0 |       90 | 10 – 99                                       |                                                                                                                                                        |
| Heart_Attack           | text/categorical  |           0 |        2 | No, Yes                                       | `No` (210195), `Yes` (29071)                                                                                                                           |

---

## Normalized Columns (Phase 1 Additions)

These fields come from the raw data and will be added during preprocessing to make analysis and modeling easier. We are not introducing new medical facts.

###  Boolean flags (derived from existing columns)

| New column         | Source column        | Rule / values                       | Type    |
|--------------------|-----------------------|-------------------------------------|---------|
| has_hypertension   | Hypertension          | Yes → True, No → False              | boolean |
| has_diabetes       | Diabetes              | Yes → True, No → False              | boolean |
| has_dyslipidemia   | Cholesterol_Level     | High → True, Low/Normal → False     | boolean |
| is_smoker          | Smoking_Status        | Smoker → True, Non-Smoker → False   | boolean |
| is_obese           | Obesity               | Yes → True, No → False              | boolean |
| tcm_use            | TCM_Use               | Yes → True, No → False              | boolean |
| is_rural           | Rural_or_Urban        | Rural → True, Urban → False         | boolean |

---

###  Ordinal encodings (stored as integers)

These columns will be mapped to ordered numeric values for Phase 1 EDA and later modeling:

- **Air_Pollution_Exposure:** Low = 0, Medium = 1, High = 2  
- **Physical_Activity:** Low = 0, Moderate = 1, High = 2  
- **Diet_Score:** Poor = 0, Moderate = 1, Healthy = 2  
- **Healthcare_Access:** Poor = 0, Moderate = 1, Good = 2  
- **Hospital_Availability:** Low = 0, Medium = 1, High = 2  
- **Income_Level:** Low = 0, Middle = 1, High = 2  

---



### Missing data handling

We will apply the following approach in the preprocessing notebook:

- **Categorical:** fill with `"Unknown"` or mode   
- **Numeric:** median fill  

Note: In our sample, `Education_Level` may include some missing values. We will re-check and update the Missing % in this dictionary if needed.

---

### Note on data leakage

`CVD_Risk_Score` stays in the dataset for EDA, but we will **exclude it from any baseline predictive modeling in Phase 2** unless confirmed safe.

---

### Output location

After normalization, we will save the processed file to:  
`data/processed/heart_attack_china_enriched.csv`
