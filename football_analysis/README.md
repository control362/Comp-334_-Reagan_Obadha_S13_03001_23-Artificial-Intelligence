# International Football Results Analysis — Exercise 1

## Description
Analysis of international football match results from 1872 to 2024 using the Kaggle dataset. Covers basic exploration, goals analysis, match outcomes, home advantage, and visualizations.

## Project Structure
```
football_analysis/
│
├── data/
│   └── results.csv
│
├── notebooks/
│   └── Football_Analysis.ipynb
│
├── README.md
└── requirements.txt
```

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Dataset
The dataset (`results.csv`) should be in the `data/` folder.
Download from: https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017

### 3. Run the notebook
```bash
cd notebooks
jupyter notebook Football_Analysis.ipynb
```

## Questions Answered
1. How many matches are in the dataset?
2. Earliest and latest year in the data
3. Number of unique countries
4. Most frequent home team
5. Average goals per match
6. Highest scoring match
7. Home vs away goals comparison
8. Most common total goals value
9. Percentage of home wins
10. Does home advantage exist?
11. Country with most wins historically

## Visualizations
- Histogram of goals per match
- Bar chart of match outcomes (Home Win / Away Win / Draw)
- Top 10 teams by total wins
- Goals trend over decades (bonus)
