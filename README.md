# 🌍 World Happiness Report — 4-Week Data Analytics & Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.9.0-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/pandas-2.2.3-150458?logo=pandas)
![Status](https://img.shields.io/badge/Status-Completed-success)

Comprehensive end-to-end data analytics, statistical hypothesis testing, and machine learning predictive pipeline analyzing global happiness determinants using the **World Happiness Report** (2015–2022).

---

## 📁 Repository Structure

```plaintext
YUVA/
│
├── .gitignore                          # Excludes temporary Office files, caches & envs
├── requirements.txt                    # Project dependencies
├── README.md                           # Master project documentation
├── world_happiness_report.csv          # Multi-year dataset (2015–2022)
│
├── week1/                              # Week 1: Data Understanding & Problem Framing
│   ├── The World Happiness Story.docx
│   └── Week 1_Task .docx
│
├── week2/                              # Week 2: Exploratory Data Analysis & Visualizations
│   ├── viz1_region_distribution.png    # Regional distribution of happiness scores
│   ├── viz2_multivariate_scatter.png   # GDP vs. Happiness with Freedom/Health hue
│   ├── viz3_correlation_matrix.png     # Heatmap of Pearson correlation coefficients
│   ├── viz4_top_bottom_disparity.png   # Comparative disparity between top & bottom nations
│   └── The World Happiness Story.docx
│
├── week3/                              # Week 3: Statistical Inference & Hypothesis Testing
│   ├── hypothesis_ttest_validation.png # Two-sample t-test distributions
│   ├── WEEK 3_task.docx
│   └── Screenshots/
│
└── week4/                              # Week 4: Machine Learning Modeling & Diagnostics
    ├── train_models.py                 # End-to-end Scikit-Learn training & evaluation pipeline
    ├── generate_doc.py                 # Script generating the finalized deliverable DOCX
    ├── Week4_ML_Report.docx            # Finalized Week 4 Report with diagnostics
    ├── viz_model_comparison.png        # R² and RMSE benchmark across 5 ML algorithms
    ├── viz_actual_vs_predicted.png     # Parity plot (Actual vs. Predicted)
    ├── viz_residuals_analysis.png      # Residual distribution & heteroscedasticity checks
    └── viz_feature_importance.png      # Gini feature importances from Random Forest
```

---

## 🚀 Week 4: Machine Learning Pipeline Overview

### 1. Algorithms Implemented
* **Multiple Linear Regression (Baseline)**: Parametric baseline for linear coefficients.
* **Ridge Regression ($L_2$ Regularization)**: Penalized regression to handle GDP-Health collinearity.
* **Decision Tree Regressor**: Non-parametric tree partitioner (`max_depth=5`).
* **Random Forest Regressor**: Ensemble bagging model (100 estimators).
* **Gradient Boosting Regressor**: Sequential boosting optimizer (`learning_rate=0.08`).

---

### 2. Model Performance Benchmark

| Model Architecture | MAE | RMSE | Test $R^2$ | 5-Fold CV $R^2$ (Mean $\pm$ Std) |
| :--- | :---: | :---: | :---: | :---: |
| **Linear Regression** | **0.353** | **0.444** | **0.866** | $0.721 \pm 0.067$ |
| **Ridge Regression** | **0.353** | **0.444** | **0.866** | $0.721 \pm 0.067$ |
| **Random Forest Regressor** | 0.392 | 0.481 | 0.844 | **$0.751 \pm 0.056$** |
| **Gradient Boosting Regressor** | 0.404 | 0.489 | 0.838 | $0.732 \pm 0.051$ |
| **Decision Tree Regressor** | 0.479 | 0.642 | 0.721 | $0.565 \pm 0.123$ |

---

### 3. Model Diagnostic Visualizations

| Model Comparison | Actual vs Predicted |
| :---: | :---: |
| ![Model Benchmark](week4/viz_model_comparison.png) | ![Actual vs Predicted](week4/viz_actual_vs_predicted.png) |

| Residual Diagnostics | Feature Importance |
| :---: | :---: |
| ![Residuals](week4/viz_residuals_analysis.png) | ![Feature Importance](week4/viz_feature_importance.png) |

---

## 🛠️ Quickstart & Reproduction

### 1. Clone Repository & Install Dependencies
```bash
git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
cd YUVA
pip install -r requirements.txt
```

### 2. Run the ML Pipeline & Generate Reports
```bash
# Execute model training, validation, and chart generation
python week4/train_models.py

# Compile the final Word report deliverable
python week4/generate_doc.py
```

---

## 👤 Author
* **YUVA Data Analytics Internship**
* Focus: Statistical Analytics, Exploratory Data Analysis & Predictive Machine Learning
