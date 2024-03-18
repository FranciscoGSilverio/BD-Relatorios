from database import Database
from ProductAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
db.resetDatabase()

analizador = ProductAnalyzer()
analizador.total_vendas_no_dia()
analizador.produto_mais_vendido()
analizador.cliente_mais_gastou()
analizador.produto_mais_de_uma_compra()
