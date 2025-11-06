import json

try:
    with open("data.json", "r") as f:
        users = json.load(f)
        for u in users:
            print(f"Name: {u['name']}, Age: {u['age']}")
except FileNotFoundError:
    print("fayl topilmadi!")