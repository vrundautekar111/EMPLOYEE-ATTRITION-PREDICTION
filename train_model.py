import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


data = pd.read_csv("employee_attrition.csv")

print("Dataset loaded successfully!")
print(data.head())


data["OverTime"] = data["OverTime"].map({
    "Yes": 1,
    "No": 0
})

data["Attrition"] = data["Attrition"].map({
    "Yes": 1,
    "No": 0
})


X = data.drop("Attrition", axis=1)

y = data["Attrition"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    max_depth=10
)


model.fit(X_train, y_train)

print("Model training completed!")


y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


joblib.dump(model, "attrition_model.pkl")

print("\nModel saved as attrition_model.pkl")