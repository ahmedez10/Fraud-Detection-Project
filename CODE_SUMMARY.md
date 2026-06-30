# Fraud Detection Project - Code Summary

## Project Overview

This project builds a Machine Learning pipeline to detect fraudulent financial transactions. It includes data exploration, feature engineering, preprocessing, model training, evaluation, and model saving.

---

# Project Workflow

Dataset
↓
Load Data
↓
Exploratory Data Analysis (EDA)
↓
Feature Engineering
↓
Data Preprocessing
↓
Train/Test Split
↓
Model Training
↓
Model Evaluation
↓
Save Trained Model

---

## 1. Import Libraries

Libraries used:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Purpose:
- Data manipulation
- Data visualization
- Machine Learning

---

## 2. Load Dataset

The CSV dataset is loaded using Pandas.

```python
df = pd.read_csv("AIML Dataset.csv")
```

---

## 3. Data Exploration

Performed:

- Dataset information
- Data types
- Missing values
- Dataset dimensions
- Fraud distribution
- Flagged fraud distribution

---

## 4. Exploratory Data Analysis

Visualizations include:

- Transaction type distribution
- Fraud rate by transaction type
- Transaction amount distribution
- Amount vs Fraud
- Fraud over time (Step)
- Correlation Heatmap
- Fraud by transaction type

Purpose:
Understand transaction behavior and identify fraud patterns.

---

## 5. Feature Engineering

Created two additional features:

### balanceDifforg

Difference between:

Old Sender Balance − New Sender Balance

### balanceDiffdest

Difference between:

New Receiver Balance − Old Receiver Balance

These features improve fraud detection performance.

---

## 6. Data Cleaning

Removed unnecessary columns:

- step
- nameOrig
- nameDest
- isFlaggedFraud

---

## 7. Data Preprocessing

Categorical feature:

- type

Numerical features:

- amount
- oldbalanceOrg
- newbalanceOrig
- oldbalanceDest
- newbalanceDest
- balanceDifforg
- balanceDiffdest

Processing:

- StandardScaler
- OneHotEncoder
- ColumnTransformer

---

## 8. Train/Test Split

Dataset split:

- 70% Training
- 30% Testing

Stratified sampling is used to preserve fraud ratio.

---

## 9. Machine Learning Model

Model used:

Random Forest Classifier

Reasons:

- Handles nonlinear relationships
- Works well with mixed features
- Robust against overfitting
- High performance on tabular datasets

---

## 10. Model Evaluation

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Results:

| Metric | Score |
|---------|-------|
| Accuracy | 99.97% |
| Precision | 96% |
| Recall | 82% |
| F1 Score | 88% |

Confusion Matrix

True Positive : 2030

True Negative : 1,906,228

False Positive : 94

False Negative : 434

---

## 11. Model Export

The trained model is saved as:

```
fraud_detection_model.pkl
```

This model can later be used in:

- Streamlit
- Flask
- FastAPI
- Power BI Integration

---

# Project Files

```
Fraud-Detection-Project/
│
├── analysis_model.ipynb
├── fraud_detection.py
├── fraud_detection_model.pkl
├── requirements.txt
├── README.md
├── LICENSE
└── CODE_SUMMARY.md
```

---

# Future Improvements

- Apply SMOTE to handle class imbalance
- Compare Random Forest with XGBoost
- Hyperparameter tuning
- Streamlit deployment
- Power BI Dashboard
- Docker deployment

---

# Author

Ahmed Ezzat

