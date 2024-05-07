class Vehicle:
    def general_usage(self):
        print("general use: transportation.")

class Car(Vehicle):
    def __init__(self):
        print("I am a car.")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("specific usage: commute to work, vacation with family.")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I am a motor cycle.")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific usage: road trip, racing.")


c = Car()
# c.general_usage()
# c.specific_usage()


m = MotorCycle()
# m.general_usage()
# m.specific_usage()

print(isinstance(c,Car))
print(isinstance(c,MotorCycle))
print(issubclass(Car,Vehicle))  
print(issubclass(Car,MotorCycle))   



