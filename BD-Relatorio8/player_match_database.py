#Create the playerMatch class containing CRUD action to both player and match neo4j entities
#The players must have a name and a unique id
#The matches must have a unique id, a result(the player who won) and the players in the match

class PlayerMatchDatabase:
    def __init__(self, db):
        self.db = db

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, name):
        query = "CREATE (:Match {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def create_player_match(self, player_name, match_name, result):
        query = "MATCH (p:Player {name: $player_name}) MATCH (m:Match {name: $match_name}) CREATE (p)-[:PLAYED]->(m) SET m.result = $result"
        parameters = {"player_name": player_name, "match_name": match_name, "result": result}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.name AS name, m.result AS result"
        results = self.db.execute_query(query)
        return [(result["name"], result["result"]) for result in results]
    
    def get_match_by_name(self, name):
        query = "MATCH (m:Match) WHERE m.name = $name RETURN m.name AS name, m.result AS result"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [(result["name"], result["result"]) for result in results]

    def get_player_matches(self, player_name):
        query = "MATCH (p:Player {name: $player_name})-[r:PLAYED]->(m:Match) RETURN p.name AS player_name, m.name AS match_name, m.result AS result"
        parameters = {"player_name": player_name}
        results = self.db.execute_query(query, parameters)
        return [(result["player_name"], result["match_name"], result["result"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
    
    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    

    