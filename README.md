# DSCI-511 Project

Collaborative repo for our DSCI 511 course project (Jupyter + LaTeX). Private repo shared by a 4-person team.

**TEAM:**
- Evan Wessel
- Leland Weeks
- Shad Scarboro
- Roy Phelps

**Project Resources:**
- **Google Drive Folder (large data / alternate option):** [(https://drive.google.com/drive/folders/1vawtjJAgRlAttClKjX46eAY9A2p-jNFe?usp=share_link)]
- **GitHub Repo (main code/paper hub):** [(https://github.com/royphelps1/DSCI-511-Project)]

## TD
- Code and notebooks go in the folders listed below.
- Upload files directly on the GitHub website into the correct folder (see “Collaboration Workflow”).
- Large data lives only in the shared Google Drive folder, not in GitHub.
- Paper is written in LaTeX at `reports/paper/main.tex`; figures/tables under `reports/`.
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
  - LaTeX sections/images → `reports/paper/` and `reports/figures/`
  - References → `references/`
  - Screenshots/docs → `docs/`
- Add a short commit message and **Commit changes**.
- **Do not upload large data** — put it in the shared Google Drive folder.

> Tip: If you later want to use GitHub Desktop or the command line, that’s fine, but it’s optional.

## Jupyter Notebooks
- Use Jupyter Notebook or JupyterLab locally.
- Save your notebooks in `notebooks/` and push them to GitHub.
- In the shared Google Drive folder, keep the same folder names so it’s easy to sync.

## LaTeX Paper
- Main file: `reports/paper/main.tex`
- Add figures to `reports/figures/` and reference with `\includegraphics{../figures/your_figure}`
- BibTeX file: `references/references.bib`
- You can edit `.tex` files online or locally with a LaTeX editor.
- Optional build locally:
  ```bash
  latexmk -pdf -interaction=nonstopmode reports/paper/main.tex
## Code Style
- Keep reusable logic in src/ and import into notebooks.
- If adding tests, place them in tests/ with pytest style.
- Use Python 3.x (an optional Conda environment is defined in environment.yml for consistency, but it’s not required if you already have Python installed).

## License
- Private class project.  Do not distribute without team consent.
