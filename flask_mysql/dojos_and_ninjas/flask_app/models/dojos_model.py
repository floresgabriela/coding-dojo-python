from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas_model import Ninja

class Dojo:
    def __init__(self, data, ninjas = []):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = ninjas
        
    @classmethod
    def get_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = dojo_id WHERE name = %(name)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojo = (cls(results[0]))
        ninjas = []
        for ninja in results:
            data = {
                **ninja,
                'id': 'ninjas.id',
                'created_at' : 'ninjas.created_at',
                'updated_at' : 'ninjas.updated_at'
            }
            ninjas.append(Ninja(data))
        dojo.ninjas = ninjas
        return dojo
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)