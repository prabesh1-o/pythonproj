class Car:
    def __init__(self,windows,tyres,engine):
        self.windows = windows
        self.tyres = tyres
        self.engine = engine
        
        #method
    def self_driving(self):
       print('the car type is {} engine'.format(self.engine))
        
        
car1 = Car(4,4,'petrol')
print(car1.tyres)
print(car1.windows)
car1.self_driving()