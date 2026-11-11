# Gaussian Naive Bayes on Iris Dataset - Complete Explanation

# Aim

To classify Iris flowers into one of three species using the **Gaussian Naive Bayes** machine learning algorithm.

The three flower classes are:

- Setosa
- Versicolor
- Virginica

The algorithm predicts the flower type based on four flower measurements.

---

# Step 1: Import Libraries

```python
from sklearn.datasets import load_iris
```

## Why?

This imports the built-in Iris dataset from Scikit-learn.

## What is the Iris Dataset?

The Iris dataset is one of the most popular datasets in Machine Learning.

It contains:

- 150 flower samples
- 3 flower species
- 4 features for each flower

The four features are:

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

---

```python
from sklearn.model_selection import train_test_split
```

## Why?

A Machine Learning model needs two types of data:

- Training Data
- Testing Data

The `train_test_split()` function divides the dataset into these two parts.

---

```python
from sklearn.naive_bayes import GaussianNB
```

## Why?

This imports the **Gaussian Naive Bayes** classifier.

We use Gaussian Naive Bayes because:

- It is simple.
- It is very fast.
- It works well with continuous numerical data.
- It is suitable for the Iris dataset.

---

```python
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
```

## Why?

These functions evaluate the model's performance.

They calculate:

- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-Score

---

# Step 2: Load the Dataset

```python
iris = load_iris()
```

## Why?

This loads the complete Iris dataset into memory.

Think of it like opening an Excel file.

The variable `iris` contains:

- Data
- Target labels
- Feature names
- Target names

---

# Step 3: Store the Features

```python
X = iris.data
```

## Why?

Machine Learning models learn using input features.

`X` stores the four measurements of each flower.

Example:

```
[5.1, 3.5, 1.4, 0.2]
```

Meaning:

```
Sepal Length = 5.1

Sepal Width = 3.5

Petal Length = 1.4

Petal Width = 0.2
```

There are 150 such rows.

---

# Step 4: Store the Target

```python
y = iris.target
```

## Why?

`y` stores the correct class of each flower.

```
0 = Setosa

1 = Versicolor

2 = Virginica
```

Example:

```
Flower Measurements

↓

5.1
3.5
1.4
0.2

↓

Target

↓

0

↓

Setosa
```

The model learns the relationship between features and the target class.

---

# Step 5: Split the Dataset

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)
```

## Why?

The model should first learn and then be tested.

Just like:

```
Student

↓

Studies

↓

Writes Exam
```

Machine Learning:

```
Training Data

↓

Model Learns

↓

Testing Data

↓

Model is Tested
```

---

## test_size = 0.3

This means:

30% of the dataset is reserved for testing.

Since the Iris dataset has 150 samples:

```
70%

↓

105 Flowers

↓

Training
```

```
30%

↓

45 Flowers

↓

Testing
```

---

## random_state = 42

This ensures that every time the program runs, the same training/testing split is used.

Without it, the split changes every time.

---

# Step 6: Create the Model

```python
model = GaussianNB()
```

## Why?

This creates an empty Gaussian Naive Bayes model.

At this stage, the model has not learned anything.

Think of it as a new student before studying.

---

# Step 7: Train the Model

```python
model.fit(X_train, y_train)
```

## Why?

This is the learning phase.

The model studies all training examples.

It starts learning patterns like:

```
Small Petals

↓

Mostly Setosa
```

```
Medium Petals

↓

Mostly Versicolor
```

```
Large Petals

↓

Mostly Virginica
```

After this step, the model becomes trained.

---

# Step 8: Predict the Test Data

```python
y_prediction = model.predict(X_test)
```

## Why?

Now the model predicts flowers it has never seen before.

Example:

```
Flower Measurements

↓

5.8
2.8
5.1
2.4

↓

Prediction

↓

Virginica
```

---

# Step 9: Print Predicted Values

```python
print(y_prediction)
```

Example:

```
[1 0 2 1 2]
```

These are the predicted classes.

---

# Step 10: Print Actual Values

```python
print(y_test)
```

Example:

```
[1 0 2 1 2]
```

These are the correct answers.

Now the model's predictions are compared with the actual values.

---

# Step 11: Calculate Accuracy

```python
accuracy = accuracy_score(y_test, y_prediction)
```

## Formula

Accuracy = Correct Predictions / Total Predictions

Example:

```
Correct Predictions = 44

Total Predictions = 45

Accuracy = 44 / 45

= 97.8%
```

Higher accuracy indicates a better model.

---

# Step 12: Confusion Matrix

```python
cm = confusion_matrix(y_test, y_prediction)
```

Example:

```
[[19 0 0]
 [0 13 0]
 [0 1 12]]
```

Meaning:

```
19 Setosa classified correctly.

13 Versicolor classified correctly.

12 Virginica classified correctly.

1 Virginica classified as Versicolor.
```

Diagonal values represent correct predictions.

Off-diagonal values represent incorrect predictions.

---

# Step 13: Classification Report

```python
classification_report(y_test, y_prediction)
```

This prints:

- Precision
- Recall
- F1-Score
- Support

---

## Precision

Out of everything predicted as a particular class,

how many predictions were actually correct?

Formula:

Precision = TP / (TP + FP)

---

## Recall

Out of all actual samples belonging to a class,

how many did the model correctly identify?

Formula:

Recall = TP / (TP + FN)

---

## F1-Score

F1-Score combines Precision and Recall.

Formula:

F1 = 2 × Precision × Recall / (Precision + Recall)

---

## Support

Support indicates the number of actual samples available for each class.

Example:

```
Setosa

↓

19 Flowers
```

---

# Why Gaussian Naive Bayes?

Gaussian Naive Bayes assumes:

- Every feature follows a Gaussian (Normal) Distribution.
- Every feature is independent of the others (Naive Assumption).

The algorithm calculates the probability of a flower belonging to each class.

The flower is assigned to the class with the highest probability.

---

# Complete Program Flow

```
Load Iris Dataset
        │
        ▼
Separate Features (X) and Target (y)
        │
        ▼
Split Dataset into Training and Testing
        │
        ▼
Create Gaussian Naive Bayes Model
        │
        ▼
Train the Model (fit)
        │
        ▼
Predict Test Data (predict)
        │
        ▼
Compare Predictions with Actual Values
        │
        ▼
Calculate Accuracy
        │
        ▼
Generate Confusion Matrix
        │
        ▼
Generate Classification Report
```

# Summary

This program demonstrates a complete Machine Learning classification workflow:

1. Import the required libraries.
2. Load the Iris dataset.
3. Separate features and target labels.
4. Split the dataset into training and testing sets.
5. Create a Gaussian Naive Bayes model.
6. Train the model using the training data.
7. Predict the classes of unseen test data.
8. Evaluate the model using Accuracy, Confusion Matrix, and Classification Report.
9. Use the results to determine how well the classifier performs.