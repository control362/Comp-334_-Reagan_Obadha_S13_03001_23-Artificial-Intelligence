import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def drop_irrelevant_columns(df):
    # Drop columns that are not useful for modeling
    cols_to_drop = ['PassengerId', 'Name', 'Ticket']
    cols_to_drop = [c for c in cols_to_drop if c in df.columns]
    df = df.drop(columns=cols_to_drop)
    return df

def remove_highly_correlated(df, target='Survived', threshold=0.95):
    # Correlation matrix (only numeric)
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.drop(columns=[target], errors='ignore').corr().abs()

    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    to_drop = [col for col in upper.columns if any(upper[col] > threshold)]

    print("Dropping highly correlated features:", to_drop)
    df = df.drop(columns=to_drop, errors='ignore')
    return df

def get_feature_importance(df, target='Survived'):
    X = df.drop(columns=[target])
    y = df[target]

    # Encode any remaining object columns
    for col in X.select_dtypes(include='object').columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))

    # Handle booleans
    X = X.astype(float)

    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X, y)

    importance_df = pd.DataFrame({
        'Feature': X.columns,
        'Importance': rf.feature_importances_
    }).sort_values(by='Importance', ascending=False)

    print("\nFeature Importances:")
    print(importance_df.to_string(index=False))

    return importance_df, X.columns.tolist()

def select_features(input_path, output_path):
    df = pd.read_csv(input_path)

    df = drop_irrelevant_columns(df)
    df = remove_highly_correlated(df)

    importance_df, selected_features = get_feature_importance(df)

    # Keep top features (importance > 0.01)
    top_features = importance_df[importance_df['Importance'] > 0.01]['Feature'].tolist()
    top_features.append('Survived')

    final_df = df[[c for c in top_features if c in df.columns]]
    final_df.to_csv(output_path, index=False)
    print(f"\nSelected {len(top_features)-1} features, saved to {output_path}")

if __name__ == "__main__":
    select_features("../data/train_engineered.csv", "../data/train_selected.csv")
