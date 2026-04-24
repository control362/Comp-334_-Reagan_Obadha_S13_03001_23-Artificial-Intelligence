import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path)
    return df

def handle_missing_values(df):
    # Age: fill with median
    df['Age'].fillna(df['Age'].median(), inplace=True)

    # Embarked: fill with mode
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    # Fare: fill with median
    df['Fare'].fillna(df['Fare'].median(), inplace=True)

    # Cabin: too many missing, drop it (we'll extract Deck in feature engineering)
    df.drop(columns=['Cabin'], inplace=True)

    return df

def handle_outliers(df):
    # Cap Fare at 99th percentile
    fare_cap = df['Fare'].quantile(0.99)
    df['Fare'] = df['Fare'].clip(upper=fare_cap)

    # Cap Age at 99th percentile
    age_cap = df['Age'].quantile(0.99)
    df['Age'] = df['Age'].clip(upper=age_cap)

    return df

def fix_consistency(df):
    # Make sure Sex values are lowercase
    df['Sex'] = df['Sex'].str.lower().str.strip()

    # Remove duplicates if any
    df.drop_duplicates(inplace=True)

    return df

def clean_data(input_path, output_path):
    df = load_data(input_path)

    print("Original shape:", df.shape)
    print("Missing values:\n", df.isnull().sum())

    df = handle_missing_values(df)
    df = handle_outliers(df)
    df = fix_consistency(df)

    print("Cleaned shape:", df.shape)
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path}")

if __name__ == "__main__":
    clean_data("../data/train.csv", "../data/train_cleaned.csv")
