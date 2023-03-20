class Animal:

    all = []
    
    def __init__ (self, species, weight, nickname, zoo):
        self.nickname = {nickname}
        self.species = {species}
        self.weight = weight
        self.all_animal_addition(self)
        self.zoo = zoo

    @classmethod
    def all_animal_addition(cls, self):
        cls.all.append(self)

    @classmethod
    def find_by_species(cls, species):
        species_list = []

        for animal_object in cls.all:
            if animal_object.species == {species}:
                species_list.append(animal_object.nickname)

        return species_list
    
        # return species_list
