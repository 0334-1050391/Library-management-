from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrowed_date = None

    def borrow(self, user):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = user
            self.borrowed_date = datetime.now()
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            self.borrowed_by = None
            self.borrowed_date = None
            return True
        return False

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow(self):
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

    def calculate_fine(self, book, fine_rate=1):
        if book.borrowed_date:
            days_overdue = (datetime.now() - book.borrowed_date).days - 14
            if days_overdue > 0:
                return days_overdue * fine_rate
        return 0

class Librarian:
    def __init__(self, name):
        self.name = name

    def search_books(self, library, keyword):
        return [book for book in library.books if keyword.lower() in book.title.lower()]

    def calculate_overdue_fines(self, user, fine_rate=1):
        total_fine = 0
        for book in user.borrowed_books:
            total_fine += user.calculate_fine(book, fine_rate)
        return total_fine

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

# Example usage
library = Library()
book1 = Book("1984", "George Orwell", "123456789")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321")
library.add_book(book1)
library.add_book(book2)

user = User("Alice", "U001")
librarian = Librarian("Bob")

# User borrows a book
user.borrow_book(book1)

# Librarian searches for a book
found_books = librarian.search_books(library, "Mockingbird")
print([book.title for book in found_books])

# User returns a book
user.return_book(book1)

# Calculate overdue fines
overdue_fine = librarian.calculate_overdue_fines(user)
print(f"Overdue fine for {user.name}: ${overdue_fine}")