import Core
import Weapons

class Humanoid(Core.Entity):
    def __init__(self, name, stats, id):
        super().__init__(name, stats, id)
        self.Weapon = Weapons.Fists

class Player(Humanoid):
    def __init__(self, name, stats, id):
        super().__init__(name, stats, id)
    
    def equipWeapon(self, weapon : Core.Weapon):
        if weapon.checkStatRequirement(self) :
            self.Weapon = weapon
            print( self.Name + " Equipped " + weapon.Name)
        else :
            print("You do not meet the stat requirements to equip this weapon!")