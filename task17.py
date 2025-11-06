import json

class User:
    def __init__(self, username, email, is_active=True):
        self.username = username
        self.email = email
        self.is_active = is_active

    def save(self):
        try:
            with open("users.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append({
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active
        })

        with open("users.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"{self.username} saqlandi!")

    def deactivate(self):
        self.is_active = False
        print(f"{self.username} nofaol boldi.")

u1 = User("Ali", "ali@gmail.com", True)
u2 = User("Vali", "vali@gmail.com", False)

u1.save()
u2.save()

try:
    with open("users.json", "r") as f:
        data = json.load(f)
        for u in data:
            print(u)
except FileNotFoundError:
    print("Fayl topilmadi!")