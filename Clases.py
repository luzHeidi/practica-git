'''class ClassName:
    def_init_(self, name, age):
        self.name = name
        self.age = age
        
    def sample_method(self):
        print(self.name.upper())'''
        
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f'{self.name.upper()} says woof woof! i´m {self.age} years old!')
        
dog_1 = Dog('Jack', 3)
dog_2 = Dog('Thatcher', 5)
        
        
dog_1.bark()
dog_2.bark()