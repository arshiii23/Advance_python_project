🤖 AI Resume Screening System (Python NLP Project)

🚀 Overview

The AI Resume Screening System is a Python-based project that analyzes resumes and matches candidate skills with job requirements using Natural Language Processing (NLP) concepts.

The project reads resume text, compares it with required job skills, and identifies the most suitable job roles based on matching skills.

This project demonstrates practical use of:

- File handling
- Data processing
- NLP basics
- Skill matching automation

---

🧠 Features

- Reads resume text automatically
- Loads job role dataset from CSV
- Matches candidate skills with job requirements
- Displays matching job roles and skills
- Beginner-friendly AI/NLP project

---

🛠️ Technologies Used

- Python
- Pandas
- File Handling
- NLP Concepts

---

📁 Project Structure

ai-resume-screening/
│── main.py
│── jobs.csv
│── resume.txt
│── README.md
│── screenshot.png

---

📊 Dataset Example ("jobs.csv")

Job Role,Skills
Data Scientist,"python,machine learning,pandas"
Web Developer,"html,css,javascript"
Data Analyst,"excel,pandas,sql"

---

📄 Resume Example ("resume.txt")

I know python, pandas, machine learning and sql.

---

⚙️ Installation & Setup

1. Clone the repository or download the files

2. Install required library:

pip install pandas

3. Run the project:

python main.py

---

▶️ How It Works

1. Loads job roles and required skills from "jobs.csv"
2. Reads resume text from "resume.txt"
3. Converts text into lowercase for easy matching
4. Compares resume skills with job requirements
5. Displays matching job roles and matched skills

---

💻 Example Code

import pandas as pd
import os

# Get project folder
base_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
jobs_file = os.path.join(base_dir, "jobs.csv")
resume_file = os.path.join(base_dir, "resume.txt")

# Load dataset
jobs = pd.read_csv(jobs_file)

# Read resume
with open(resume_file, "r") as file:
    resume_text = file.read().lower()

print("\n===== MATCHING JOBS =====")

for index, row in jobs.iterrows():

    skills = row["Skills"].lower().split(",")

    matched_skills = []

    for skill in skills:
        if skill.strip() in resume_text:
            matched_skills.append(skill)

    print("\nJob Role:", row["Job Role"])

    if matched_skills:
        print("Matched Skills:", matched_skills)
    else:
        print("No matching skills found")

---

💻 Example Output

===== MATCHING JOBS =====

Job Role: Data Scientist
Matched Skills: ['python', 'machine learning', 'pandas']

Job Role: Web Developer
No matching skills found

Job Role: Data Analyst
Matched Skills: ['pandas', 'sql']

---

🎯 Skills Demonstrated

- Data Processing
- File Handling
- CSV Handling
- NLP Basics
- Python Automation
- Skill Matching Logic

---

🔮 Future Improvements

- Add PDF resume support
- Calculate matching percentage
- Add GUI using Tkinter or Streamlit
- Use real-world job datasets
- Deploy as a web application

---

👨‍💻 Author

Arsheen Shaikh

---