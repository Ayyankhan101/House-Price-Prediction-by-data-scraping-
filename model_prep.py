import pandas as pd
from sklearn.model_selection import train_test_split

csv_path = "/home/ayyan/the-current news  website project/zameen_properties.csv"

try:
    df = pd.read_csv(csv_path)

    # Drop rows where the target variable (Price_Cleaned) is NaN
    df.dropna(subset=["Price_Cleaned"], inplace=True)

    # Select features and target
    features = ["Beds_Cleaned", "Baths_Cleaned", "Area_SqFt"]
    target = "Price_Cleaned"

    X = df[features]
    y = df[target]

    # Handle remaining NaNs in features by filling with the mean
    # This is a simple imputation strategy. More advanced methods can be used.
    X = X.fillna(X.mean())

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Data preparation complete.")
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"y_test shape: {y_test.shape}")

    # Save processed data for the next steps (Modeling)
    X_train.to_csv(
        "/home/ayyan/the-current news  website project/X_train.csv",
        index=False,
    )
    X_test.to_csv(
        "/home/ayyan/the-current news  website project/X_test.csv", index=False
    )
    y_train.to_csv(
        "/home/ayyan/the-current news  website project/y_train.csv",
        index=False,
    )
    y_test.to_csv(
        "/home/ayyan/the-current news  website project/y_test.csv", index=False
    )

    print("Processed data saved to X_train.csv, X_test.csv, y_train.csv, y_test.csv")

except FileNotFoundError:
    print(f"Error: The file {csv_path} was not found.")
except Exception as e:
    print(f"An error occurred during data preparation: {e}")
