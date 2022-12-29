from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# from flask_bcrypt import bcrypt
# from flask_app.controllers.users_controller import bcrypt

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
        results =  connectToMySQL('login_and_reg').query_db(query, data)
        return results
    
    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results =  connectToMySQL('login_and_reg').query_db(query, data)
        
        if not results or len(results) < 1:
            return False
        else:
            return cls(results[0])
    
    
    @staticmethod
    def validate_user(data):
        is_valid = True
        
        if len(data['first_name']) < 2:
            is_valid = False
            flash('invalid first name')
            
        if len(data['last_name']) < 2:
            is_valid = False
            flash('invalid last name')
            
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('invalid email')
            
        if len(data['password']) < 8:
            is_valid = False
            flash('invalid pw')
        
        return is_valid