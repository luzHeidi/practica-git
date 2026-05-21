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

'''class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        
car_1 = Car('red', 'Toyota Corolla')
car_2 = Car('greem', 'Lamborghini Revuelto')

print(car_1.model)
print(car_2.model)

print(car_1.color)
print(car_2.color)'''

'''class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f'´{self.title}´ has {self.pages} pages'
    
    def __eq__(self, other):
        return self.pages == other.pages
    
book1 = Book('Built Wealth Like a Boss', 420)
book2 = Book('Be Your Own Start', 420)

print(len(book1))
print(len(book2))
print(str(book1))
print(str(book2))
print(book1 == book2)'''

'''class Cart:
    def __init__(self):
        self.items = []
        
    def add(self, item):
        self.items.append(item)
        
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')
            
    def list_items(self):
        return self.items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __contains__(self, item):
        return item in self.items
    
    def __iter__(self):
        return iter(self.items)
    

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
    print(item, end=' ')
    
print(len(cart))
print(cart[3])

print('Monitor' in cart)
print('banana' in cart)

cart.remove('Ergo keyboard')

print(cart.list_items())

cart.remove('banana')'''

#Manejo de atributos de objetos dinamicos

'''class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
my_car = Car('Lamborghini', 'Gallardo')
#print(my_car.brand)
#print(my_car.model)

#getattr

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
person = Person('John Doe', 30)

print(getattr(person, 'name'))
print(getattr(person, 'age'))
print(getattr(person, 'city', 'Milano'))'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
person = Person('John doe', 30)

attr_name = input('Enter the attribute you want to see: ?')
print(getattr(person, attr_name, 'Attribute not found'))