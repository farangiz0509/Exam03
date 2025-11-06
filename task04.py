import json

name = input("Ismingizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))

try:
    with open("data.json", "r") as f:
        users = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    users = []

users.append({"name": name, "age": age})

with open("data.json", "w") as f:
    json.dump(users, f, indent=4)

print("Ma'lumot yozildi!")