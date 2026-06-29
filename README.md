# 💳 Fraud Detection Project

## 📌 Overview
This project analyzes financial transaction data to identify fraudulent activities using Exploratory Data Analysis (EDA) and Machine Learning preprocessing techniques.

The notebook explores transaction patterns, creates new features, visualizes important trends, and prepares the dataset for fraud detection models.

---

## 📂 Dataset
The dataset contains transaction records with features such as:

- Transaction Type
- Transaction Amount
- Sender & Receiver Balances
- Transaction Time (Step)
- Fraud Label (`isFraud`)
- Flagged Fraud (`isFlaggedFraud`)

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📊 Exploratory Data Analysis

The project includes:

- Dataset inspection
- Missing value analysis
- Fraud distribution
- Transaction type analysis
- Fraud rate by transaction type
- Transaction amount distribution
- Amount vs Fraud visualization
- Fraud occurrence over time
- Correlation heatmap
- High-risk transaction analysis

---

## ⚙️ Feature Engineering

Two additional features were created:

- `balanceDifforg`
- `balanceDiffdest`

These features represent balance changes before and after each transaction.

---

## 🤖 Machine Learning Preparation

The notebook prepares the data by:

- Removing unnecessary columns
- Separating numerical and categorical features
- Applying StandardScaler
- Applying One-Hot Encoding
- Splitting the dataset into training and testing sets

The preprocessing pipeline is built using Scikit-learn's `ColumnTransformer`.

---

## 📁 Project Structure

```
Fraud-Detection-Project/
│
├── analysis_model.ipynb
├── AIML Dataset.csv
├── fraud_detection.py
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

- Train multiple ML models
- Hyperparameter tuning
- Handle class imbalance (SMOTE)
- Feature selection
- Model comparison
- Deploy with Streamlit
- Docker deployment
## Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | **99.97%** |
| Precision | **96%** |
| Recall | **82%** |
| F1-Score | **88%** |

---

## 📈 Project Goal

The main objective is to build a machine learning pipeline capable of detecting fraudulent financial transactions with high accuracy while understanding the underlying transaction patterns through data analysis.
