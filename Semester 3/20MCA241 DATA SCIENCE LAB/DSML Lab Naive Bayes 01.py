# Import the Breast Cancer dataset
from sklearn.datasets import load_breast_cancer

# Import required libraries
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
cancer = load_breast_cancer()

# Features and target
X = cancer.data
y = cancer.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = GaussianNB()

# Train the model
model.fit(X_train, y_train)

# Predict the test data
y_pred = model.predict(X_test)

print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))



sample = X_test[0].reshape(1, -1)
prediction=model.predict(sample)
print("Predicted class : ",prediction)
print(cancer.target_names[prediction])

sample = X_test[1].reshape(1, -1)
prediction=model.predict(sample)
print("Predicted class : ",prediction)
print(cancer.target_names[prediction])