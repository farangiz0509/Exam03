name = input("Ismingizni kiriting: ")
age = input("Yoshingizni kiriting: ")

with open("data.txt", "a") as file:
    file.write(f"{name} – {age} yosh\n")

print("malumot faylga yozildi!")