import json

name = input("Ismingizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))

try:
    with open("data.json", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

data.append({"name": name, "age": age})

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Ma’lumot JSON faylga yozildi!")