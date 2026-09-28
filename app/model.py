import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample Training Data (Experience vs Role Category)
X = np.array([[1, 20], [2, 30], [3, 50], [4, 65], [5, 80]])
y = np.array([0, 0, 1, 1, 1])  # 0 = Junior, 1 = Senior

model = LogisticRegression()
model.fit(X, y)

def predict_seniority(years_exp: float, skill_score: float) -> str:
    prediction = model.predict([[years_exp, skill_score]])[0]
    return "Senior Role" if prediction == 1 else "Junior Role"