import pandas as pd
import re

csv_path = "/home/ayyan/the-current news  website project/zameen_properties.csv"


def clean_price(price_str):
    if isinstance(price_str, str):
        price_str = price_str.replace(",", "").strip()
        if "Crore" in price_str:
            value = float(price_str.replace("Crore", "").strip())
            return value * 10_000_000  # 1 Crore = 10,000,000
        elif "Lac" in price_str:
            value = float(price_str.replace("Lac", "").strip())
            return value * 100_000  # 1 Lac = 100,000
    return None


def clean_area(area_str):
    if isinstance(area_str, str):
        match = re.match(r"([\d\.]+)" + " (Marla|Kanal)", area_str, re.IGNORECASE)
        if match:
            value = float(match.group(1))
            unit = match.group(2).lower()
            if unit == "marla":
                return value * 272.25  # Convert Marla to Sq Ft
            elif unit == "kanal":
                return value * 5445  # Convert Kanal to Sq Ft
    return None


try:
    df = pd.read_csv(csv_path)
    print("Original DataFrame head:")
    print(df.head())

    # Clean Price column
    df["Price_Cleaned"] = df["Price"].apply(clean_price)

    # Clean Beds and Baths columns
    df["Beds_Cleaned"] = pd.to_numeric(df["Beds"], errors="coerce").astype("Int64")
    df["Baths_Cleaned"] = pd.to_numeric(df["Baths"], errors="coerce").astype("Int64")

    # Clean Area column
    df["Area_SqFt"] = df["Area"].apply(clean_area)

    print("\nDataFrame head after cleaning:")
    print(df.head())

    # Save the cleaned data to a new CSV or overwrite the old one
    df.to_csv(csv_path, index=False)
    print(f"\nCleaned data saved to {csv_path}")

except FileNotFoundError:
    print(f"Error: The file {csv_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
