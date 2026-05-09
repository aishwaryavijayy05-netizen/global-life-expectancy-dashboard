import pandas as pd

# -----------------------------
# LOAD DATASET
# -----------------------------

df = pd.read_csv("data/processed/master_dataset.csv")

print("Dataset loaded successfully.")

# -----------------------------
# CREATE GENDER GAP
# -----------------------------

df["gender_gap"] = (
    df["life_expectancy_female"] -
    df["life_expectancy_male"]
)

print("Gender gap calculated.")

# -----------------------------
# GROUP BY INCOME GROUP + YEAR
# -----------------------------

grouped = (
    df.groupby(["income_group", "year"])["gender_gap"]
    .mean()
    .reset_index()
)

# -----------------------------
# GET 1960 DATA
# -----------------------------

gap_1960 = grouped[grouped["year"] == 1960]

# -----------------------------
# GET 2023 DATA
# -----------------------------

gap_2023 = grouped[grouped["year"] == 2023]

# -----------------------------
# MERGE BOTH YEARS
# -----------------------------

comparison = gap_1960.merge(
    gap_2023,
    on="income_group",
    suffixes=("_1960", "_2023")
)

# -----------------------------
# CALCULATE CHANGE
# -----------------------------

comparison["change"] = (
    comparison["gender_gap_2023"] -
    comparison["gender_gap_1960"]
)

# -----------------------------
# SORT RESULTS
# -----------------------------

comparison = comparison.sort_values(
    by="change",
    ascending=False
)

# -----------------------------
# SHOW RESULTS
# -----------------------------

print("\nGender Gap Change by Income Group:\n")

print(comparison[
    [
        "income_group",
        "gender_gap_1960",
        "gender_gap_2023",
        "change"
    ]
])