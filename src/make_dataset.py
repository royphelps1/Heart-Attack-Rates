"""
make_dataset.py

Usage (from repo root):
    python src/make_dataset.py \
        --raw data/raw/heart_attack_china.csv \
        --interim data/interim/heart_attack_china_clean.csv \
        --final data/final/heart_attack_china_final.csv

This script mirrors the simple notebook steps:
1) Read raw CSV
2) Clean/rename SBP and add missing flag
3) Build final features (SBP_hypertensive)
4) Save interim and final CSVs
"""

import argparse
import sys
import pandas as pd


def read_raw(path: str) -> pd.DataFrame:
    # Read raw CSV safely with UTF-8 and low_memory=False for predictable dtypes.
    try:
        return pd.read_csv(path, encoding="utf-8", low_memory=False)
    except FileNotFoundError:
        print(f"[ERROR] Raw file not found: {path}")
        sys.exit(1)


def clean_sbp(df: pd.DataFrame) -> pd.DataFrame:
    """
    Beginner-cleaning step for SBP:
    - Rename Blood_Pressure -> SBP (if exists)
    - Coerce SBP to numeric (invalid parses -> NaN)
    - Add SBP_missing flag (True if NaN)
    """
    rename_map = {}
    if "Blood_Pressure" in df.columns:
        rename_map["Blood_Pressure"] = "SBP"
    # If your column is already 'SBP', this does nothing.
    df = df.rename(columns=rename_map)

    if "SBP" not in df.columns:
        print("[ERROR] Column 'Blood_Pressure' or 'SBP' not found in the raw dataset.")
        sys.exit(1)

    # Coerce to numeric and build missing flag
    df["SBP"] = pd.to_numeric(df["SBP"], errors="coerce")
    df["SBP_missing"] = df["SBP"].isna()

    return df


def build_final(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build minimal final dataset features.
    - SBP_hypertensive: 1 if SBP >= 140 else 0 (Int64 for nullable integer)
    - Keep only a small, clear set of columns
    """
    HYPERTENSION_SBP = 140
    df["SBP_hypertensive"] = (df["SBP"] >= HYPERTENSION_SBP).astype("Int64")

    keep = ["SBP", "SBP_missing", "SBP_hypertensive"]
    # If your project requires an ID or other columns, add them to 'keep' above.
    final_df = df[keep].copy()
    return final_df


def write_csv(df: pd.DataFrame, path: str) -> None:
    """Write CSV with UTF-8 encoding. Creates parent folders if needed."""
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Rebuild Phase 2 final dataset (SBP-only).")
    parser.add_argument("--raw", required=True, help="Path to raw CSV (e.g., data/raw/heart_attack_china.csv)")
    parser.add_argument("--interim", required=True, help="Path to write the cleaned interim CSV")
    parser.add_argument("--final", required=True, help="Path to write the final dataset CSV")
    args = parser.parse_args()

    print(" Reading raw CSV ...")
    raw_df = read_raw(args.raw)

    print(" Cleaning SBP ...")
    clean_df = clean_sbp(raw_df)
    write_csv(clean_df, args.interim)
    print(f" Wrote interim CSV: {args.interim}")

    print(" Building final features ...")
    final_df = build_final(clean_df)
    write_csv(final_df, args.final)
    print(f" Wrote final CSV: {args.final}")

    print(" Done. Final dataset ready.")


if __name__ == "__main__":
    main()
