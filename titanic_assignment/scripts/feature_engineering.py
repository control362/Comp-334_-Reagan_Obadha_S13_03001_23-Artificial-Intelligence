import pandas as pd
import numpy as np
import re

def create_family_features(df):
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    return df

def extract_title(df):
    # Extract title from Name column
    df['Title'] = df['Name'].apply(lambda x: re.search(r',\s*(\w+)\.', x).group(1) if re.search(r',\s*(\w+)\.', x) else 'Unknown')

    # Group rare titles
    common_titles = ['Mr', 'Miss', 'Mrs', 'Master']
    df['Title'] = df['Title'].apply(lambda x: x if x in common_titles else 'Other')

    return df

def extract_deck(df):
    # Cabin column was dropped, so we just set Deck to Unknown
    # If Cabin column exists, extract first letter
    if 'Cabin' in df.columns:
        df['Deck'] = df['Cabin'].apply(lambda x: str(x)[0] if pd.notnull(x) else 'Unknown')
    else:
        df['Deck'] = 'Unknown'
    return df

def create_age_groups(df):
    bins = [0, 12, 18, 60, 100]
    labels = ['Child', 'Teen', 'Adult', 'Senior']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)
    return df

def create_fare_per_person(df):
    df['FarePerPerson'] = df['Fare'] / df['FamilySize']
    return df

def encode_features(df):
    # One-hot encode nominal features
    df = pd.get_dummies(df, columns=['Sex', 'Embarked', 'Title', 'Deck', 'AgeGroup'], drop_first=False)
    return df

def log_transform(df):
    # Log transform skewed features
    df['Fare_log'] = np.log1p(df['Fare'])
    df['Age_log'] = np.log1p(df['Age'])
    return df

def engineer_features(input_path, output_path):
    df = pd.read_csv(input_path)

    df = create_family_features(df)
    df = extract_title(df)
    df = extract_deck(df)
    df = create_age_groups(df)
    df = create_fare_per_person(df)
    df = log_transform(df)
    df = encode_features(df)

    print("Features after engineering:", df.columns.tolist())
    df.to_csv(output_path, index=False)
    print(f"Saved engineered data to {output_path}")

if __name__ == "__main__":
    engineer_features("../data/train_cleaned.csv", "../data/train_engineered.csv")
