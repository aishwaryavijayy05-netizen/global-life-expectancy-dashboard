import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv(
    "data/processed/master_dataset.csv"
)

print("Dataset loaded.")

# -----------------------------
# GROUP DATA
# -----------------------------

income_trend = (
    df.groupby(["year", "income_group"])
    ["life_expectancy_total"]
    .mean()
    .reset_index()
)

print("Data grouped successfully.")

# -----------------------------
# CREATE LINE CHART
# -----------------------------

fig = px.line(
    income_trend,
    x="year",
    y="life_expectancy_total",
    color="income_group",
    title="Life Expectancy Over Time by Income Group",
    labels={
        "year": "Year",
        "life_expectancy_total": "Life Expectancy",
        "income_group": "Income Group"
    }
)

# -----------------------------
# IMPROVE LAYOUT
# -----------------------------

fig.update_layout(
    template="plotly_white",
    title_font_size=24,
    hovermode="x unified"
)

# -----------------------------
# SHOW CHART
# -----------------------------

fig.show()
# =====================================================
# WORLD MAP VISUALIZATION
# =====================================================

# -----------------------------
# FILTER 2023 DATA
# -----------------------------

latest_data = df[df["year"] == 2023]

print("2023 data prepared.")

# -----------------------------
# CREATE WORLD MAP
# -----------------------------

map_fig = px.choropleth(
    latest_data,
    locations="country",
    locationmode="country names",
    color="life_expectancy_total",
    hover_name="country",
    color_continuous_scale="Viridis",
    title="Global Life Expectancy in 2023"
)

# -----------------------------
# IMPROVE LAYOUT
# -----------------------------

map_fig.update_layout(
    template="plotly_white",
    title_font_size=24
)

# -----------------------------
# SHOW MAP
# -----------------------------

map_fig.show()
# =====================================================
# SANKEY DIAGRAM
# =====================================================

print("Preparing Sankey diagram data...")

# -----------------------------
# CREATE LABELS
# -----------------------------

labels = [
    "Very Low",
    "Low",
    "Medium",
    "High",
    "Very High"
]

# -----------------------------
# GET 1960 DATA
# -----------------------------

data_1960 = df[df["year"] == 1960][
    ["country", "life_expectancy_total"]
].copy()

# -----------------------------
# GET 2023 DATA
# -----------------------------

data_2023 = df[df["year"] == 2023][
    ["country", "life_expectancy_total"]
].copy()

# -----------------------------
# CREATE BUCKETS
# -----------------------------

data_1960["bucket_1960"] = pd.qcut(
    data_1960["life_expectancy_total"],
    5,
    labels=labels
)

data_2023["bucket_2023"] = pd.qcut(
    data_2023["life_expectancy_total"],
    5,
    labels=labels
)

# -----------------------------
# MERGE BOTH YEARS
# -----------------------------

transition = data_1960.merge(
    data_2023,
    on="country"
)

# -----------------------------
# COUNT FLOWS
# -----------------------------

flows = (
    transition.groupby(
        ["bucket_1960", "bucket_2023"]
    )
    .size()
    .reset_index(name="count")
)

print("Flow counts created.")

# -----------------------------
# CREATE NODE LABELS
# -----------------------------

left_labels = [
    label + " (1960)"
    for label in labels
]

right_labels = [
    label + " (2023)"
    for label in labels
]

all_labels = left_labels + right_labels

# -----------------------------
# MAP SOURCES/TARGETS
# -----------------------------

source_map = {
    label: i
    for i, label in enumerate(labels)
}

target_map = {
    label: i + 5
    for i, label in enumerate(labels)
}

sources = flows["bucket_1960"].map(source_map)

targets = flows["bucket_2023"].map(target_map)

values = flows["count"]

# -----------------------------
# CREATE SANKEY FIGURE
# -----------------------------

sankey_fig = go.Figure(data=[
    go.Sankey(
        node=dict(
            pad=20,
            thickness=20,
            label=all_labels
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values
        )
    )
])

# -----------------------------
# UPDATE LAYOUT
# -----------------------------

sankey_fig.update_layout(
    title_text="Country Movement in Life Expectancy Categories (1960 → 2023)",
    font_size=12
)

# -----------------------------
# SHOW SANKEY
# -----------------------------

sankey_fig.show()