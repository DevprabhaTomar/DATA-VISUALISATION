import pandas as pd

data = {
    "Name": ["Aman", "Ravi", "Sita"],
    "Math": [80, 60, 90],
    "Science": [70, 75, 85],
    "English": [88, 65, 95]
}

df = pd.DataFrame(data)

df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Percentage"] = df["Total"] / 3

def grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Percentage"].apply(grade)

print(df)