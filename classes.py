#Single inheritance
#Parent class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Parent class')
        
#Child class
class Car(Vehicle):
    def Car_info(self):
        print('Inside Child class')
        
c1 = Car()

c1.Vehicle_info()
c1.Car_info()

#Multiple Inheritance
#Parent class
class Person:
    def Person_info(self, name, age):
        print('Inside person class')
        print('Name: ', name, 'Age: ', age)
         
#Parent class 2
class Company:
    def Company_info(self, name, location):
        print('Inside company class')
        print('Name: ', name, 'Location: ', location)
        
#Child class
class Employee(Person, Company):
    def Emplotee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary: ', salary, 'Skill: ', skill)
        
#Object of employee
emp = Employee()

#access data
emp.Person_info('Manasseh', 20)
emp.Company_info('Kengen', 'Kenya')
emp.Emplotee_info('200000', 'EEE')

#Multilevel inheritance
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

class Car(Vehicle):
    def Car_info(self):
        print('Inside Car class')
        
class sportsCar(Car):
    def sportsCar_info(self):
        print('Inside sportsCar class')
        
s_car = sportsCar()
s_car.Vehicle_info()
s_car.Car_info()
s_car.sportsCar_info()

#Hierachical Inheritance
class Vehicle:
    def Vehicle_info(self):
        print('This is vehicle')
        
class Car(Vehicle):
    def car_info(self, name):
        print('Car name is ', name)
class Truck(Vehicle):
    def truck_info(self, name):
        print('Truck name is ', name)
        
obj1 = Car()
obj1.Vehicle_info()
obj1.car_info("Mercedes")

obj2 = Truck()
obj2.Vehicle_info()
obj2.truck_info('FH')

#Hybrid inheritance
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

class Car(Vehicle):
    def Car_info(self):
        print('Inside Car class')
        
class Truck(Vehicle):
    def truck_info(self, name):
        print('Truck name is ', name)
        
class sportsCar(Car, Vehicle):
    def sportsCar_info(self):
        print('Inside sportsCar class')
        
s_car = sportsCar()
s_car.Vehicle_info()
s_car.Car_info()
s_car.sportsCar_info()

#Python super function
class Company:
    def Company_info(self):
        return 'Kengen'
    
class Employee(Company):
    def Employee_info(self):
        #Calling superclass
        c_name = super().Company_info()
        print('Manasseh works at ', c_name)
        
#Creating object

emp = Employee()
emp.Employee_info()

#issubclass()
print(issubclass(Employee, Company))
print(issubclass(Company, Employee))