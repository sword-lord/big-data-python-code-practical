import json
data = '{"name":"Ayo","age":22}'
parsed = json.loads(data)
print(parsed)
print(parsed["name"])
print(parsed["age"])