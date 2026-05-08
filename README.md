# SWE485 Project: Employee Attrition Prediction System

## 1. Group Information
### Group 2
### Members
- Lana Alturki – 444200666
- Najla Alanazi - 444200597
- Nouf Alkathiri – 444200698
- Jood Alshehri - 444200773
- Fatema Maklad - 444200114
- Nouf Alerwan - 444200408
- Nada AlShaibi - 444200546

---

## 2. Task Distribution

### Phase 1
| Member | Responsibilities |
|--------|-----------------|
| **Jood** | Data preprocessing & feature engineering (outlier handling, BusinessTravel encoding, age discretization, satisfaction features), final dataset validation/export, insights & challenges |
| **Nada** | Data preprocessing (cleaning, target encoding, one-hot encoding, scaling), dataset preparation for modeling |
| **Fatema** | XGBoost model, evaluation, misclassification analysis |
| **Nouf AlKathiri** | Logistic Regression model, model selection & justification |
| **Najla** | SVM model, performance comparison |
| **Lana** | Exploratory Data Analysis (validation, class balance, feature relationships, visualizations) |
| **Nouf AlErewan** | Problem definition, dataset selection & justification, dataset overview |

### Phase 2
| Member | Responsibilities |
|--------|-----------------|
| **Jood** | K-means Clustering algorithm implementation |
| **Nada** | Quantitative analysis, prompt selection, ethics section |
| **Fatema** | Integration & Documentation Lead |
| **Nouf AlKathiri** | DBSCAN algorithm implementation|
| **Najla** |Generative AI API setup and implementation |
| **Lana** | Hierarchical Clustering algorithm implementation|
| **Nouf AlErewan** | Prompt templates, Testing, quantitative analysis |

---

## 3. Project Overview & Motivation

### Phase 1: Predictive Analysis of Employee Attrition

Employee attrition represents a critical challenge for organizations, as companies often struggle to identify the specific factors that lead employees to leave. With a large workforce, the challenge lies in using employee data to uncover hidden patterns that indicate whether an employee is likely to leave the company.

To address this, we are using the IBM HR Employee Attrition dataset, a structured tabular dataset containing 1,470 records and 35 features. This data, covering demographics, job roles, and satisfaction levels, allows us to build a binary classification system to predict the target variable "Attrition" (Yes/No).

### Phase 2: From Prediction to Explanation

Phase 2 builds on the foundation established in Phase 1 by adding two new layers of intelligence to the system. First, unsupervised learning (clustering) is applied to group employees into behavioral profiles, uncovering hidden patterns that go beyond simple attrition prediction. Second, Generative AI is integrated to transform raw predictions into personalized, human-readable retention advice that HR managers can act on directly. Together, these components turn the system from a prediction tool into a complete HR decision-support pipeline.

---

## 4. Conclusion

This project demonstrates a complete machine learning pipeline applied to the real-world problem of employee attrition. Starting from raw HR data, the system progresses through three stages: supervised learning to predict attrition, unsupervised learning to identify behavioral clusters, and generative AI to explain predictions in human-readable form.

The key finding is that employee attrition is driven by a combination of job satisfaction, compensation, work-life balance, and tenure. The most at-risk group identified by clustering is Cluster 2 — junior, low-earning employees — with a 27.8% attrition rate, nearly double the dataset average of 16.7%.

By combining Logistic Regression, DBSCAN clustering, and a LLaMA-powered prompt template, the system provides HR managers with actionable, personalized recommendations rather than just a binary prediction. This approach shows how multiple ML techniques can be integrated to address a real organizational challenge effectively.
