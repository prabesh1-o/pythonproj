class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color= color
        
    def __init_(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species
        
    def make_sound(self,sound):
        print("the animal is{} and says {}".format(self.name,sound))
        

dog = Animal('dog','black')
print(dog.name)
dog.make_sound('wowowo')