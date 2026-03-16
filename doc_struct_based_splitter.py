from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

code = """
class Car:
    species = "Vehicle"

    def __init__(self, make, model, year):
       
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Default attribute

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def display_details(self):
        
        return f"{self.year} {self.make} {self.model} is a {self.species}."



if __name__ == "__main__":
    # Create an instance (object) of the Car class
    my_new_car = Car("Audi", "A4", 2024)

    # Access attributes and call methods using the object and dot operator
    print(my_new_car.display_details())
    my_new_car.read_odometer()

    # Update an attribute and call a method
    my_new_car.update_odometer(50)
    my_new_car.read_odometer()

    # Attempt to roll back the odometer (will be rejected)
    my_new_car.update_odometer(20)
    """
splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=300,
        chunk_overlap=0
    )

chunks = splitter.split_text(code)

print(chunks)

