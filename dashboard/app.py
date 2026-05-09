import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Global Life Expectancy Dashboard",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/processed/master_dataset.csv"
    )

df = load_data()

# =====================================================
# TITLE
# =====================================================

st.title("🌍 Global Life Expectancy Dashboard")

st.markdown("""
This dashboard analyzes global trends in:
- Life expectancy
- Fertility rate
- Death rate
- Gender-based life expectancy differences

Data Source: World Bank
""")

# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.header("🔎 Dashboard Filters")

selected_country = st.sidebar.selectbox(
    "Select Country",
    sorted(df["country"].unique())
)

selected_income = st.sidebar.multiselect(
    "Select Income Group",
    options=sorted(df["income_group"].unique()),
    default=sorted(df["income_group"].unique())
)

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)

# =====================================================
# FILTER DATA
# =====================================================

filtered_df = df[
    (df["country"] == selected_country) &
    (df["income_group"].isin(selected_income)) &
    (df["region"].isin(selected_region))
]

# =====================================================
# KPI METRICS
# =====================================================

latest_year = filtered_df["year"].max()

latest_data = filtered_df[
    filtered_df["year"] == latest_year
]

life_exp = latest_data[
    "life_expectancy_total"
].mean()

fertility = latest_data[
    "fertility_rate"
].mean()

death_rate = latest_data[
    "death_rate"
].mean()

gender_gap = (
    latest_data["life_expectancy_female"].mean()
    -
    latest_data["life_expectancy_male"].mean()
)

# =====================================================
# KPI DISPLAY
# =====================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Life Expectancy",
    f"{life_exp:.2f}"
)

col2.metric(
    "Fertility Rate",
    f"{fertility:.2f}"
)

col3.metric(
    "Death Rate",
    f"{death_rate:.2f}"
)

col4.metric(
    "Gender Gap",
    f"{gender_gap:.2f}"
)
st.subheader("📈 Trend Analysis")
# =====================================================
# LIFE EXPECTANCY TREND
# =====================================================

life_fig = px.line(
    filtered_df,
    x="year",
    y="life_expectancy_total",
    title="Life Expectancy Over Time"
)

st.plotly_chart(
    life_fig,
    use_container_width=True
)

# =====================================================
# FERTILITY TREND
# =====================================================

fertility_fig = px.line(
    filtered_df,
    x="year",
    y="fertility_rate",
    title="Fertility Rate Over Time"
)

st.plotly_chart(
    fertility_fig,
    use_container_width=True
)
st.subheader("👨 Male vs 👩 Female Comparison")
# =====================================================
# GENDER COMPARISON
# =====================================================

gender_df = filtered_df.melt(
    id_vars=["year"],
    value_vars=[
        "life_expectancy_male",
        "life_expectancy_female"
    ],
    var_name="gender",
    value_name="life_expectancy"
)

gender_fig = px.line(
    gender_df,
    x="year",
    y="life_expectancy",
    color="gender",
    title="Male vs Female Life Expectancy"
)

st.plotly_chart(
    gender_fig,
    use_container_width=True
)
# =====================================================
# WORLD MAP
# =====================================================

st.subheader("🌍 Global Life Expectancy Map (2023)")

latest_global = df[df["year"] == 2023]

map_fig = px.choropleth(
    latest_global,
    locations="country",
    locationmode="country names",
    color="life_expectancy_total",
    hover_name="country",
    color_continuous_scale="Viridis",
    title="Global Life Expectancy"
)

map_fig.update_layout(
    template="plotly_white"
)

st.plotly_chart(
    map_fig,
    width="stretch"
)