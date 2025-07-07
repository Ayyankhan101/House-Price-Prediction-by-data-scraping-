import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the prepared data
X_train = pd.read_csv("/home/ayyan/the-current news  website project/X_train.csv")
X_test = pd.read_csv("/home/ayyan/the-current news  website project/X_test.csv")
y_train = pd.read_csv(
    "/home/ayyan/the-current news  website project/y_train.csv"
).squeeze()  # .squeeze() to convert DataFrame to Series
y_test = pd.read_csv(
    "/home/ayyan/the-current news  website project/y_test.csv"
).squeeze()


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = mse**0.5  # Calculate RMSE manually
    r2 = r2_score(y_test, predictions)
    return mae, mse, rmse, r2


print("--- Training Linear Regression Model ---")
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
mae, mse, rmse, r2 = evaluate_model(linear_model, X_test, y_test)
print(
    f"Linear Regression - MAE: {mae:.2f}, MSE: {mse:.2f}, "
    f"RMSE: {rmse:.2f}, R2: {r2:.2f}"
)


print("\n--- Training Random Forest Regressor Model ---")
random_forest_model = RandomForestRegressor(random_state=42)
random_forest_model.fit(X_train, y_train)
mae, mse, rmse, r2 = evaluate_model(random_forest_model, X_test, y_test)
print(
    f"Random Forest Regressor - MAE: {mae:.2f}, MSE: {mse:.2f}, "
    f"RMSE: {rmse:.2f}, R2: {r2:.2f}"
)


print("\n--- Training XGBoost Regressor Model ---")
xgb_model = XGBRegressor(random_state=42)
xgb_model.fit(X_train, y_train)
mae, mse, rmse, r2 = evaluate_model(xgb_model, X_test, y_test)
print(
    f"XGBoost Regressor - MAE: {mae:.2f}, MSE: {mse:.2f}, "
    f"RMSE: {rmse:.2f}, R2: {r2:.2f}"
)
