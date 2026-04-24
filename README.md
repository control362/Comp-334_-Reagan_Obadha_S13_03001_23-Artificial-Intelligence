# Artificial Intelligence (COMP 334) Assignments

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

This repository contains the data science and machine learning assignments for the **COMP 334: Artificial Intelligence** unit.

## Repository Structure

The workspace is divided into two primary projects, each containing its respective datasets, scripts, Jupyter notebooks, and documentation.

### 1. [Titanic Survival Prediction (`titanic_assignment/`)](./titanic_assignment)
A comprehensive machine learning pipeline addressing the classic Kaggle Titanic challenge. This project aims to predict passenger survival based on various demographic and travel attributes.
* **Key Features:**
  * Exploratory Data Analysis (EDA) of the Titanic dataset
  * Automated data cleaning pipeline (handling missing values, format standardizations)
  * Feature engineering (deck extraction, family size calculations, title parsing)
  * Feature selection (correlation matrix, thresholding)
  * Predictive classification modeling

### 2. [International Football Match Analysis (`football_analysis/`)](./football_analysis)
An exploratory data analysis project focusing on a vast historical dataset of international football matches. 
* **Key Features:**
  * Aggregation and statistical analysis of historical game data
  * Trend visualizations over time (growth of international matches)
  * Performance metrics (home vs. away advantages, highest scoring teams)
  * Tournament-specific breakdowns (e.g., FIFA World Cup vs. friendly matches)

## Setup & Installation

To run the projects locally, clone the repository and install the required dependencies.

```powershell
# Clone the repository
git clone https://github.com/control362/Comp-334_-Reagan_Obadha_S13_03001_23-Artificial-Intelligence.git

# Navigate into the project folder
cd "Comp-334_-Reagan_Obadha_S13_03001_23-Artificial-Intelligence"

# Install requirements for Titanic assignment
pip install -r titanic_assignment/requirements.txt
```

Each subdirectory contains its own standalone notebooks and scripts that can be executed independently. Please refer to any secondary `README.md` files within those folders for more granular instructions on running specific pipelines.
