from database import Database
from school_database import SchoolDatabase
from player_match_database import PlayerMatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.198.174.141:7687", "neo4j", "grips-branches-dose")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
player_match = PlayerMatchDatabase(db)

# Criando um jogador
player_match.create_player("Jogador 1")
player_match.create_player("Jogador 2")
player_match.create_player("Jogador 3")

#Criando uma partida
player_match.create_match("Partida 1")
player_match.create_match("Partida 2")

#Criando uma relação entre jogador e partida
player_match.create_player_match("Jogador 1", "Partida 1", "Jogador 1")
player_match.create_player_match("Jogador 2", "Partida 1", "Jogador 1")
player_match.create_player_match("Jogador 1", "Partida 2", "Jogador 2")
player_match.create_player_match("Jogador 2", "Partida 2", "Jogador 2")

# Atualizando o nome de um jogador
player_match.update_player("Jogador 3", "Ronaldo Fenomeno");

# Recuperando os jogadores
players = player_match.get_players()
print("Jogadores:")

for player in players:
    print(player)

# Deletando um jogador
player_match.delete_player("Ronaldo Fenomeno")

# Recuperando uma partida pelo nome
matches = player_match.get_match_by_name("Partida 1")
print("\nPartida 1:")
for match in matches:
    print(match)

# Recuperando as relações entre jogadores e partidas
player_matches = player_match.get_player_matches("Jogador 1")
print("\nPartidas e resultados do Jogador 1:")
for player_match in player_matches:
    print(player_match)


# Fechando a conexão com o banco de dados
db.close()