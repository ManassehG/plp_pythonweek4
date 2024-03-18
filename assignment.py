class Person:
    name = "Manasseh"
    age = 20
    gender = "Male"
    
    def introduce(self):
        print(f'Your name is {self.name}. You are {self.age} years old and gender is {self.gender}')
        
p1 = Person()

p1.introduce()