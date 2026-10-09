



#Save the following program as student_performance.py.



import pandas as pd
import numpy as np

# Configuration
CSV_FILE = "students.csv"
PASS_PERCENTAGE = 40
MAX_MARKS_PER_SUBJECT = 100

# Load student data
try:
    df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    print(f"Error: {CSV_FILE} not found.")
    raise SystemExit(1)

# Identify subject columns
required_columns = ["RollNo", "Name"]
if not all(col in df.columns for col in required_columns):
    print("Error: CSV must contain RollNo and Name columns.")
    raise SystemExit(1)

subject_columns = [
    col for col in df.columns
    if col not in required_columns
]

if not subject_columns:
    print("Error: No subject columns found.")
    raise SystemExit(1)

# Validate marks
df[subject_columns] = df[subject_columns].apply(
    pd.to_numeric, errors="coerce"
)

if df.empty:
    print("Error: CSV contains no student records.")
    raise SystemExit(1)

if df[subject_columns].isna().any().any():
    print("Error: Missing or non-numeric marks found.")
    raise SystemExit(1)

if (
    (df[subject_columns] < 0).any().any()
    or (df[subject_columns] > MAX_MARKS_PER_SUBJECT).any().any()
):
    print("Error: Marks must be between 0 and 100.")
    raise SystemExit(1)

# Calculate total marks and percentage
total_subjects = len(subject_columns)
max_total = total_subjects * MAX_MARKS_PER_SUBJECT

df["Total"] = df[subject_columns].sum(axis=1)
df["Percentage"] = (
    df["Total"] / max_total
) * 100

# Calculate grades
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= PASS_PERCENTAGE:
        return "E"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(calculate_grade)

# Calculate subject-wise statistics using NumPy
subject_stats = pd.DataFrame({
    "Average": df[subject_columns].mean(),
    "Highest": df[subject_columns].max(),
    "Lowest": df[subject_columns].min(),
    "Standard Deviation": df[subject_columns].std(ddof=0)
})

# Class statistics
class_average = df["Percentage"].mean()

# Identify topper(s), including ties
highest_percentage = df["Percentage"].max()
toppers = df[
    np.isclose(df["Percentage"], highest_percentage)
]

# Identify students below pass percentage
failed_students = df[
    df["Percentage"] < PASS_PERCENTAGE
]

# Also identify students who failed any individual subject
failed_subject_students = df[
    (df[subject_columns] < PASS_PERCENTAGE).any(axis=1)
]

# Display results
print("\n========== STUDENT PERFORMANCE REPORT ==========")

print("\n1. Individual Student Results")
print(
    df[["RollNo", "Name", "Total", "Percentage", "Grade"]]
    .to_string(index=False, formatters={
        "Percentage": "{:.2f}%".format
    })
)

print("\n2. Class Statistics")
print(f"Total Students       : {len(df)}")
print(f"Number of Subjects   : {total_subjects}")
print(f"Maximum Total Marks  : {max_total}")
print(f"Class Average        : {class_average:.2f}%")

print("\n3. Class Topper(s)")
for _, student in toppers.iterrows():
    print(
        f"{student['Name']} - "
        f"{student['Percentage']:.2f}% "
        f"(Total: {student['Total']})"
    )

print("\n4. Subject-wise Statistics")
print(subject_stats.round(2).to_string())

print("\n5. Students Below Pass Percentage")
if failed_students.empty:
    print("No students are below the pass percentage.")
else:
    print(
        failed_students[
            ["RollNo", "Name", "Percentage", "Grade"]
        ].to_string(index=False)
    )

print("\n6. Students Failing in Any Subject")
if failed_subject_students.empty:
    print("No students failed any subject.")
else:
    for _, student in failed_subject_students.iterrows():
        failed_subjects = [
            subject for subject in subject_columns
            if student[subject] < PASS_PERCENTAGE
        ]
        print(
            f"{student['Name']}: "
            f"{', '.join(failed_subjects)}"
        )

# Save the reports
df.to_csv("student_results.csv", index=False)
subject_stats.round(2).to_csv("subject_statistics.csv")

failed_students.to_csv("students_below_pass.csv", index=False)

print("\nReports saved successfully:")
print("- student_results.csv")
print("- subject_statistics.csv")
print("- students_below_pass.csv")
