import pandas as pd

students = []

def add_student():
    name = input("Name: ")
    marks = int(input("Marks: "))
    students.append({"Name": name, "Marks": marks})

def save_file():
    df = pd.DataFrame(students)
    df.to_csv("students.csv", index=False)
    print("Saved successfully")

def show_report():
    df = pd.read_csv("students.csv")
    df["Grade"] = df["Marks"].apply(lambda x: "A" if x >= 80 else "B" if x >= 60 else "C")
    print(df)

while True:
    print("\n1. Add Student")
    print("2. Save")
    print("3. Report")
    print("4. Exit")

    ch = input("Choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        save_file()
    elif ch == "3":
        show_report()
    elif ch == "4":
        break