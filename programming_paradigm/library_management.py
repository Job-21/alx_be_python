# library_management.py

class Book:
    """Represents a book with a title and author, and its checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """Represents a collection of books and their availability status."""

    def __init__(self):
        self._books = []  # Private list of books

    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print a list of all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
