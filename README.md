# Customer Churn Prediction - Machine Learning Project

## Project Overview
This project focuses on predicting whether a telecom customer will churn (leave the service) based on historical customer data. The goal is to help businesses identify customers at risk of leaving and take preventive actions to improve retention.

---

## Problem Statement
Telecom companies face customer loss due to churn. The objective of this project is to build a machine learning model that can predict customer churn using customer demographic, account, and service-related features.

---

## Dataset Information
- Dataset: IBM Telco Customer Churn Dataset
- Total Records: 7043 customers
- Features: 31 columns after preprocessing
- Target Variable: Churn (Yes/No converted to 0/1)

---

## Tools and Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Data Preprocessing Steps
- Handled missing values in TotalCharges
- Removed customerID column
- Converted categorical variables into numerical format using encoding techniques
- Applied one-hot encoding for multi-category features
- Converted boolean values to numerical format for model compatibility

---

## Exploratory Data Analysis (EDA)
The following insights were observed:
- Customers with low tenure are more likely to churn
- Month-to-month contract users show higher churn rates
- Higher monthly charges increase churn probability
- Long-term contract customers have lower churn rates

---

## Machine Learning Models Used
Two classification models were trained and evaluated:

1. Logistic Regression
2. Random Forest Classifier

---

## Model Evaluation Results

| Model | Accuracy | Recall (Churn Class) |
|------|----------|----------------------|
| Logistic Regression | 82% | 0.59 |
| Random Forest | 80% | 0.48 |

### Best Model
Logistic Regression performed better based on higher accuracy and better recall for churn detection.

---

## Evaluation Metrics Used
- Accuracy Score
- Confusion Matrix
- Precision
- Recall
- F1 Score

---

## Confusion Matrix Analysis
The models were evaluated using confusion matrices to understand correct and incorrect predictions:
- True Positives: Correctly predicted churn customers
- True Negatives: Correctly predicted non-churn customers
- False Positives: Incorrect churn predictions
- False Negatives: Missed churn customers

---

## Key Insights
- Early-stage customers are more likely to leave the service
- Contract type plays a major role in churn behavior
- Monthly charges significantly influence churn probability

---

## Conclusion
This project successfully demonstrates a machine learning approach to predict customer churn. The model can help businesses identify at-risk customers and improve retention strategies.

---

## Future Improvements
- Hyperparameter tuning for better accuracy
- Use advanced models such as XGBoost or LightGBM
- Deploy model using Streamlit or Flask
- Feature selection and optimization techniques

---

## Author
Preethi SS
