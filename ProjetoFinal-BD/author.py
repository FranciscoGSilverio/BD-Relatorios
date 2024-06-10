# author properties: id, name, birth_date, gender, books
from bson.objectid import ObjectId

class Author:
    def __init__(self, db):
        self.db = db
        self.collection = db.collection

    def add_author(self, name: str, birth_date: str, gender: str, books: list) -> str:
        try:
            result = self.collection.insert_one(
                {
                    "name": name,
                    "birth_date": birth_date,
                    "gender": gender,
                    "books": books
                })
            author_id = str(result.inserted_id)
            print(f"Author created: {name}, id: {author_id}")
            return author_id

        except Exception as error:
            print(f"Error: {error}")
            return None
    
    def find_author(self, author_id: str) -> dict:
        try:
            author = self.collection.find_one({"_id": ObjectId(author_id)})
            if author:
                print(f"Author: {author}")
                return author
            else:
                print(f"Author with id {author_id} not found")
                return None
        except Exception as error:
            print(f"Error: {error}")
            return None
        
    def update_author(self, author_id: str, name: str, birth_date: str, gender: str, books: list) -> int:
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(author_id)},
                {
                    "$set": {
                        "name": name,
                        "birth_date": birth_date,
                        "gender": gender,
                        "books": books
                    }})
            if result.modified_count:
                print(
                    f"Author with id: {author_id} updated, name: {name}, birth_date: {birth_date}")
            else:
                print(f"Author with id {author_id} not found")
            return result.modified_count
        except Exception as error:
            print(f"Error: {error}")
            return None
        
    def delete_author(self, author_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(author_id)})
            if result.deleted_count:
                print(f"Author with id {author_id} deleted")
            else:
                print(f"Author with id {author_id} not found")
            return result.deleted_count
        except Exception as error:
            print(f"Error: {error}")
            return None
