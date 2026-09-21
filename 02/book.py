class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return '"' + self.title + '" - ' + self.author + " (" + str(self.year) + ")"

book_1 = Book("Python dla początkujących", "Jan Kowalski", 2022)
book_2 = Book("Hobbit, czyli tam i z powrotem", "J.R.R. Tolkien", 1937)
book_3 = Book("Miecz przeznaczenia", "Andrzej Sapkowski", 1992)

print(book_1)
print(book_2)
print(book_3)
