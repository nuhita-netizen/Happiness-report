import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Set style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

output_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(output_dir, '..', 'world_happiness_report.csv')

print("1. Loading dataset...")
df = pd.read_csv(data_path)
print(f"Original shape: {df.shape}")

# Inspect columns and handle missing data
features = [
    'Economy (GDP per Capita)',
    'Family',
    'Health (Life Expectancy)',
    'Freedom',
    'Trust (Government Corruption)',
    'Generosity'
]
target = 'Happiness Score'

# Filter complete cases
clean_df = df.dropna(subset=features + [target]).copy()
print(f"Cleaned dataset shape: {clean_df.shape}")

X = clean_df[features]
y = clean_df[target]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
print(f"Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}")

# Scaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define models
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Decision Tree": DecisionTreeRegressor(max_depth=5, random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=6, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.08, max_depth=3, random_state=42)
}

results = []
trained_models = {}

print("\n2. Training and Evaluating Models...")
for name, model in models.items():
    # Use scaled data for linear/ridge, unscaled for trees
    if name in ["Linear Regression", "Ridge Regression"]:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='r2')
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
        
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    trained_models[name] = (model, y_pred)
    results.append({
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "Test R2": r2,
        "CV R2 (Mean)": cv_scores.mean(),
        "CV R2 (Std)": cv_scores.std()
    })

results_df = pd.DataFrame(results)
print("\nModel Evaluation Summary:")
print(results_df.to_string(index=False))

# --- Visualizations ---
print("\n3. Generating Performance Visualizations...")

# Viz 1: Model Comparison (R2 and RMSE)
fig, ax1 = plt.subplots(figsize=(10, 5), dpi=300)
x_pos = np.arange(len(results_df))
width = 0.35

rects1 = ax1.bar(x_pos - width/2, results_df['Test R2'], width, label='Test R² Score', color='#1f77b4', edgecolor='black', alpha=0.85)
ax1.set_ylabel('R² Score (Higher is better)', color='#1f77b4', fontweight='bold')
ax1.set_ylim(0.6, 1.0)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(results_df['Model'], fontweight='bold')

ax2 = ax1.twinx()
rects2 = ax2.bar(x_pos + width/2, results_df['RMSE'], width, label='RMSE (Lower is better)', color='#ff7f0e', edgecolor='black', alpha=0.85)
ax2.set_ylabel('RMSE (Score Points)', color='#ff7f0e', fontweight='bold')
ax2.set_ylim(0, 0.8)

# Adding values above bars
for rect in rects1:
    h = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., h + 0.01, f'{h:.3f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
for rect in rects2:
    h = rect.get_height()
    ax2.text(rect.get_x() + rect.get_width()/2., h + 0.01, f'{h:.3f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title('Machine Learning Model Performance Benchmark (Week 4)', fontsize=13, fontweight='bold', pad=15)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'viz_model_comparison.png'))
plt.close()

# Viz 2: Actual vs Predicted (Best Model: Random Forest / Gradient Boosting)
best_model_name = "Gradient Boosting"
_, best_pred = trained_models[best_model_name]

fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
sns.scatterplot(x=y_test, y=best_pred, color='#2ca02c', edgecolor='black', s=70, alpha=0.8, ax=ax)
min_val = min(y_test.min(), best_pred.min()) - 0.2
max_val = max(y_test.max(), best_pred.max()) + 0.2
ax.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction Line (y=x)')

ax.set_xlabel('Actual Happiness Score', fontweight='bold')
ax.set_ylabel('Predicted Happiness Score', fontweight='bold')
ax.set_title(f'Actual vs. Predicted Happiness Score ({best_model_name})', fontsize=13, fontweight='bold')
ax.legend(frameon=True)
best_r2 = results_df.loc[results_df['Model'] == best_model_name, 'Test R2'].values[0]
best_rmse = results_df.loc[results_df['Model'] == best_model_name, 'RMSE'].values[0]
ax.text(0.05, 0.90, f'Test R² = {best_r2:.3f}\nRMSE = {best_rmse:.3f}', transform=ax.transAxes,
        fontsize=10, bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8, edgecolor='gray'))

fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'viz_actual_vs_predicted.png'))
plt.close()

# Viz 3: Residual Distribution & Residuals vs Fitted
residuals = y_test - best_pred
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5), dpi=300)

# Residual histogram / KDE
sns.histplot(residuals, kde=True, color='#9467bd', edgecolor='black', ax=ax1)
ax1.axvline(0, color='red', linestyle='--', linewidth=1.5)
ax1.set_title('Residual Error Distribution', fontweight='bold')
ax1.set_xlabel('Residual (Actual - Predicted)')
ax1.set_ylabel('Frequency')

# Residual vs Fitted
ax2.scatter(best_pred, residuals, color='#d62728', alpha=0.7, edgecolor='k')
ax2.axhline(0, color='black', linestyle='--', linewidth=1.5)
ax2.set_title('Residuals vs. Fitted Values', fontweight='bold')
ax2.set_xlabel('Predicted Score (Fitted)')
ax2.set_ylabel('Residual')

fig.suptitle(f'Model Error & Residual Diagnostics ({best_model_name})', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'viz_residuals_analysis.png'))
plt.close()

# Viz 4: Feature Importance
rf_model = trained_models["Random Forest"][0]
importances = pd.Series(rf_model.feature_importances_, index=features).sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
colors = plt.cm.viridis(np.linspace(0.2, 0.85, len(importances)))
bars = ax.barh(importances.index, importances.values, color=colors, edgecolor='black', alpha=0.85)
ax.set_xlabel('Relative Importance (Gini / Impurity Reduction)', fontweight='bold')
ax.set_title('Feature Importance in Predicting World Happiness (Random Forest)', fontsize=13, fontweight='bold')

for bar in bars:
    w = bar.get_width()
    ax.text(w + 0.008, bar.get_y() + bar.get_height()/2, f'{w*100:.1f}%', va='center', fontsize=10, fontweight='bold')

ax.set_xlim(0, max(importances.values) + 0.08)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'viz_feature_importance.png'))
plt.close()

print("All tasks completed and visualizations generated successfully!")
