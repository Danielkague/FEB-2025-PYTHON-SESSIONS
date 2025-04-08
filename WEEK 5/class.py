#class Car:
    #color = "red"  # class variable
    #model = "BMW" # class variable


    # Method/behaviour to dislay the car details
    #def drive(self):
        #print("The car is driving")

#my_car = Car()  # create an instance of the Car class
#my_car.drive()  # call the drive method
#print(my_car.color)  # access the color attribute
#print(my_car.model)  # access the model attribute













class Person:
    # constructor method to initialize the object
    def __init__(self, name, age, height):
        self.name = name # instance variable for name
        self.age = age # instance variable for age
        self.height = height

personDetails = Person("Daniel", 25, 54.5) # create an instance of the Person class

print(personDetails.name) # access the name attribute
print(personDetails.age) # access the age attribute
print(personDetails.height) # access the height attribute

