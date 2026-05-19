🎵 Music Recommendation System (Python Recommendation Project)

🚀 Overview

The Music Recommendation System is a Python-based project that recommends songs based on the user’s favorite music genre.

The project reads song data from a CSV dataset, filters songs according to the selected genre, and displays recommended tracks along with artist names.

This project demonstrates practical concepts of:

- Data filtering
- CSV dataset handling
- Recommendation system basics
- User interaction
- Python automation

---

🧠 Features

- Reads song dataset from CSV
- Recommends songs based on genre
- Displays song name and artist
- Handles invalid genre input
- Beginner-friendly recommendation system

---

🛠️ Technologies Used

- Python
- Pandas
---

📊 Dataset Example ("songs.csv")

Song,Genre,Artist
Believer,Rock,Imagine Dragons
Thunder,Rock,Imagine Dragons
Shape of You,Pop,Ed Sheeran
Perfect,Pop,Ed Sheeran
Blinding Lights,Pop,The Weeknd
Lose Yourself,Rap,Eminem

---

⚙️ Installation & Setup

1. Clone the repository or download files

---

2. Install required library

pip install pandas

---

3. Run the project

python main.py

---

💻 Complete Code ("main.py")

import pandas as pd
import os

# Get current project folder
base_dir = os.path.dirname(os.path.abspath(__file__))

# Dataset path
dataset_path = os.path.join(base_dir, "songs.csv")

# Load dataset
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

# Show available genres
print("Available Genres:")

genres = df["Genre"].unique()

for genre in genres:
    print("-", genre)

# User input
user_genre = input("\nEnter your favorite genre: ").strip().lower()

# Filter songs
recommended_songs = df[
    df["Genre"].str.lower() == user_genre
]

# Display recommendations
print("\n===== RECOMMENDED SONGS =====")

if not recommended_songs.empty:

    for index, row in recommended_songs.iterrows():

        print(f"\n🎵 Song: {row['Song']}")
        print(f"🎤 Artist: {row['Artist']}")

else:
    print("No songs found for this genre")

---

▶️ How It Works

1. Loads song dataset using Pandas
2. Displays available music genres
3. User enters favorite genre
4. Program filters matching songs
5. Recommended songs and artists are displayed

---

💻 Example Output

Dataset loaded successfully!

Available Genres:
- Rock
- Pop
- Rap

Enter your favorite genre: pop

===== RECOMMENDED SONGS =====

🎵 Song: Shape of You
🎤 Artist: Ed Sheeran

🎵 Song: Perfect
🎤 Artist: Ed Sheeran

🎵 Song: Blinding Lights
🎤 Artist: The Weeknd

---

🎯 Skills Demonstrated

- Data Filtering
- CSV Dataset Handling
- Recommendation System Basics
- User Input Handling
- Python Automation

---

🔮 Future Improvements

- Add mood-based song recommendations
- Add artist search functionality
- Use machine learning recommendation algorithms
- Build GUI using Tkinter
- Create web app using Streamlit
- Integrate Spotify API

---

👨‍💻 Author

Arsheen Shaikh

---

