from database import Database
from model import Livro

db = Database(database="library", collection="book")
db.resetDatabase()
livro = Livro(db)

id_livro = livro.add_livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, 19.50)

livro.encontra_livro(id_livro)
livro.corrige_livro(id_livro, "O Cortiço", "Aluísio Azevedo" , 1890, 23.33)
livro.exclui_livro(id_livro)