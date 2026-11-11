# Import the Iris dataset
from sklearn.datasets import load_iris

# Import function to split dataset into training and testing sets
from sklearn.model_selection import train_test_split

# Import Gaussian Naive Bayes classifier
from sklearn.naive_bayes import GaussianNB

# Import functions to evaluate the model
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import numpy as np

# Load the Iris dataset
iris = load_iris()

# Store the input features (sepal length, sepal width, petal length, petal width)
X = iris.data

# Store the target labels (flower classes)
y = iris.target

# Split the dataset into training data (70%) and testing data (30%)
# random_state=42 ensures the same split every time
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

# Create the Gaussian Naive Bayes model
model = GaussianNB()

# Train the model using the training data
model.fit(X_train, y_train)

# Predict the class labels for the test data
y_prediction = model.predict(X_test)

# Print the predicted class labels
print("Predicted Values:")
print(y_prediction)

# Print the actual class labels
print("\nActual Values:")
print(y_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_prediction)

# Display the accuracy score
print("\nAccuracy Score:", accuracy)

# Generate the confusion matrix
cm = confusion_matrix(y_test, y_prediction)

# Display the confusion matrix
print("\nConfusion Matrix:")
print(cm)

# Generate and display the classification report
# It includes precision, recall, F1-score, and support
print("\nClassification Report:")
print(classification_report(y_test, y_prediction))

# End of program


#

# Sample 1 - Setosa
sample = np.array([[5.1, 3.5, 1.4, 0.2]])
pred = model.predict(sample)
print("Sample 1 Prediction:", pred)
print("Flower Name:", iris.target_names[pred[0]])

# Sample 2 - Versicolor
sample = np.array([[6.0, 2.9, 4.5, 1.5]])
pred = model.predict(sample)
print("Sample 2 Prediction:", pred)
print("Flower Name:", iris.target_names[pred[0]])

# Sample 3 - Virginica
sample = np.array([[6.9, 3.1, 5.4, 2.1]])
pred = model.predict(sample)
print("Sample 3 Prediction:", pred)
print("Flower Name:", iris.target_names[pred[0]])


# Create multiple flower samples (2D array)
sample = np.array([
    [5.1, 3.5, 1.4, 0.2],  # Setosa
    [6.0, 2.9, 4.5, 1.5],  # Versicolor
    [6.9, 3.1, 5.4, 2.1]  # Virginica
   
])

# Predict the classes
pred = model.predict(sample)

# Print predicted class numbers
print("Predicted Classes:", pred)

#pinrt all traget names
print(iris.target_names)

# Print predicted flower names
for i in range(len(pred)):
    print(f"Sample {i+1}: {iris.target_names[pred[i]]}")


   