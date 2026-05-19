import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# CREATE DATASET

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 30, 40, 50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

# FEATURES & TARGET

X = df[["Hours"]]
y = df["Marks"]

# SPLIT DATA

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# TRAIN MODEL

model = LinearRegression()

model.fit(X_train, y_train)

# MODEL ACCURACY

score = model.score(X_test, y_test)

print("Model Accuracy:", round(score * 100, 2), "%")

# PREDICTION

prediction = model.predict([[6]])

print("Predicted Marks for 6 hours study:")
print(round(prediction[0], 2))

# CREATE GRAPH

plt.figure(figsize=(8, 5))

# Scatter points
plt.scatter(df["Hours"], df["Marks"])

# Regression line
plt.plot(df["Hours"], model.predict(X))

# Labels
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# SAVE GRAPH INSIDE PROJECT FOLDER

base_dir = os.path.dirname(os.path.abspath(__file__))

graph_path = os.path.join(base_dir, "ml_graph.png")

plt.savefig(graph_path)

print("\nGraph saved successfully!")
print("Location:", graph_path)

# SHOW GRAPH
plt.show()