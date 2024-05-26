from database import Database
from query import Queries
from TeacherCRUD import TeacherCRUD

db = Database("bolt://34.205.53.13:7687", "neo4j",
              "tickets-nomenclature-water")

queries = Queries(db)
teacherCRUD = TeacherCRUD(db)

questao_1A = queries.questao_1A()
print(questao_1A)

questao_1B = queries.questao_1B()
print(questao_1B)

questao_1C = queries.questao_1C()
print(questao_1C)

questao_1D = queries.questao_1D()
print(questao_1D)

questao_2A = queries.questao_2A()
print(questao_2A)

questao_2B = queries.questao_2B()
print(questao_2B)

questao_2C = queries.questao_2C()
print(questao_2C)

questao_2D = queries.questao_2D()
print(questao_2D)

questao_3B = teacherCRUD.create("Chris Lima", 1956, '189.052.396-66')

questao_3C = teacherCRUD.read("Chris Lima")
print(questao_3C)

questao_3D = teacherCRUD.update("Chris Lima", "162.052.777-77")
updatedCris  = teacherCRUD.read("Chris Lima")
print(updatedCris)