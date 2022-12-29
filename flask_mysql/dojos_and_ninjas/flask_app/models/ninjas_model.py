from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        
    # @classmethod
    # def get_all(cls, data):
    #     query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = dojo_id WHERE name = %(name)s;"
    #     results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
    #     dojo = (cls(results[0]))
    #     ninjas = []
    #     for ninja in results:
    #         data = {
    #             **ninja,
    #             'id': 'ninjas.id',
    #             'created_at' : 'ninjas.created_at',
    #             'updated_at' : 'ninjas.updated_at'
    #         }
    #         ninjas.append(cls(data))
    #     dojo.ninjas = ninjas
    #     return dojo
    
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s, NOW(), NOW(), %(dojo_id)s);'
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)