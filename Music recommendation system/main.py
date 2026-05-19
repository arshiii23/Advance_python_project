import pandas as pd
import os

# ---------------------------------
# GET CURRENT PROJECT FOLDER
# ---------------------------------

base_dir = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------
# DATASET PATH
# ---------------------------------

dataset_path = os.path.join(base_dir, "songs.csv")

# ---------------------------------
# LOAD DATASET
# ---------------------------------

try:
    df = pd.read_csv(dataset_path)

    print("Dataset loaded successfully!\n")

except FileNotFoundError:
    print("Error: songs.csv file not found")
    exit()

except Exception as e:
    print("Error loading dataset:")
    print(e)
    exit()

# ---------------------------------
# SHOW AVAILABLE GENRES
# ---------------------------------

print("Available Genres:")

genres = df["Genre"].unique()

for genre in genres:
    print("-", genre)

# USER INPUT

user_genre = input("\nEnter your favorite genre: ").strip().lower()

# FILTER SONGS

recommended_songs = df[
    df["Genre"].str.lower() == user_genre
]

# DISPLAY RESULTS

print("\n===== RECOMMENDED SONGS =====")

if not recommended_songs.empty:

    for index, row in recommended_songs.iterrows():

        print(f"\n🎵 Song: {row['Song']}")
        print(f"🎤 Artist: {row['Artist']}")

else:
    print("No songs found for this genre")