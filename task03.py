import json

name = input("ismingizni kiriting: ")
age = int(input("yoshingizni kiriting: "))

try:
    with open("data.json", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

data.append({"name": name, "age": age})

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("malumot JSON faylga yozildi")