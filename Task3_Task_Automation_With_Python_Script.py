# TASK 3: Task Automation with Python Scripts
    
# Goal: Automate a small, real-life repetitive task.
# Pick One of These Ideas:
# ● Move all .jpg files from a folder to a new folder.
# ● Extract all email addresses from a .txt file and save them to another file.
# ● Scrape the title of a fixed webpage and save it.
# Key Concepts Used: os, shutil, re, requests, file handling.

# Task 1
# ● Move all .jpg files from a folder to a new folder.

import os
import shutil

source = "C:/Program_Files/VS Code/Python Internship/Original_file"
destination = "C:/Program_Files/VS Code/Python Internship/Duplicate_file" 

os.makedirs(destination, exist_ok=True)           # Create folder if needed

with open("moved_files.txt", "w") as log:
    for file in os.listdir(source):
        if file.lower().endswith(".jpg"):
            shutil.move(f"{source}/{file}", f"{destination}/{file}")
            log.write(file + "\n")
            print(f"Moved: {file}")

print("✅ All .jpg files moved and recorded.")


# Task 2
# ● Extract all email addresses from a .txt file and save them to another file.

import re

input_file = "input_file.txt"       
output_file = "output_file.txt"      

# Read the input file content
with open(input_file, "r") as file:
    text = file.read()

# 🔄 Simpler regex to find emails
emails = re.findall(r"\S+@\S+", text)

# Write found emails to output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print(f"✅ Found {len(emails)} email(s). Saved to '{output_file}'.")
