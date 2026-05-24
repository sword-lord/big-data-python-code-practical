import requests
import pandas as pd
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print("status code:", response.status_code)
data = response.json()
df = pd.DataFrame(data)
print(df[["id", "name", "username", "email"]])
df.to_csv("users.csv", index=False)
print("Data saved successfully!")