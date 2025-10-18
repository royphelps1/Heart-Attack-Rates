# DSCI-511 Project

## Phase 1 Dataset & Documentation

This repository currently uses the following dataset and documentation for Phase 1:

- **Dataset:** `heart_attack_china.csv` (stored in `data/raw/`)
- **Data Dictionary:** `docs/data_dictionary.md`
- **Normalized Variables Plan:** `docs/normalized_flags.md`
- **Phase 1 Report Scaffold:** `docs/Phase1_Report_Scaffold.md`

The cleaned/enriched output for Phase 1 will be written to:
`data/processed/heart_attack_china_enriched.csv`


Collaborative repo for our DSCI 511 course project (Jupyter + LaTeX). Private repo shared by a 4-person team.

**TEAM:**
- Evan Wessel
- Leland Weeks
- Shad Scarboro
- Roy Phelps

**Project Resources:**
- **Google Drive Folder (large data / alternate option):** [(https://drive.google.com/drive/folders/1vawtjJAgRlAttClKjX46eAY9A2p-jNFe?usp=share_link)]
- **GitHub Repo (main code/paper hub):** [(https://github.com/royphelps1/DSCI-511-Project)]

## Note
- Code and notebooks go in the folders listed below.
- Upload files directly on the GitHub website into the correct folder.
- Paper is written in LaTeX or Jupyter Markdown, which ever is required `reports/paper/..`; figures/tables under `reports/`.
- Everyone may also work from the shared Google Drive folder if preferred; keep the same structure there.

## Repo Structure

```text
.
├── notebooks/           # Jupyter notebooks (EDA, experiments)
├── src/                 # Python modules reusable across notebooks
├── tests/               # Optional unit tests for src
├── data/
│   ├── raw/             # Original, immutable data dumps (not tracked by Git)
│   ├── processed/       # Cleaned/engineered data (not tracked by Git)
│   └── external/        # Third-party data (not tracked by Git)
├── reports/
│   ├── paper/           # LaTeX paper (main.tex)
│   ├── figures/         # Saved plots/diagrams
│   └── tables/          # Exported CSV/LaTeX tables
├── references/          # BibTeX (references.bib), notes
├── docs/                # Extra documentation (e.g., screenshots)
├── environment.yml      # Optional reproducible Conda environment
├── CONTRIBUTING.md      # Team workflow and conventions
└── .gitignore
```


## Collaboration Workflow (via GitHub Website)
- Go to the repo on GitHub and **navigate into the correct folder** first.
- Click **Add file → Upload files**.
- Drop your files:
  - Notebooks → `notebooks/`
  - Python helpers → `src/` (create a subfolder if needed)
  - LaTeX sections or Jupyter Markdown/images → `reports/paper/` and `reports/figures/`
  - References → `references/`
  - Screenshots/docs → `docs/`
- Add a short commit message and **Commit changes**.


## Jupyter Notebooks
- Use Jupyter Notebook or JupyterLab locally.
- Save your notebooks in `notebooks/` and push them to GitHub.
- In the shared Google Drive folder, keep the same folder names so it’s easy to sync.

## Paper
- Main file: `reports/paper/..`
- Add figures to `reports/figures/`.
- 
## Code Style
- Keep reusable logic in src/ and import into notebooks.
- If adding tests, place them in tests/ with pytest style.
- Use Python 3.x (an optional Conda environment is defined in environment.yml for consistency, but it’s not required if you already have Python installed).

## License
- Private class project.  Do not distribute without team consent.