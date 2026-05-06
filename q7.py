class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self, make, model, year): #runs when a new Car is created, sets up its details
        self.make = make                   #stores make as attribute
        self.model = model                 #stores model as attribute
        self.year = year                   #stores year as attribute

    def describe_car(self):
        print(self.year,self.make, self.model) # prints year, make, model
    


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

my_car = Car("Toyota","Corolla",2020)
my_car.describe_car()
