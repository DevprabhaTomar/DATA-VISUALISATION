import pandas as pd

# Load CSV file
df = pd.read_csv("attendance.csv")

# Show data (for debugging)
print("All Records:\n", df)

# Filter students below 75%
low_attendance = df[df["Attendance"] < 75]

print("\nStudents below 75% attendance:\n")
print(low_attendance)