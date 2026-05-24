import pandas as pd
data = pd.read_csv("dirty_students.csv")
print(data.isnull().sum())
cleaned = data.dropna()
print(cleaned)
cleaned.to_csv("cleaned.csv", index=False)
print("cleaned file saved.")