from pymongo import MongoClient
from bson.objectid import ObjectId


class Livro:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def add_livro(self, titulo: str, autor: str, ano: int, preco: float) -> str:
        try:
            result = self.collection.insert_one(
                {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            book_id = str(result.inserted_id)
            print(f"Livro criado: {titulo}, id: {book_id}")
            return book_id
        except Exception as error:
            print(f"Error: {error}")
            return None

    def encontra_livro(self, book_id: str) -> dict:
        try:
            book = self.collection.find_one({"_id": ObjectId(book_id)})
            if book:
                print(f"Livro: {book}")
                return book
            else:
                print(f"Livro com id {book_id} não encontrado")
                return None
        except Exception as error:
            print(f"Error: {error}")
            return None

    def corrige_livro(self, book_id: str, titulo: str, autor: str, ano: int, preco: float) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(book_id)}, {
                                                "$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            if result.modified_count:
                print(
                    f"Livro com id: {book_id} atualizado, título: {titulo}, autor: {autor}, ano: {ano}, preço: {preco}")
            else:
                print(f"Livro com id {book_id} não encontrado")
            return result.modified_count
        except Exception as error:
            print(f"Error: {error}")
            return None

    def exclui_livro(self, book_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(book_id)})
            if result.deleted_count:
                print(f"Livro com id {book_id} deletado")
            else:
                print(f"Livro com id {book_id} não encontrado")
            return result.deleted_count
        except Exception as error:
            print(f"Error: {error}")
            return None
