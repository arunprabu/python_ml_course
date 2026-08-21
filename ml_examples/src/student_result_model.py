import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

"""
Logistic Regression is a machine-learning model that looks at examples 
and calculates the probability of something being one of two choices, 
such as YES/NO, PASS/FAIL, or SPAM/NOT SPAM.

The important thing to remember:
Linear Regression → predicts a number 🔢
Logistic Regression → predicts a probability/class 🎯
"""


# 1. DATA — hours studied and whether the student passed
# 0 = Fail, 1 = Pass
df = pd.DataFrame(
    {
        "hours": [
            1,
            1.5,
            2,
            2.5,
            3,
            3.5,
            4,
            4.5,
            5,
            5.5,
            6,
            6.5,
            7,
            7.5,
            8,
            8.5,
            9,
            9.5,
            10,
            10.5,
        ],
        "passed": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    }
)


# # 2. FEATURES (X) and TARGET (y)
# # X = input, y = what we want to predict
X = df[["hours"]]  # features to be in 2D
y = df["passed"]  # target to be in 1D

# # 3. Split into train and test
# # stratify is the following
# # When you split the students into two groups, keep the same Pass/Fail ratio in both groups.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=56, stratify=y
)

# # 4. MODEL — train it
model = LogisticRegression()
model.fit(X_train, y_train)

# # 5. EVALUATE
print("Accuracy:", model.score(X_test, y_test))

# # 6. PREDICT for new students
# print("Prediction (1 = pass, 0 = fail):\n")
new_student = pd.DataFrame({"hours": [5.9]})
print("Prediction for 5.9 hours:", model.predict(new_student)[0])

lazy_student = pd.DataFrame({"hours": [2.0]})
print("Prediction for 2 hours:", model.predict(lazy_student)[0])

# another_student = pd.DataFrame({"hours": [9.2]})
# print("Prediction for 9.2 hours:", model.predict(another_student)[0])
