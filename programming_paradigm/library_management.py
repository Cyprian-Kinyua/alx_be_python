class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def return_book(self):
        Library.return_book(self.title)

    _is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        result = print(
            f"Book '{book.title}' by {book.author} added to the library.")
        return result

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                result = print(
                    f"{book.title} by {book.author} is now checked out.")
                return result
        result = "Book not available or already checked out."
        return result

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                result = print(f"{book.title} returned successfully.")
                return result
        result = "Book not found or not checked out."
        return result

    def list_available_books(self):
        available_books = []
        for book in self._books:
            if not book._is_checked_out:
                available_books.append(book.title)

            if not available_books:
                print("No available books.")
            else:
                book_list = print(
                    f"  {','.join(available_books)}")
                return book_list
