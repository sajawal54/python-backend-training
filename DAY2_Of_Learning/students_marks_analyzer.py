import csv
from pathlib import Path

file_path = Path(__file__).parent / "students.csv"

total_students = 0
total_marks = 0
highest_marks = 0
highest_student = ""

above_80 = []

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_students += 1

        marks = int(row["Marks"])

        total_marks += marks

        if marks > highest_marks:
            highest_marks = marks
            highest_student = row["Name"]

        if marks >= 80:
            above_80.append(row["Name"])

average = total_marks / total_students

print("\n========== STUDENT REPORT ==========\n")

print(f"Total Students : {total_students}")
print(f"Average Marks  : {average:.2f}")
print(f"Highest Marks  : {highest_student} ({highest_marks})")

print("\nStudents Above 80:")

for student in above_80:
    print(f"- {student}")

print("\n===================================")