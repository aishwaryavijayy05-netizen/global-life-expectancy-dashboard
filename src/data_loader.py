import wbdata
import pandas as pd

# -----------------------------
# WORLD BANK INDICATORS
# -----------------------------

indicators = {
    "SP.DYN.LE00.IN": "life_expectancy_total",
    "SP.DYN.LE00.MA.IN": "life_expectancy_male",
    "SP.DYN.LE00.FE.IN": "life_expectancy_female",
    "SP.DYN.CDRT.IN": "death_rate",
    "SP.DYN.TFRT.IN": "fertility_rate",
}

print("Downloading data from World Bank...")

# -----------------------------
# DOWNLOAD MAIN DATASET
# -----------------------------

df = wbdata.get_dataframe(indicators)

# Convert index into columns
df = df.reset_index()

print("Main dataset downloaded.")

# -----------------------------
# CLEAN COLUMN NAMES
# -----------------------------

df.columns = [
    "country",
    "year",
    "life_expectancy_total",
    "life_expectancy_male",
    "life_expectancy_female",
    "death_rate",
    "fertility_rate"
]

# -----------------------------
# FIX YEAR FORMAT
# -----------------------------

df["year"] = df["year"].astype(str)
df["year"] = df["year"].str[:4]
df["year"] = df["year"].astype(int)

print("Year column cleaned.")

# -----------------------------
# DOWNLOAD COUNTRY METADATA
# -----------------------------

countries = wbdata.get_countries()

metadata = []

for country in countries:
    metadata.append({
        "country": country["name"],
        "region": country["region"]["value"],
        "income_group": country["incomeLevel"]["value"]
    })

metadata_df = pd.DataFrame(metadata)

print("Country metadata downloaded.")

# -----------------------------
# MERGE METADATA
# -----------------------------

df = df.merge(
    metadata_df,
    on="country",
    how="left"
)

print("Metadata merged.")

# -----------------------------
# REMOVE MISSING VALUES
# -----------------------------

# -----------------------------
# REMOVE MISSING VALUES
# -----------------------------

df = df.dropna(
    subset=["life_expectancy_total"]
)

# -----------------------------
# REMOVE AGGREGATE REGIONS
# -----------------------------

# -----------------------------
# REMOVE INVALID / AGGREGATE ROWS
# -----------------------------

df = df.dropna(
    subset=["region", "income_group"]
)

df = df[
    (df["region"] != "Aggregates") &
    (df["income_group"] != "Aggregates") &
    (df["income_group"] != "Not classified")
]

print("Aggregate and invalid rows removed.")

print("Aggregate regions removed.")

print("Missing values removed.")

# -----------------------------
# SAVE CLEAN DATASET
# -----------------------------

output_path = "data/processed/master_dataset.csv"

df.to_csv(output_path, index=False)

print(f"Dataset saved to: {output_path}")

# Preview
print(df.head())