import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------
# GET CURRENT PROJECT FOLDER
# ---------------------------------

base_dir = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------
# DATASET PATH
# ---------------------------------

dataset_path = os.path.join(base_dir, "netflix_titles.csv")

# ---------------------------------
# LOAD DATASET
# ---------------------------------

try:
    df = pd.read_csv(dataset_path)

    print("Dataset loaded successfully!\n")

except FileNotFoundError:
    print("Error: netflix_titles.csv file not found")
    exit()

except Exception as e:
    print("Error loading dataset:")
    print(e)
    exit()

# ---------------------------------
# SHOW FIRST 5 ROWS
# ---------------------------------

print(df.head())

# ---------------------------------
# COUNT MOVIES VS TV SHOWS
# ---------------------------------

content_counts = df["type"].value_counts()

print("\nContent Type Counts:")
print(content_counts)

# ---------------------------------
# CREATE GRAPH
# ---------------------------------

plt.figure(figsize=(6, 4))

content_counts.plot(kind="bar")

plt.title("Netflix Content Type")
plt.xlabel("Type")
plt.ylabel("Count")

# ---------------------------------
# SAVE GRAPH
# ---------------------------------

graph_path = os.path.join(base_dir, "netflix_chart.png")

plt.savefig(graph_path)

print("\nGraph saved successfully!")

# ---------------------------------
# SHOW GRAPH
# ---------------------------------

plt.show()