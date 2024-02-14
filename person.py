class Person():
     def __init__(self, person_name, person_height, person_age):
         self.name = person_name
         self.height =  person_height
         self.age =person_age
class Superhero():
    def __init__(self, superhero_name, secret_identity, super_power, arch_enemy,lair):
        self.name=superhero_name
        self.identity=secret_identity
        self.power=super_power
        self.enemy=arch_enemy
        self.lair=lair
    def set_new_lair(self, new_lair):
        self.new_lair=new_lair
    def introduce(self):
            print (f" {self.identity} is actualy {self.name} and he fights {self.enemy} because he is {self.power}.")
    def get_lair(self):
        return self.lair