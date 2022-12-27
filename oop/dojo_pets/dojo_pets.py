class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        
    def sleep(self):
        self.energy += 25
        print(self.energy)
        return self
        
    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.energy)
        return self
        
    def play(self):
        self.health += 5
        print(self.health)
        return self
        
    def noise(self):
        print("noise")
        return self


# class Dog(Pet):
#     def __init__(self, name, type, tricks, health, energy):
#         super().__init__(name, type, tricks, health, energy)