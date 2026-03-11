class Ocean:
    def __init__(self, sea_creature_name, sea_creature_size):
        self.name = sea_creature_name
        self.size = sea_creature_size

    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.size}'

    def __repr__(self):
        return f"Ocean('{self.name}', {self.size})"

c = Ocean('Jellyfish', '30 cm')


print(str(c)) 


print(repr(c)) 
