import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the prepared data
X_train = pd.read_csv("/home/ayyan/the-current news  website project/X_train.csv")
X_test = pd.read_csv("/home/ayyan/the-current news  website project/X_test.csv")
y_train = pd.read_csv(
    "/home/ayyan/the-current news  website project/y_train.csv"
).squeeze()
y_test = pd.read_csv(
    "/home/ayyan/the-current news  website project/y_test.csv"
).squeeze()

# Train the best performing model (XGBoost) on the full training data
xgb_model = XGBRegressor(random_state=42)
xgb_model.fit(X_train, y_train)

# Make predictions on the test set
predictions = xgb_model.predict(X_test)

# --- Plot 1: Actual vs. Predicted Prices ---
def plot_actual_vs_predicted(y_test, predictions, plot_path):
    plot_df = pd.DataFrame({"Actual Price": y_test, "Predicted Price": predictions})
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x="Actual Price", y="Predicted Price", data=plot_df, alpha=0.6)
    min_val = min(plot_df["Actual Price"].min(), plot_df["Predicted Price"].min())
    max_val = max(plot_df["Actual Price"].max(), plot_df["Predicted Price"].max())
    plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', lw=2)
    plt.title("Actual vs. Predicted House Prices (XGBoost)")
    plt.xlabel("Actual Price (PKR)")
    plt.ylabel("Predicted Price (PKR)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close() # Close the plot to free memory
    print(f"Plot saved to {plot_path}")

# --- Plot 2: Residual Plot ---
def plot_residuals_vs_predicted(y_test, predictions, plot_path):
    residuals = y_test - predictions
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=predictions, y=residuals, alpha=0.6)
    plt.axhline(y=0, color='red', linestyle='--', lw=2)
    plt.title("Residuals vs. Predicted Values")
    plt.xlabel("Predicted Price (PKR)")
    plt.ylabel("Residuals (Actual - Predicted)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()
    print(f"Plot saved to {plot_path}")

# --- Plot 3: Feature Importance Plot ---
def plot_feature_importance(model, features_names, plot_path):
    importance = model.feature_importances_
    feature_importance_df = pd.DataFrame({'Feature': features_names, 'Importance': importance})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
    plt.title("Feature Importance (XGBoost)")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()
    print(f"Plot saved to {plot_path}")

# --- Plot 4: Distribution of Residuals ---
def plot_residuals_distribution(y_test, predictions, plot_path):
    residuals = y_test - predictions
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True)
    plt.title("Distribution of Residuals")
    plt.xlabel("Residuals (Actual - Predicted)")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()
    print(f"Plot saved to {plot_path}")

# Call the plotting functions
plot_actual_vs_predicted(y_test, predictions,
                         "/home/ayyan/the-current news  website project/actual_vs_predicted_prices.png")
plot_residuals_vs_predicted(y_test, predictions,
                            "/home/ayyan/the-current news  website project/residuals_vs_predicted.png")
plot_feature_importance(xgb_model, X_test.columns,
                        "/home/ayyan/the-current news  website project/feature_importance.png")
plot_residuals_distribution(y_test, predictions,
                            "/home/ayyan/the-current news  website project/residuals_distribution.png")