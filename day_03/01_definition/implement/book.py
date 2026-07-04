class Book:
    def __init__(self, title=None, genre=None, author=None):
        self.title = title
        self.genre = genre
        self.author = author

    def __repr__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Author: {self.author}"

book = Book ("The Hobbit", "Fantasy", "Tolkien")
print(book)