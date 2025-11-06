class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book("Alkimyogar", "Paulo Coelho", 1988)
book2 = Book("Sariq devni minib", "X. Toxtaboyev", 1970)

print(book1.title, "-", book1.author, "-", book1.year)
print(book2.title, "-", book2.author, "-", book2.year)