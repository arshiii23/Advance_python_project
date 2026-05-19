import pandas as pd
import os

# -----------------------------
# FILE PATHS
# -----------------------------

# Get current folder location
base_dir = os.path.dirname(os.path.abspath(__file__))

# Create full paths
jobs_file = os.path.join(base_dir, "jobs.csv")
resume_file = os.path.join(base_dir, "resume.txt")

# -----------------------------
# LOAD JOB DATASET
# -----------------------------

jobs = pd.read_csv(jobs_file)

# -----------------------------
# READ RESUME TEXT
# -----------------------------

with open(resume_file, "r") as file:
    resume_text = file.read().lower()

# -----------------------------
# MATCH SKILLS
# -----------------------------

print("\n===== MATCHING JOBS =====")

for index, row in jobs.iterrows():

    # Convert skills into list
    skills = row["Skills"].lower().split(",")

    # Check matching skills
    matched_skills = []

    for skill in skills:
        if skill.strip() in resume_text:
            matched_skills.append(skill)

    # Display results
    print("\nJob Role:", row["Job Role"])

    if matched_skills:
        print("Matched Skills:", matched_skills)
    else:
        print("No matching skills found")