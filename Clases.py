'''class ClassName:
    def_init_(self, name, age):
        self.name = name
        self.age = age
        
    def sample_method(self):
        print(self.name.upper())'''
        
'''class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f'{self.name.upper()} says woof woof! i´m {self.age} years old!')
        
dog_1 = Dog('Jack', 3)
dog_2 = Dog('Thatcher', 5)
        
        
dog_1.bark()
dog_2.bark()'''

'''class Dog:
    species = 'French bulldog'
    
    def __init__(self, name):
        self.name = name
        
print(Dog.species)

dog1= Dog('Jack')
print(dog1.name)
print(dog1.species)

dog2 = Dog('Tom')
print(dog2.name)
print(dog2.species)'''

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        
car_1 = Car('red', 'Toyota Corolla')
car_2 = Car('greem', 'Lamborghini Revuelto')

print(car_1.model)
print(car_2.model)

print(car_1.color)
print(car_2.color)