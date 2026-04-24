# Titanic Survival Prediction — Assignment 2

## Description
This project performs data cleaning, feature engineering, and feature selection on the Titanic dataset to build a foundation for a survival prediction model.

## Project Structure
```
titanic_assignment/
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── notebooks/
│   └── Titanic_Feature_Engineering.ipynb
│
├── scripts/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   └── feature_selection.py
│
├── README.md
└── requirements.txt
```

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Download the dataset
Download `train.csv` and `test.csv` from [Kaggle Titanic](https://www.kaggle.com/competitions/titanic/data) and place them in the `data/` folder.

### 3. Run scripts in order
```bash
cd scripts
python data_cleaning.py
python feature_engineering.py
python feature_selection.py
```

### 4. Or explore the notebook
```bash
cd notebooks
jupyter notebook Titanic_Feature_Engineering.ipynb
```

## Approach

### Data Cleaning
- **Age**: Filled missing values with the median
- **Embarked**: Filled 2 missing rows with the mode
- **Cabin**: Dropped — over 77% of values were missing
- **Outliers**: Capped Fare and Age at the 99th percentile
- **Consistency**: Standardized Sex column to lowercase; removed duplicates

### Features Engineered
| Feature | Description |
|---|---|
| FamilySize | SibSp + Parch + 1 |
| IsAlone | 1 if FamilySize == 1 |
| Title | Extracted from Name (Mr, Mrs, Miss, Master, Other) |
| Deck | Derived from Cabin (Unknown if Cabin missing) |
| AgeGroup | Child / Teen / Adult / Senior |
| FarePerPerson | Fare / FamilySize |
| Fare_log | Log transform of Fare |
| Age_log | Log transform of Age |

### Feature Selection
- Dropped non-predictive columns (PassengerId, Name, Ticket)
- Removed highly correlated features (threshold > 0.95)
- Used Random Forest feature importance to keep features with importance > 0.01

## Key Findings
- Title is a strong predictor (captures both gender and social status)
- Passengers travelling alone had lower survival rates
- Fare and Pclass are highly related — one can be dropped
- Log transforming Fare significantly reduces skewness
