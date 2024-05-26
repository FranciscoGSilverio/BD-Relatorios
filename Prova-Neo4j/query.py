class Queries:
    def __init__(self, db):
        self.db = db

    def questao_1A(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.cpf"
        results = self.db.execute_query(query)
        return [(result["t.ano_nasc"], result["t.cpf"]) for result in results]

    def questao_1B(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
        results = self.db.execute_query(query)
        return [(result["t.name"], result["t.cpf"]) for result in results]

    def questao_1C(self):
        query = "MATCH (c:City) RETURN c.name"
        results = self.db.execute_query(query)
        return [result["c.name"] for result in results]
    
    def questao_1D(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
        results = self.db.execute_query(query)
        return [(result["s.name"], result["s.address"], result["s.number"]) for result in results]

    def questao_2A(self):
        query = "MATCH (t:Teacher) RETURN min(t.ano_nasc), max(t.ano_nasc)"
        results = self.db.execute_query(query)
        return [(result["min(t.ano_nasc)"], result["max(t.ano_nasc)"]) for result in results]
    
    def questao_2B(self):
        query = "MATCH (c:City) RETURN avg(c.population)"
        results = self.db.execute_query(query)
        return [result["avg(c.population)"] for result in results]
    
    def questao_2C(self):
        query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN replace(c.name, 'a', 'A')"
        results = self.db.execute_query(query)
        return [result["replace(c.name, 'a', 'A')"] for result in results]
    
    def questao_2D(self):
        query = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1)"
        results = self.db.execute_query(query)
        return [result["substring(t.name, 2, 1)"] for result in results]