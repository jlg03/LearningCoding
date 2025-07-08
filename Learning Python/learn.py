class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale
    
    def drive(self):
        print(f"Your drive the car {self.model}")
    def stop(self):
        print(f"You stop the car {self.model}")

car1 = Car("Mustang", 2024, "red", False)

car1.drive()
car1.stop()
 