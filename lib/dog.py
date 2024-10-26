# /!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = ['Labrador', 'Beagle', 'Bulldog', 'Poodle', 'Rottweiler', 
                       'German Shepherd', 'Golden Retriever', 'French Bulldog']

    def __init__(self, name="Ashley", breed="Labrador") -> None:
        self._name = name  # Private attribute for name
        self._breed = breed  # Private attribute for breed

    @property
    def name(self):
        print("Retrieving name!")
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            print(f"Setting name to {value}")
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        print("Retrieving breed!")
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.APPROVED_BREEDS:
            print(f"Setting breed to {value}")
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

# Example Usage
dog = Dog()
print(dog.name)  # Retrieving name!
dog.name = "Max"  # Setting name to Max
print(dog.name)  # Retrieving name!
dog.breed = "Bulldog"  # Setting breed to Bulldog
print(dog.breed)  # Retrieving breed!
dog.breed = "Unknown"  # Breed must be in list of approved breeds.



