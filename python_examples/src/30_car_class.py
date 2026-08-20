# // public variables
# // id, make, model, no_of_variants,  colors, range, mileage, price_range, thumbnail

# // public methods
# // get_name(make, model):
# 	// return make +  " " model

# // get_price_range(range):
# 	// min = .....
# 	// max = ....
# 	// return min + " -" + max


class Car:
    """car class"""

    id = 0
    make = ""
    model = ""
    no_of_variants = 0
    colors = []
    range = ""
    mileage = ""
    price_range = [0]
    thumbnail = ""

    def __init__(self, id, make, model, no_of_variants, colors):
        self.id = id
        self.make = make
        self.model = model
        self.no_of_variants = no_of_variants
        self.colors = colors

    def get_name(self):
        return self.make + " " + self.model


my_car1 = Car(2345678, "Mercedes-Benz", "CLA Electric", 3, ["red", "green", "blue"])
print(my_car1.id)
print(my_car1.make)
print(my_car1.model)
print(my_car1.no_of_variants)

print(my_car1.get_name())

print("==" * 100)

my_car2 = Car(34567890, "Mercedes-Benz", "CLE Electric", 5, ["red", "green", "blue"])
print(my_car2.id)
print(my_car2.make)
print(my_car2.model)
print(my_car2.no_of_variants)

print(my_car2.get_name())
