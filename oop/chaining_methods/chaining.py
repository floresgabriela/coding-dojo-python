class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        # print(self.first_name, '\n', self.last_name, '\n', self.email, '\n', self.age)
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
        
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
        
    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self
    
user1 = User("Gabriela", "Flores", "gflores@gmail.com", 25)
user2 = User("Angela", "Vo", "avo@gmail.com", 26)
user3 = User("Cathy", "Brown", "cbrown@gmail.com", 26)

user1.enroll().spend_points(50).display_info()
# user1.spend_points(50)
user2.enroll().spend_points(80).display_info()
# user2.spend_points(80)
# user1.display_info()
# user2.display_info()
user3.display_info()
# print(user1.gold_card_points)