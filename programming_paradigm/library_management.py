# library_management.py

class Book:
    """A class to represent a book in the library."""

    def __init__(self, title, author):
        """Initialize a book with its title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track if the book is checked out

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class to represent a library that manages a collection of books."""

    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a new book to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Only Book instances can be added to the library.")

    def check_out_book(self, title):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
