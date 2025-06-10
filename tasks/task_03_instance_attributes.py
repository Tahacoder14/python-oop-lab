"""
Task 3: Instance Attributes - An Object's Personal Data
Concept:
Instance attributes are variables unique to each object (instance).
Define a 'Book' and give it specific details like title, author, and page count.
Each book object you create will hold its own set of these details.
"""

class Book:
    def __init__(self, title, author, pages, genre):
        # These are instance attributes:
        self.title = title
        self.author = author
        self.pages = int(pages) # Ensure pages is an integer
        self.genre = genre
        self.current_page = 1 # Default for a new book
        print(f"Book created: '{self.title}' by {self.author} ({self.pages} pages, {self.genre}).")

    def read_to_page(self, page_number):
        if 1 <= page_number <= self.pages:
            self.current_page = int(page_number)
            print(f"You are now on page {self.current_page} of '{self.title}'.")
        else:
            print(f"Invalid page number. '{self.title}' has pages 1 to {self.pages}.")

    def get_info(self):
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Pages: {self.pages}. Currently on page {self.current_page}."

def get_input_params():
    return [
        {"name": "book_title", "label": "Book Title:", "type": "text_input", "default": "The Pythonic Journey"},
        {"name": "book_author", "label": "Author:", "type": "text_input", "default": "A. Coder"},
        {"name": "book_pages", "label": "Number of Pages:", "type": "number_input", "default": 300, "min_value": 1, "step": 1, "format": "%d"},
        {"name": "book_genre", "label": "Genre:", "type": "selectbox",
         "options": ["Fantasy", "Sci-Fi", "Mystery", "Educational", "Biography"], "default": "Educational"},
        {"name": "read_up_to", "label": "Read up to Page:", "type": "number_input", "default": 50, "min_value": 1, "step": 1, "format": "%d"}
    ]

def run_task(book_title, book_author, book_pages, book_genre, read_up_to):
    print("--- Creating your custom Book ---")
    my_book = Book(book_title, book_author, book_pages, book_genre)

    print("\n--- Reading your Book ---")
    my_book.read_to_page(read_up_to)
    print(my_book.get_info())

    print("\n--- Creating another Book to show attributes are per-instance ---")
    another_book = Book("Cosmic Wonders", "Stella Gazer", 250, "Sci-Fi")
    another_book.read_to_page(10)

    print("\n--- Comparing Book Info (Note how attributes differ) ---")
    print(f"Your Book: {my_book.get_info()}")
    print(f"Another Book: {another_book.get_info()}")

if __name__ == "__main__":
    run_task("Dune", "Frank Herbert", 896, "Sci-Fi", 150)