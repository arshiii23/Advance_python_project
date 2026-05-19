🎬 Netflix Data Analysis Project (Python Data Science Project)

🚀 Overview

The Netflix Data Analysis Project is a Python-based data analysis project that explores and visualizes Netflix content data using Pandas and Matplotlib.

This project analyzes the distribution of Movies and TV Shows available on Netflix and generates visual insights using graphs.

It demonstrates practical skills in:

- Data analysis
- Data visualization
- CSV dataset handling
- Python scripting

---

🧠 Features

- Loads real-world Netflix dataset
- Analyzes Movies vs TV Shows
- Generates bar chart visualization
- Saves graph automatically as PNG
- Beginner-friendly data science project

---

🛠️ Technologies Used

- Python
- Pandas
- Matplotlib

---

📁 Project Structure

netflix-analysis/
│── main.py
│── netflix_titles.csv
│── netflix_chart.png
│── README.md

---

📊 Dataset

Dataset downloaded from Kaggle:

"Netflix Dataset on Kaggle" (https://www.kaggle.com/datasets/shivamb/netflix-shows?utm_source=chatgpt.com)

Dataset file:

netflix_titles.csv

---

⚙️ Installation & Setup

1. Clone the repository or download the files

2. Install required libraries:

pip install pandas matplotlib

3. Place "netflix_titles.csv" inside the project folder

4. Run the project:

python main.py

---

💻 Example Code

import pandas as pd
import matplotlib.pyplot as plt
import os

# Get current project folder
base_dir = os.path.dirname(os.path.abspath(__file__))

# Dataset path
dataset_path = os.path.join(base_dir, "netflix_titles.csv")

# Load dataset
df = pd.read_csv(dataset_path)

# Count content types
content_counts = df["type"].value_counts()

# Create graph
content_counts.plot(kind="bar")

plt.title("Netflix Content Type")
plt.xlabel("Type")
plt.ylabel("Count")

# Save graph
graph_path = os.path.join(base_dir, "netflix_chart.png")

plt.savefig(graph_path)

plt.show()

---

▶️ How It Works

1. Loads Netflix dataset using Pandas
2. Counts number of Movies and TV Shows
3. Creates visualization using Matplotlib
4. Saves graph automatically as PNG image
5. Displays chart on screen

---

🎯 Skills Demonstrated

- Data Cleaning & Analysis
- Data Visualization
- CSV File Handling
- Python Automation
- Working with Real-world Datasets

---

🔮 Future Improvements

- Analyze release years
- Find top Netflix genres
- Country-wise content analysis
- Create interactive dashboard using Streamlit
- Add multiple graph visualizations

---

👨‍💻 Author

Arsheen Shaikh

---