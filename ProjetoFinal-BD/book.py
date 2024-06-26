# books properties: id, titulo, published_at, gender, pages, author_id
from bson.objectid import ObjectId

class Book:
    def __init__(self, db, authorDB):
        self.db = db
        self.collection = db.collection
        self.authorDB = authorDB

    def add_book(self, title: str, published_at: str, gender: str, pages: int, author_id: str) -> str:
        try:
            result = self.collection.insert_one(
                {
                    "title": title,
                    "published_at": published_at,
                    "gender": gender,
                    "pages": pages,
                    "author_id": author_id
                }
            )

            book_id = str(result.inserted_id)

             # Update author's books list
            author = self.authorDB.collection.find_one({"_id": ObjectId(author_id)})
            if author:
                books = author.get("books", "")
                if book_id not in books:
                    books = books + (', ' if books else '') + book_id
                    self.authorDB.collection.update_one(
                        {"_id": ObjectId(author_id)},
                        {"$set": {"books": books}}
                    )
            print(f"Book created: {title}, id: {book_id}")
            return book_id
        except Exception as error:
            print(f"Error: {error}")
            return None

    def find_book(self, book_id: str) -> dict:
        try:
            book = self.collection.find_one({"_id": ObjectId(book_id)})

            for key, value in book.items():
                print(f"{key}: {value}")
            else:
                print(f"Book with id {book_id} not found")
                return None
        except Exception as error:
            print(f"Error: {error}")
            return None

    def update_book(self, book_id: str, title: str, published_at: str, gender: str, pages: int, author_id: str) -> int:
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(book_id)},
                {
                    "$set": {
                        "title": title,
                        "published_at": published_at,
                        "gender": gender,
                        "pages": pages,
                        "author_id": author_id}})

            if result.modified_count:
                print(
                    f"Book with id: {book_id} updated, title: {title}, published_at: {published_at}")
            else:
                print(f"Book with id {book_id} not found")
            return result.modified_count
        except Exception as error:
            print(f"Error: {error}")
            return None

    def delete_book(self, book_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(book_id)})
            if result.deleted_count:
                print(f"Book with id {book_id} deleted")
            else:
                print(f"Book with id {book_id} not found")
            return result.deleted_count
        except Exception as error:
            print(f"Error: {error}")
            return None
