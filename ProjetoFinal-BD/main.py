from database import Database
from book import Book
from author import Author

bookDB = Database(database="library", collection="book", name="book")
authorDB = Database(database="library", collection="author", name="author")

book = Book(bookDB, authorDB)
author = Author(authorDB)


def main():
    bookDB.resetDatabase()
    authorDB.resetDatabase()

    print("")
    print("Bem-vindo à biblioteca!")
    while True:
        print("")
        print("Escolha uma opção:")
        print("")
        print("1 - Adicionar autor")
        print("2 - Buscar autor")
        print("3 - Atualizar autor")
        print("4 - Deletar autor")
        print("5 - Adicionar livro")
        print("6 - Buscar livro")
        print("7 - Atualizar livro")
        print("8 - Deletar livro")
        print("9 - Sair")
        print("")
        option = input("Opção: ")

        if option == '1':
            name = input("Nome: ")
            birth_date = input("Data de nascimento: ")
            gender = input("Gênero: ")
            books = input("Livros: ")
            author.add_author(name, birth_date, gender, books)

        elif option == '2':
            author_id = input("Id do autor: ")
            author.find_author(author_id)

        elif option == '3':
            author_id = input("Id do autor: ")
            name = input("Nome: ")
            birth_date = input("Data de nascimento: ")
            gender = input("Gênero: ")
            books = input("Livros: ")
            author.update_author(author_id, name, birth_date, gender, books)

        elif option == '4':
            author_id = input("Id do autor: ")
            author.delete_author(author_id)

        elif option == '5':
            title = input("Título: ")
            publication_date = input("Data de publicação: ")
            genre = input("Gênero: ")
            pages = input("Páginas: ")
            author_id = input("Id do autor: ")
            book.add_book(title, publication_date, genre, pages, author_id)
            
        elif option == '6':
            book_id = input("Id do livro: ")
            book.find_book(book_id)

        elif option == '7':
            book_id = input("Id do livro: ")
            title = input("Título: ")
            publication_date = input("Data de publicação: ")
            genre = input("Gênero: ")
            pages = input("Páginas: ")
            author_id = input("Id do autor: ")
            book.update_book(book_id, title, publication_date,
                             genre, pages, author_id)

        elif option == '8':
            book_id = input("Id do livro: ")
            book.delete_book(book_id)

        elif option == '9':
            print("Goodbye!")
            break

        print("")


main()
