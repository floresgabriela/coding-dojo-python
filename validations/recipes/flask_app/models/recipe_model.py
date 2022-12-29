from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user_model import User


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under = data['under']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, under, description, instructions, date_made, created_at, updated_at, user_id) VALUES (%(name)s, %(under)s, %(description)s, %(instructions)s, %(date_made)s, NOW(), NOW(), %(user_id)s);"
        results = connectToMySQL('recipes').query_db(query, data)
        return results
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL('recipes').query_db(query)
        
        recipes = []
        for result in results:
            recipe = cls(result)
            
            user_data = {
                **result,
                'id' : result['users.id'],
                'created_at' : result['users.created_at'],
                'updated_at' : result['users.updated_at']
            }
            
            creator = User(user_data)
            recipe.creator = creator
            recipes.append(recipe)
            
        return recipes
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        
        if not results or len(results) < 1:
            return False
        else:
            return cls(results[0])
        
    @classmethod
    def view_recipe(cls, data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        result = results[0]
        recipe = cls(results[0])
        
        user_data = {
                **result,
                'id' : result['users.id'],
                'created_at' : result['users.created_at'],
                'updated_at' : result['users.updated_at']
            }
        creator = User(user_data)
        recipe.creator = creator
        return recipe
        
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under=%(under)s, updated_at=NOW() WHERE id=%(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        return results
    
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        return results
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        
        if len(data['name']) < 3:
            is_valid = False
            flash('Name must not be blank.', 'edit')
            
        if len(data['description']) < 3:
            is_valid = False
            flash('Description must not be blank.', 'edit')
            
        if len(data['instructions']) < 3:
            is_valid = False
            flash('Description must not be blank.', 'edit')
            
        return is_valid         