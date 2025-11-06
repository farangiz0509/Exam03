try:
    with open("data.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("fayl topilmadi!")
