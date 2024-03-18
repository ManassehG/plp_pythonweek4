class Person:
    name = 'Skinny'
    
print(Person.name)

class People:
    def __init__(self) -> None: #Constructor method
        print('Constructor invoked')
        
details = People()

class People:
    def __init__(self) -> None: #Constructor method
        self.name = "Manasseh"
        self.age = 20
        
details = People().name #or similarly p1 = People() then call p1.name
print(details)

class People:
    def __init__(self, name, age) -> None: #Constructor method
        self.name = name
        self.age = age
        
p2= People('James', 20) #Passing instance attribute values
print(p2.name)
print(p2.age)

#Default Values
class People:
    def __init__(self, name ="Guest", age= 18) -> None: #Default attribute values
        self.name = name
        self.age = age
        
p2 = People()
print(p2.name)
print(p2.age)

class Info:
    def displayInfo(self):
        print('Displaying info')
        
p3 = Info()
p3.displayInfo()

class People:
    def __init__(self, name , age) -> None:
        self.name = name
        self.age = age
        
    def displayInfo(self):
        print(f'Person name: {self.name}, Person age: {self.age}')
        
p4 = People("Musa", 45)
p4.displayInfo()        