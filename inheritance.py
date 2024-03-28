# inheritance
## car class blueprint

class Car:
    def __init__(self,windows,door,enginetype):
        self.windows = windows
        self.door = door
        self.enginetype = enginetype
        
    def driving(self):
        print('car is used for driving')
        
     # audii car is inherting from the car class   
class Audi(Car):
    def __init__(self,windows,door,enginetype,horsepower):
        super().__init__(windows,door,enginetype)
        self.horsepower = horsepower
        
    def selfdriving(self):
        print("it is self driving car")
        
        
        
audiq7 = Audi(4,5,'diesel',200)
print(audiq7.horsepower)
print(audiq7.windows)
audiq7.driving()
audiq7.selfdriving()

car1 = Car(4,5,'diesel')

        