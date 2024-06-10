from database import Database
from book import Book
from author import Author

bookDB = Database(database="library", collection="book")
authorDB = Database(database="library", collection="author")

book = Book(bookDB)
author = Author(authorDB)

author1 = author.add_author("Machado de Assis", '21-06-1839', 'M', [])
author1_id = author1
book_1 = book.add_book("Memórias Póstumas de Brás Cubas", '10-10-1880', 'romance', 350, author1_id)