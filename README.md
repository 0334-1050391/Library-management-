# Book class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.is_available}")

# Member class
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_issued = []

    def issue_book(self, book):
        if book.is_available:
            book.is_available = False
            self.books_issued.append(book)
            print(f"{book.title} issued to {self.name}")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.books_issued:
            book.is_available = True
            self.books_issued.remove(book)
            print(f"{book.title} returned by {self.name}")
        else:
            print("Book not found in issued list.")

# Library class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            book.display_info()

# Example Usage
library = Library("City Library")

# Adding books
book1 = Book(1, "Python Programming", "John Doe")
book2 = Book(2, "Data Structures", "Jane Smith")

library.add_book(book1)
library.add_book(book2)

# Adding members
member1 = Member(101, "Ali")
member2 = Member(102, "Sara")

library.add_member(member1)
library.add_member(member2)

# Issue and return operations
library.display_books()
member1.issue_book(book1)
library.display_books()
member1.return_book(book1)
library.display_books()