# 🌍 Global Life Expectancy BI Dashboard

## 📌 Project Overview

This project analyzes global health trends using World Bank data.

The analysis focuses on:
- Life expectancy at birth
- Male vs female life expectancy
- Fertility rate
- Death rate
- Income group comparisons
- Regional analysis

The project includes:
- Data engineering pipeline
- Statistical analysis
- Interactive visualizations
- BI dashboard development

---

# 📊 Data Source

Data obtained from the World Bank API.

Indicators used:

| Indicator | Code |
|---|---|
| Life expectancy (total) | SP.DYN.LE00.IN |
| Life expectancy (male) | SP.DYN.LE00.MA.IN |
| Life expectancy (female) | SP.DYN.LE00.FE.IN |
| Death rate | SP.DYN.CDRT.IN |
| Fertility rate | SP.DYN.TFRT.IN |

---

# 🛠️ Tech Stack

- Python
- Pandas
- Plotly
- Streamlit
- World Bank API

---

# 📈 Statistical Analysis

The following analytical questions were explored:

1. Which income group experienced the largest change in gender life expectancy gap between 1960 and 2023?

2. How has variability in life expectancy changed across income groups?

3. Which countries show the strongest correlation between fertility rate and life expectancy?

---

# 🌍 Visualizations

The project includes:

- Time-series line charts
- Interactive world choropleth map
- Sankey diagram showing country movement between life expectancy categories
- Interactive dashboard with filters

---

# 📊 Dashboard Features

Users can filter by:
- Country
- Region
- Income group

Dashboard includes:
- KPI metrics
- Trend analysis
- Gender comparison charts
- Global map visualization

---

# 🚀 How to Run the Project

## 1. Clone Repository

```bash
git clone <your-repository-link>
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Generate Dataset

```bash
py src/data_loader.py
```

## 4. Run Dashboard

```bash
py -m streamlit run dashboard/app.py
```

---

# 📁 Project Structure

```text
bi-assignment/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data_loader.py
│   ├── analysis.py
│   └── visualizations.py
│
├── dashboard/
│   └── app.py
│
├── notebooks/
│
├── README.md
├── requirements.txt
└── main.py
```

---

# 📌 Key Insights

- Lower-middle-income countries experienced the largest increase in gender life expectancy gap.
- Global life expectancy has improved significantly since 1960.
- Fertility rate generally shows a negative correlation with life expectancy.
- Major regional disparities remain visible across the world.

---

# 👨‍💻 Author

<Your Name>