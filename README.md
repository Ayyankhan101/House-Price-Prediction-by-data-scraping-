# Real Estate Price Predictor with Web Scraping

This project demonstrates a complete data science pipeline, from data acquisition through web scraping to building and evaluating machine learning models for real estate price prediction.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Visualizations](#visualizations)

## Project Overview

The goal of this project is to predict house prices based on various features. Unlike typical datasets, this project involves scraping real-world data from a real estate website, handling its complexities, cleaning it, and then applying machine learning techniques to build a predictive model.

## Features

- **Web Scraping**: Dynamically collects real estate listing data from `zameen.com` using Selenium.
- **Data Cleaning**: Processes raw, unstructured data into a clean, usable format.
  - Converts price strings (e.g., "Crore", "Lac") to numerical values.
  - Standardizes area units (e.g., "Marla", "Kanal") to Square Feet.
  - Cleans and converts numerical features (Beds, Baths).
- **Data Preparation**: Splits data into training and testing sets, and handles missing values.
- **Machine Learning Modeling**: Trains and evaluates multiple regression models (Linear Regression, Random Forest, XGBoost).
- **Visualization**: Generates insightful plots to understand data distributions, model performance, and feature importance.

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create and activate a virtual environment:**

    It's highly recommended to use a virtual environment to manage project dependencies.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create `requirements.txt` after running the project once, or manually add `selenium`, `beautifulsoup4`, `pandas`, `scikit-learn`, `xgboost`, `matplotlib`, `seaborn`, `webdriver-manager` to it.)*

4.  **Install Firefox browser:**

    This project uses Selenium with Firefox. Ensure Firefox is installed on your system. If not, you can download it from [Mozilla Firefox](https://www.mozilla.org/firefox/new/).

## Usage

Run the scripts in the following order:

1.  **Scrape Data:**

    ```bash
    python3 scrape_zameen.py
    ```
    This script will scrape data from `zameen.com` and save it to `zameen_properties.csv`.

2.  **Clean Data:**

    ```bash
    python3 clean_data.py
    ```
    This script will clean the `zameen_properties.csv` file.

3.  **Prepare Data for Modeling:**

    ```bash
    python3 model_prep.py
    ```
    This script will prepare the data and save `X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`.

4.  **Train and Evaluate Models:**

    ```bash
    python3 train_model.py
    ```
    This script will train Linear Regression, Random Forest, and XGBoost models and print their evaluation metrics.

5.  **Generate Visualizations:**

    ```bash
    python3 visualize_results.py
    ```
    This script will generate several plots (e.g., `actual_vs_predicted_prices.png`, `residuals_vs_predicted.png`, `feature_importance.png`, `residuals_distribution.png`) in the project directory.

## Project Structure

```
.  # Project Root
├── .gitignore
├── pyproject.toml
├── .flake8
├── scrape_zameen.py
├── clean_data.py
├── model_prep.py
├── train_model.py
├── visualize_results.py
├── zameen_properties.csv  # Generated after scraping and cleaning
├── X_train.csv            # Generated after data preparation
├── X_test.csv             # Generated after data preparation
├── y_train.csv            # Generated after data preparation
├── y_test.csv             # Generated after data preparation
├── actual_vs_predicted_prices.png  # Generated after visualization
├── residuals_vs_predicted.png      # Generated after visualization
├── feature_importance.png          # Generated after visualization
└── residuals_distribution.png      # Generated after visualization
```

## Results

After running the `train_model.py` script, you will see the following evaluation metrics for the models:

*(Example results from a previous run:)*

```
--- Training Linear Regression Model ---
Linear Regression - MAE: 28846791.00, MSE: 2555921858959043.50, RMSE: 50556125.83, R2: 0.63

--- Training Random Forest Regressor Model ---
Random Forest Regressor - MAE: 32748167.99, MSE: 2475095432111714.00, RMSE: 49750330.97, R2: 0.64

--- Training XGBoost Regressor Model ---
XGBoost Regressor - MAE: 31208067.47, MSE: 2235400020281119.00, RMSE: 47280017.13, R2: 0.68
```

XGBoost Regressor generally performs best, explaining approximately 68% of the variance in house prices.

## Visualizations

Several plots are generated to help understand the data and model performance:

-   `actual_vs_predicted_prices.png`: A scatter plot comparing the actual house prices against the model's predicted prices. Points closer to the diagonal line indicate better predictions.
-   `residuals_vs_predicted.png`: Shows the distribution of prediction errors (residuals) against predicted values. Ideally, residuals should be randomly scattered around zero.
-   `feature_importance.png`: A bar chart indicating the relative importance of each feature (Beds, Baths, Area) in the XGBoost model's predictions.
-   `residuals_distribution.png`: A histogram showing the distribution of the residuals. Ideally, residuals should be normally distributed around zero.
