# classes are real world entity or object
#attributes == properties of the class 
#methos == actions of the class




class Car:
    pass

Car1 = Car()
Car2 = Car()

Car1.windows = 2
Car1.tyrees = 4
Car1.engine = 'diesel'

Car2.windows = 4
Car2.tyres = 4
Car2.engine = 'petrol'

#print(Car1.engine)
#print(Car2.windows)

print(dir(Car1))
