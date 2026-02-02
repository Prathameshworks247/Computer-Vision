import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Load Data (The "Grid of Numbers")
digits = load_digits()

# Set the target: Classify '0' vs 'Not 0'
# We change labels to 1 (is zero) and -1 (is not zero) for AdaBoost logic
X = digits.data
y = list(1 if target == 0 else -1 for target in digits.target)

# Split into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Define the "Weak Learner"
# A Decision Stump is a Tree with max_depth=1. 
# It makes a decision based on a SINGLE pixel's value (just like a single Haar feature).
weak_learner = DecisionTreeClassifier(max_depth=1)

# 3. Train the AdaBoost Classifier
# n_estimators=50 means we will select the 50 best "stumps" to form our committee.
clf = AdaBoostClassifier(
    estimator=weak_learner,
    n_estimators=50,
    random_state=42
)

clf.fit(X_train, y_train)

# 4. Evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy with 50 Weak Learners: {accuracy * 100:.2f}%")

# --- Deep Dive: Feature Importance ---
# We can see which pixels (features) AdaBoost thought were most important for identifying a '0'.
import numpy as np

# Feature importances tells us which pixels were chosen by the algorithm
importances = clf.feature_importances_
importance_image = importances.reshape(8, 8)

plt.figure(figsize=(8, 4))

# Plot the "Average Zero" for reference
plt.subplot(1, 2, 1)
plt.title("Average '0' Image")
plt.imshow(np.mean(X[np.array(y) == 1], axis=0).reshape(8, 8), cmap='gray')
plt.axis('off')

# Plot the "AdaBoost Selected Pixels"
plt.subplot(1, 2, 2)
plt.title("Key Pixels (AdaBoost Importance)")
plt.imshow(importance_image, cmap='hot')
plt.axis('off')

plt.show()