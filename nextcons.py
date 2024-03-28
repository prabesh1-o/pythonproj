class Animal:
    def __init__(self,*args):
        if len(args)==1:
            self.name =args[0]
        elif len(args)==2:
            self.name = args[0]
            self.species = args[1]
        elif len(args)==3:
            self.name=args[0]
            self.species = args[1]
            self.age = args[2]
            
    
    def make_sound(self,sound):
        print("the name of the animal is {} and says {}".format(self.name,sound))
        
obj = Animal('cow','mammal',23)
print(obj.name)
print(obj.species)
print(obj.age)
obj.make_sound('baaba')