import random

class Farm:
    def __init__(self, farm_name, owner):
        self.name = farm_name
        self.owner = owner
    
    def __str__(self):
        return f'{self.name} belongs to {self.owner}.'

class Animal:
    places = ['Bedroom', 'Barn', 'Kitchen', 'Toilet', 'Bath', 'Living Room']
    drinks = ['CocaCola', 'Pepsi', 'Sprite', 'Beer', 'Water', 'Milkis']

    def __init__(self, farm, name):
        self.farm = farm
        self.name = name

    def eat(self):
        food = ['Meat', 'Grass', 'Pizza', 'KFC', 'McDonalds Burgers', 'Hay', 'Apple', 'Banana']
        food_1 = random.choice(food)
        place_1 = random.choice(self.places)  
        return place_1, food_1
    
    def drink(self):
        return random.choice(self.drinks)
    
    def relieve(self):
        return random.choice(self.places)

    def __str__(self):
        return f'This {self.name} belongs to the farm "{self.farm.name}" owned by {self.farm.owner}.'

class Dog(Animal):
    def __init__(self, name, farm):
        super().__init__(farm, name)  

    def dog_eat(self):
        s, p = self.eat()
        print(f'The dog is eating {p} in the {s}.')

    def bark(self):
        print("Shsh... Do you hear the dog barking?")
        d = input(f"Where do you think it is? {self.places}: ")
        s = self.relieve()
        if d == s:
            print(f"You found it! It was barking in the {s}.")
        else:
            print(f"Imagine, it is barking from {s}?!")

class Donkey(Animal):
    def __init__(self, name, farm):
        super().__init__(farm, name)  

    def donkey_drink(self):
        place = self.relieve()
        drink = self.drink()
        print(f"Guess where and what the donkey is drinking!")
        c_place = input(f"Choose a place {self.places}: ")
        c_drink = input(f"Choose a drink {self.drinks}: ")

        if c_place == place and c_drink != drink:
            print(f"You found the place! Imagine, the donkey was drinking {drink} in the {place}.")
        elif c_place != place and c_drink == drink:
            print(f"You found the drink! Imagine, the donkey was drinking {drink} in the {place}.")
        elif c_place != place and c_drink != drink:
            print(f'Unfortunately, you could not guess it. The donkey was drinking {drink} in the {place}.')
        else:
            print(f'Wow, you found both! Indeed, the donkey was drinking {drink} in the {place}.')

farm = Farm("Unusual Farm", "Johnny Depp")
dog = Dog("Dog", farm)
donkey = Donkey("Donkey", farm)

print(dog)
dog.bark()
dog.dog_eat()

print(donkey)
donkey.donkey_drink()