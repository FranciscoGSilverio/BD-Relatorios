from database import Database
from write_a_json import write_a_json

db = Database(database="mercado", collection="compras")


class ProductAnalyzer:

    #Busca o total de vendas em um dia
    def total_vendas_no_dia(self):
        result = db.collection.aggregate([
            {
                "$group": {
                    "_id": "$data_compra",
                    "total": {
                        "$count": {}
                    }
                }
            }
        ])
        write_a_json(result, "total_vendas")

    #Busca o produto mais vendido
    def produto_mais_vendido(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"}, {"$group": {"_id": "$produtos.descricao",
                                                  "total": {"$count": {}}}}, {"$sort": {"total": -1}}, {"$limit": 1}
        ])
        write_a_json(result, "mais_vendidos")

    #Busca o cliente que mais gastou
    def cliente_mais_gastou(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"}, {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": [
                "$produtos.quantidade", "$produtos.preco"]}}}}, {"$sort": {"total": -1}}, {"$limit": 1}
        ])
        write_a_json(result, "cliente_mais_gastou")

    #Busca os produtos que foram comprados mais de uma vez
    def produto_mais_de_uma_compra(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"}, {"$group": {
                "_id": "$produtos.descricao", "total": {"$count": {}}}}
        ])
        write_a_json(result, "produtos_mais_de_uma_compra")
