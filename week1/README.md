# 📊 Week 1: Data Acquisition, Cleaning & Exploratory Data Analysis (EDA)

## 🎯 Task Objective
Week 1 simulates the foundational data preparation process essential for any production data science workflow. Using the **World Happiness Report** dataset (`world_happiness_report.csv`), the primary focus is data profiling, missing value handling, schema validation, and initial exploratory data analysis to uncover baseline patterns in global well-being metrics.

---

## 📦 Deliverables Summary

| Deliverable | File | Description |
| :--- | :--- | :--- |
| **Comprehensive Report** | [The World Happiness Story.docx](file:///d:/YUVA/week1/The%20World%20Happiness%20Story.docx) | Primary technical report detailing acquisition, cleaning rationales, and exploratory findings. |
| **Task Documentation** | [Week 1_Task .docx](file:///d:/YUVA/week1/Week%201_Task%20.docx) | Project task assignment report outlining methodology and initial observations. |

---

## 🔍 Key Methodological Steps

### 1. Data Acquisition & Profiling
* Acquired multi-year World Happiness Report records comprising 1,231 rows across 14 columns: `Country`, `Region`, `Happiness Rank`, `Happiness Score`, `Standard Error`, `Economy (GDP per Capita)`, `Family`, `Health (Life Expectancy)`, `Freedom`, `Trust (Government Corruption)`, `Generosity`, `Dystopia Residual`, and `year`.
* Audited schema distributions and identified structural concatenation inconsistencies in 2017–2022 records.

### 2. Data Cleaning & Preprocessing
* **Missing Value Filtering**: Isolated complete cases across core socio-economic dimensions.
* **Deduplication**: Verified unique `(Country, year)` observation pairs.
* **Leakage Prevention**: Identified target-dependent columns (`Happiness Rank`, `Dystopia Residual`) to exclude from downstream predictive modeling.
* **Data Type Rectification**: Converted numeric indicators to standard 64-bit floating point structures.

### 3. Exploratory Data Analysis (EDA) Insights
* **Univariate Distributions**: National happiness scores follow an approximately normal distribution centered at a global median of $\approx 5.286$ (ranging from $2.839$ in Togo/Burundi to $7.587$ in Switzerland).
* **Bivariate Associations**: Strong preliminary correlations observed between subjective well-being and economic prosperity (GDP per capita) and healthy life expectancy.

---

## 💻 Python Pipeline Snippet

```python
import pandas as pd

# Load dataset
df = pd.read_csv('../world_happiness_report.csv')

# Core feature definitions
features = [
    'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)',
    'Freedom', 'Trust (Government Corruption)', 'Generosity'
]

# Cleaning and inspection
clean_df = df.dropna(subset=features + ['Happiness Score']).copy()
clean_df = clean_df.drop_duplicates(subset=['Country', 'year'])

print("Clean dataset dimensions:", clean_df.shape)
print(clean_df[features + ['Happiness Score']].describe())
```
