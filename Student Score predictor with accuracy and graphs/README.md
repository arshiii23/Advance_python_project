🧠 Student Score Predictor (Machine Learning Project)

🚀 Overview

The Student Score Predictor is a beginner-friendly Machine Learning project built using Python and Scikit-learn. The application predicts student marks based on the number of study hours using a Linear Regression model.

The project also visualizes the relationship between study hours and marks using a graph and automatically saves the chart as a PNG image.

This project demonstrates practical concepts of:

- Machine Learning
- Linear Regression
- Data Visualization
- Model Training & Prediction
- Python Data Analysis

---

🧠 Features

- Predicts student marks based on study hours
- Uses Linear Regression algorithm
- Displays model accuracy
- Generates and saves graph automatically
- Beginner-friendly ML implementation

---

🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

---

⚙️ Installation & Setup

1. Clone the repository or download files

---

2. Install required libraries

pip install pandas matplotlib scikit-learn

---

3. Run the project

python main.py

---

💻 Complete Code ("main.py")

import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 30, 40, 50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Hours"]]
y = df["Marks"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()

model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)

print("Model Accuracy:", round(score * 100, 2), "%")

# Prediction
prediction = model.predict([[6]])

print("Predicted Marks for 6 hours study:")
print(round(prediction[0], 2))

# Create graph
plt.figure(figsize=(8, 5))

plt.scatter(df["Hours"], df["Marks"])

plt.plot(df["Hours"], model.predict(X))

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Save graph
base_dir = os.path.dirname(os.path.abspath(__file__))

graph_path = os.path.join(base_dir, "ml_graph.png")

plt.savefig(graph_path)

print("\nGraph saved successfully!")

# Show graph
plt.show()

---

▶️ How It Works

1. Creates dataset of study hours and marks
2. Splits dataset into training and testing data
3. Trains Linear Regression model
4. Predicts marks based on study hours
5. Calculates model accuracy
6. Generates and saves visualization graph

---

💻 Example Output

Model Accuracy: 100.0 %

Predicted Marks for 6 hours study:
70.0

Graph saved successfully!

---

📈 Generated Graph

ml_graph.png

The graph is automatically saved inside the project folder.

---

🎯 Skills Demonstrated

- Machine Learning Basics
- Linear Regression
- Data Visualization
- Model Training & Prediction
- Python Data Analysis
- Working with Scikit-learn

---

🔮 Future Improvements

- Use real-world student datasets
- Add multiple input features
- Create Streamlit web application
- Add user input GUI
- Deploy ML model online

---

👨‍💻 Author

Arsheen Shaikh

---
