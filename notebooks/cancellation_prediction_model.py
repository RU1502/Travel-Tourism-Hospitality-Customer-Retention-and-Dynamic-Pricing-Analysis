

##Import Libraries
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)


## Load Dataset
df = pd.read_csv("eda_hotel_bookings.csv")
df.head()


## Dataset Overview
print("Dataset Shape:", df.shape)
df.info()
df.head()
df["is_canceled"].value_counts()


## Check Cancellation Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="is_canceled")
plt.title("Cancellation Target Distribution")
plt.xlabel("Is Canceled")
plt.ylabel("Count")
plt.show()
cancel_rate = df["is_canceled"].mean() * 100
print(f"Cancellation Rate: {cancel_rate:.2f}%")


## 1. Select Features and Target
## Select Useful Columns
selected_features = [
    "hotel",
    "lead_time",
    "arrival_date_month",
    "arrival_date_week_number",
    "stays_in_weekend_nights",
    "stays_in_week_nights",
    "adults",
    "children",
    "babies",
    "meal",
    "country",
    "market_segment",
    "distribution_channel",
    "is_repeated_guest",
    "previous_cancellations",
    "previous_bookings_not_canceled",
    "reserved_room_type",
    "assigned_room_type",
    "booking_changes",
    "deposit_type",
    "agent",
    "company",
    "days_in_waiting_list",
    "customer_type",
    "adr",
    "required_car_parking_spaces",
    "total_of_special_requests",
    "total_stay",
    "total_guests",
    "lead_time_category",
    "season",
    "customer_segment"
]

target = "is_canceled"


## Keep Only Required Columns
model_df = df[selected_features + [target]].copy()

model_df.head()

## Check Missing Values
model_df.isnull().sum().sort_values(ascending=False)
model_df = model_df.dropna()

print("Shape after removing missing values:", model_df.shape)

## 2. Split Data
##  Define X and y
X = model_df[selected_features]
y = model_df[target]

print("Feature Shape:", X.shape)
print("Target Shape:", y.shape)


## Identify Numeric and Categorical Columns
numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_features = X.select_dtypes(include=["object", "category"]).columns.tolist()

print("Numeric Features:")
print(numeric_features)

print("\nCategorical Features:")
print(categorical_features)


## Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)


## 3. Preprocessing Pipeline
##  Create Preprocessor
numeric_transformer = Pipeline(steps=[
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)


## 4. Model 1: Logistic Regression
##Build Logistic Regression Model
logistic_model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])

## Train Logistic Regression
logistic_model.fit(X_train, y_train)
##Predict Using Logistic Regression
y_pred_lr = logistic_model.predict(X_test)
y_prob_lr = logistic_model.predict_proba(X_test)[:, 1]

## Evaluate Logistic Regression
print("Logistic Regression Results")
print("---------------------------")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print("Precision:", precision_score(y_test, y_pred_lr))
print("Recall:", recall_score(y_test, y_pred_lr))
print("F1 Score:", f1_score(y_test, y_pred_lr))
print("ROC-AUC:", roc_auc_score(y_test, y_prob_lr))

print("\nClassification Report:")
print(classification_report(y_test, y_pred_lr))


##Confusion Matrix — Logistic Regression
cm_lr = confusion_matrix(y_test, y_pred_lr)

plt.figure(figsize=(6, 4))
sns.heatmap(cm_lr, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


## 5. Model 2: Decision Tree
## Build Decision Tree Model
decision_tree_model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", DecisionTreeClassifier(
        max_depth=8,
        random_state=42
    ))
])


## Train Decision Tree
decision_tree_model.fit(X_train, y_train)
## Predict Using Decision Tree
y_pred_dt = decision_tree_model.predict(X_test)
y_prob_dt = decision_tree_model.predict_proba(X_test)[:, 1]

## Evaluate Decision Tree
print("Decision Tree Results")
print("---------------------")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print("Precision:", precision_score(y_test, y_pred_dt))
print("Recall:", recall_score(y_test, y_pred_dt))
print("F1 Score:", f1_score(y_test, y_pred_dt))
print("ROC-AUC:", roc_auc_score(y_test, y_prob_dt))

print("\nClassification Report:")
print(classification_report(y_test, y_pred_dt))


## Confusion Matrix — Decision Tree
cm_dt = confusion_matrix(y_test, y_pred_dt)

plt.figure(figsize=(6, 4))
sns.heatmap(cm_dt, annot=True, fmt="d", cmap="Greens")
plt.title("Confusion Matrix - Decision Tree")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


## 6. Model 3: Random Forest
## Build Random Forest Model
random_forest_model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=100,
        max_depth=12,
        random_state=42,
        n_jobs=-1
    ))
])


## Train Random Forest
random_forest_model.fit(X_train, y_train)
## Predict Using Random Forest
y_pred_rf = random_forest_model.predict(X_test)
y_prob_rf = random_forest_model.predict_proba(X_test)[:, 1]

