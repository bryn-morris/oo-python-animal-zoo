from lib.animal import Animal

import ipdb

class Zoo:

    all = []
    
    def __init__(self, name = "Pereguin Zoo", location = "Bergenshire"):
        self.location = location
        self.name = name

        # self.animal_species = []

        self.store_zoo_data(self)

###########################################################################

    @classmethod
    def store_zoo_data (cls, self):
        cls.all.append(self)

    @classmethod
    def find_by_location(cls, location):
        
       return [zoo.name for zoo in cls.all if zoo.location == location]

        # location_list = []
        # iterate through all and return keys that are 
        # associated with location argument
        # return location_list        

###########################################################################
    def get_animals(self):

        return [animal for animal in Animal.all if animal.zoo == self]

    def get_animal_species(self):

        animal_species_list = [eachAnimalObj.species for eachAnimalObj in Animal.all if eachAnimalObj.zoo == self]

        new_animal_species_list = []

        for eachSpecie in animal_species_list:
            if eachSpecie not in new_animal_species_list:
                new_animal_species_list.append(eachSpecie)

        return new_animal_species_list


    def find_by_species(self, species):
        find_by_species_list = []

        for animal in self.animals:
            if animal.species == {species}:
                find_by_species_list.append(animal)

        return find_by_species_list

    def get_animal_nicknames(self):
        return [animal.nickname for animal in self.animals]
        # self.nickname_list = []
        # return nickname_list

    animals = property(get_animals)
    animal_species = property(get_animal_species,)
    animal_nicknames = property(get_animal_nicknames)

  


