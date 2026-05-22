#Definicion de clases

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print('{self.name.upper()} says woof woof')
        
        
#Creacion de Objetos

dog1 = Dog('Jack', 3)
dog2 = dog('Thatcher', 5)

#LLamar metodos en objetos

dog1.bark()
dog2.bark()

#Atributos de instancia y de clase

class Dog:
    species = 'French Bulldog' #atributo de clase
    
    def __init__(self, name):
        self.name = name        #atributo de instancia
        
print(Dog.species)

jack = Dog('Jack')
print(jack.name)
print(jack.species)

#Metodos

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        
    def describe(self):
        return f'This car is a {self.color} {self.model}'
    
my_car_1 = Car('red', 'Tesla Model S')
print(my_car_1.describe)

#Accediendo a Metodos

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        
    def describe(self):
        return f'This car is a {self.color} {self.model}'
    
my_car_1 = Car('red', 'Tesla Model S')
my_car_2 = Car('green', 'Lamborghini REvuelto')

print(my_car_1.describe())

print(my_car_2.describe())

#Metodos Dunder

    #Metodos especiales __init__ , __len__ , __str__ , __eq__
    

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages =pages
        
    def __len__(self):
        return self.pages

    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"
    
    def __eq__(self, other):
        return self.pages == other.pages
    
book1 = Book('Built Wealth Like a Boss', 420)
print(len(book1))
print(str(book1))

#Lamar a metodos dunder indirectamente

class Cart:
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
        return iter(self.items)
    
cart = Cart()
cart.add('Laptop')
print(len(cart))
print('Laptop' in cart)