## Evaluate Random Forest
print("Random Forest Results")
print("---------------------")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Precision:", precision_score(y_test, y_pred_rf))
print("Recall:", recall_score(y_test, y_pred_rf))
print("F1 Score:", f1_score(y_test, y_pred_rf))
print("ROC-AUC:", roc_auc_score(y_test, y_prob_rf))

print("\nClassification Report:")
print(classification_report(y_test, y_pred_rf))

## Confusion Matrix — Random Forest
cm_rf = confusion_matrix(y_test, y_pred_rf)

plt.figure(figsize=(6, 4))
sns.heatmap(cm_rf, annot=True, fmt="d", cmap="Oranges")
plt.title("Confusion Matrix - Random Forest")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

## 7. Compare All Models
## Create Model Comparison Table
model_results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "Accuracy": [
        accuracy_score(y_test, y_pred_lr),
        accuracy_score(y_test, y_pred_dt),
        accuracy_score(y_test, y_pred_rf)
    ],
    "Precision": [
        precision_score(y_test, y_pred_lr),
        precision_score(y_test, y_pred_dt),
        precision_score(y_test, y_pred_rf)
    ],
    "Recall": [
        recall_score(y_test, y_pred_lr),
        recall_score(y_test, y_pred_dt),
        recall_score(y_test, y_pred_rf)
    ],
    "F1 Score": [
        f1_score(y_test, y_pred_lr),
        f1_score(y_test, y_pred_dt),
        f1_score(y_test, y_pred_rf)
    ],
    "ROC-AUC": [
        roc_auc_score(y_test, y_prob_lr),
        roc_auc_score(y_test, y_prob_dt),
        roc_auc_score(y_test, y_prob_rf)
    ]
})

model_results

##  Plot Model Comparison
plt.figure(figsize=(10, 5))
sns.barplot(data=model_results, x="Model", y="ROC-AUC")
plt.title("Model Comparison Based on ROC-AUC")
plt.xlabel("Model")
plt.ylabel("ROC-AUC Score")
plt.ylim(0, 1)
plt.show()
plt.figure(figsize=(10, 5))
sns.barplot(data=model_results, x="Model", y="Recall")
plt.title("Model Comparison Based on Recall")
plt.xlabel("Model")
plt.ylabel("Recall Score")
plt.ylim(0, 1)
plt.show()

## 8. ROC Curve
## Plot ROC Curves
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prob_lr)
fpr_dt, tpr_dt, _ = roc_curve(y_test, y_prob_dt)
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)

plt.figure(figsize=(8, 6))

plt.plot(fpr_lr, tpr_lr, label=f"Logistic Regression AUC = {roc_auc_score(y_test, y_prob_lr):.3f}")
plt.plot(fpr_dt, tpr_dt, label=f"Decision Tree AUC = {roc_auc_score(y_test, y_prob_dt):.3f}")
plt.plot(fpr_rf, tpr_rf, label=f"Random Forest AUC = {roc_auc_score(y_test, y_prob_rf):.3f}")

plt.plot([0, 1], [0, 1], "k--")

plt.title("ROC Curve Comparison")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()

## 9. Feature Importance
## Feature Importance from Random Forest
rf_classifier = random_forest_model.named_steps["classifier"]
preprocessor_fitted = random_forest_model.named_steps["preprocessor"]

encoded_cat_features = preprocessor_fitted.named_transformers_["cat"]["onehot"].get_feature_names_out(categorical_features)
all_feature_names = np.concatenate([numeric_features, encoded_cat_features])

feature_importance = pd.DataFrame({
    "Feature": all_feature_names,
    "Importance": rf_classifier.feature_importances_
})

feature_importance = feature_importance.sort_values(by="Importance", ascending=False)

feature_importance.head(20)

## Plot Top 20 Important Features
top_features = feature_importance.head(20)

plt.figure(figsize=(10, 8))
sns.barplot(data=top_features, x="Importance", y="Feature")
plt.title("Top 20 Important Features for Cancellation Prediction")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()

## 10. Save Model Results
##  Save Model Comparison Results
model_results.to_csv("model_comparison_results.csv", index=False)
print("Model comparison results saved successfully.")


## Save Feature Importance Results
feature_importance.to_csv("feature_importance_results.csv", index=False)
print("Feature importance results saved successfully.")

## 11. Final Model Selection
##Choose Best Model
best_model = model_results.sort_values(by="ROC-AUC", ascending=False).iloc[0]

print("Best Model Based on ROC-AUC")
print("--------------------------")
print(best_model)


##  Business Interpretation
print("""
Business Interpretation:

The cancellation prediction model helps identify bookings that are likely to be canceled.

Important business uses:
1. High-risk bookings can be targeted with reminder emails or confirmation calls.
2. Customers with long lead times can be given retention offers.
3. Revenue managers can adjust room availability and pricing based on cancellation risk.
4. Marketing teams can focus retention campaigns on high-risk customer segments.

The final model should be selected based on ROC-AUC, Recall, and F1 Score.
Recall is important because the business wants to correctly identify as many likely cancellations as possible.
""")
