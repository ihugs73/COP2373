import numpy as np
import pandas as pd
import sys

PASS_MARK = 60  # ≥ 60 is a pass


def load_data(filename: str):
    """Load CSV and return (DataFrame, numeric‑only NumPy array)."""
    df = pd.read_csv(filename)
    grades = df.iloc[:, 2:].to_numpy(dtype=float)  # exams start at col index 2
    return df, grades


def per_exam_stats(grades: np.ndarray):
    """Return a dict of stats for each exam (column)."""
    stats = {}
    for idx in range(grades.shape[1]):
        col = grades[:, idx]
        stats[idx + 1] = {
            "mean":   np.mean(col),
            "median": np.median(col),
            "std":    np.std(col, ddof=1),
            "min":    np.min(col),
            "max":    np.max(col),
            "passed": int(np.sum(col >= PASS_MARK)),
            "failed": int(np.sum(col < PASS_MARK)),
        }
    return stats


def overall_stats(grades: np.ndarray):
    """Return aggregate stats across *all* exams for *all* students."""
    flat = grades.flatten()
    return {
        "mean":      np.mean(flat),
        "median":    np.median(flat),
        "std":       np.std(flat, ddof=1),
        "min":       np.min(flat),
        "max":       np.max(flat),
        "pass_pct":  np.sum(flat >= PASS_MARK) / flat.size * 100,
    }


def main(filename: str = "grades.csv"):
    df, grades = load_data(filename)

    # --- inspect dataset ----------------------------------------------------
    print("First five rows:")
    print(df.head(), "\n")

    # --- per‑exam statistics ------------------------------------------------
    print("Per‑exam statistics:")
    for exam, s in per_exam_stats(grades).items():
        print(f"Exam {exam}: "
              f"mean={s['mean']:.2f}, median={s['median']:.2f}, "
              f"std={s['std']:.2f}, min={s['min']:.0f}, max={s['max']:.0f}, "
              f"passed={s['passed']}, failed={s['failed']}")

    # --- overall statistics -------------------------------------------------
    o = overall_stats(grades)
    print("\nOverall statistics (all exams combined):")
    print(f"mean={o['mean']:.2f}, median={o['median']:.2f}, "
          f"std={o['std']:.2f}, min={o['min']:.0f}, max={o['max']:.0f}, "
          f"pass percentage={o['pass_pct']:.2f}%")


if __name__ == "__main__":
    # allow optional command‑line CSV path
    csv_file = sys.argv[1] if len(sys.argv) > 1 else "grades.csv"
    main(csv_file)
