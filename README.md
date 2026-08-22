# 🌍 World Happiness Report — End-to-End Data Science Project

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.9.0-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/pandas-2.2.3-150458?logo=pandas)
![Status](https://img.shields.io/badge/Status-Completed-success)

This repository contains the complete **4-Week Data Science & Analytics Project** analyzing global determinants of subjective well-being using the **World Happiness Report** dataset (`world_happiness_report.csv`). The project covers the full data science lifecycle: data cleaning, exploratory data analysis, visual storytelling, statistical hypothesis testing, and supervised machine learning.

---

## 📊 Dataset Overview: `world_happiness_report.csv`

The **World Happiness Report** is a landmark survey of the state of global happiness. The happiness scores and rankings use data from the Gallup World Poll, based on answers to the main life evaluation question known as the **Cantril ladder** (where respondents rate their current life on a scale from 0 to 10).

### Data Dictionary

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **`Country`** | String / Text | Name of the nation surveyed (e.g., Switzerland, Denmark, India). |
| **`Region`** | String / Text | Geographic region (e.g., Western Europe, Sub-Saharan Africa, Latin America). |
| **`Happiness Rank`** | Integer | Global rank of the country according to its overall Happiness Score ($1 = \text{Happiest}$). |
| **`Happiness Score`** | Float | National average subjective well-being score measured on the 0–10 Cantril Ladder scale. |
| **`Standard Error`** | Float | Standard error of the national happiness score estimate. |
| **`Economy (GDP per Capita)`** | Float | Statistical extent to which GDP per capita accounts for the national happiness score. |
| **`Family`** | Float | Extent to which social support networks contribute to the happiness score. |
| **`Health (Life Expectancy)`** | Float | Extent to which healthy life expectancy contributes to the happiness score. |
| **`Freedom`** | Float | National perception of personal freedom to make life choices. |
| **`Trust (Government Corruption)`** | Float | Extent to which public and private sector corruption perception impacts well-being. |
| **`Generosity`** | Float | Extent to which national philanthropic and altruistic giving contributes to happiness. |
| **`Dystopia Residual`** | Float | Benchmark baseline score relative to a hypothetical worst-case nation (*Dystopia*). |
| **`year`** | Integer | Data collection / reporting year (spanning **2015 to 2022**). |

---

## 📁 4-Week Project Roadmap

Each weekly milestone is thoroughly documented in its own dedicated directory with deliverables, scripts, and visualizations:

| Phase | Milestone | Focus Areas & Deliverables | Folder Link |
| :---: | :--- | :--- | :---: |
| **Week 1** | **Data Acquisition & Cleaning** | Data profiling, missing value auditing, schema validation, and preliminary exploratory distributions. | [Explore Week 1 ➔](week1/) |
| **Week 2** | **Advanced Visual Storytelling** | Multi-dimensional narratives, regional distributions, multivariate scatter plots, and correlation heatmaps. | [Explore Week 2 ➔](week2/) |
| **Week 3** | **Statistical Hypothesis Testing** | Parametric inference, two-sample independent $t$-tests ($t=16.84, p < 0.0001$), and confidence intervals. | [Explore Week 3 ➔](week3/) |
| **Week 4** | **Machine Learning & Evaluation** | Supervised classification and regression models (Linear, Ridge, Decision Tree, Random Forest, Gradient Boosting). | [Explore Week 4 ➔](week4/) |

---

## 📂 Repository Directory Structure

```plaintext
Happiness-report/
│
├── .gitignore                          # Excludes temporary Office files, caches & envs
├── requirements.txt                    # Project dependencies for one-command setup
├── README.md                           # Master repository & dataset documentation
├── world_happiness_report.csv          # Multi-year World Happiness dataset (2015–2022)
│
├── week1/                              # Week 1: Data Acquisition & Exploratory Analysis
│   ├── README.md                       # Week 1 documentation & cleaning rationales
│   ├── The World Happiness Story.docx  # Deliverable document
│   └── Week 1_Task .docx               # Deliverable document
│
├── week2/                              # Week 2: Visual Storytelling with Python
│   ├── README.md                       # Visual narrative documentation
│   ├── viz1_region_distribution.png    # Regional happiness score distributions
│   ├── viz2_multivariate_scatter.png   # GDP vs. Happiness with Freedom/Health hue
│   ├── viz3_correlation_matrix.png     # Heatmap of Pearson correlation coefficients
│   ├── viz4_top_bottom_disparity.png   # Comparative disparity between top & bottom nations
│   └── The World Happiness Story.docx  # Final narrative report
│
├── week3/                              # Week 3: Statistical Inference & Hypothesis Testing
│   ├── README.md                       # Statistical test breakdown & p-value results
│   ├── hypothesis_ttest_validation.png # Two-sample t-test distributions
│   ├── WEEK 3_task.docx                # Formal statistical analysis report
│   └── Screenshots/                    # Visual test verification captures
│
└── week4/                              # Week 4: Machine Learning Modeling & Diagnostics
    ├── README.md                       # ML architecture breakdown, ROC, and benchmarks
    ├── train_models.py                 # Scikit-Learn training & evaluation pipeline
    ├── generate_doc.py                 # Script generating the finalized deliverable DOCX
    ├── Week4_ML_Report.docx            # Finalized Week 4 Report with diagnostics
    ├── viz_model_comparison.png        # R² and RMSE benchmark across 5 ML algorithms
    ├── viz_actual_vs_predicted.png     # Parity plot (Actual vs. Predicted)
    ├── viz_residuals_analysis.png      # Residual distribution & heteroscedasticity checks
    └── viz_feature_importance.png      # Gini feature importances from Random Forest
```

---

## 🛠️ Installation & Reproduction

### 1. Clone the Repository
```bash
git clone https://github.com/nuhita-netizen/Happiness-report.git
cd Happiness-report
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Pipeline Scripts
```bash
# Run Week 4 ML models and generate all evaluation plots
python week4/train_models.py

# Compile the final Word report deliverable
python week4/generate_doc.py
```

---

## 👤 Author
* **YUVA Data Analytics Internship**
* Focus: Statistical Analytics, Exploratory Data Analysis & Predictive Machine Learning
