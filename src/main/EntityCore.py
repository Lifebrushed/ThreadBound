import Core
import Weapons
import Tags
import random

class Humanoid(Core.Entity):
    def __init__(self, name, stats, id):
        super().__init__(name, stats, id)
        self.Weapon = Weapons.Fists
    
    def getTags(self):
        return super().getTags() + [
            Tags.HUMANOID
        ]
    
    def getActions(self):
        actions = super().getActions() + [
            self.Weapon.Attack
        ]
        return actions
    
    def CombatTurn(self, victim):
        choice = random.randint(1, 100)
        if choice <= 30 :
            self.doNothing()
        else :
            print(self.Name + " Attacked!")
            self.Weapon.Use(self,victim)
    
    def doNothing(self):
        niloutcome = random.randint(1,10)
        if niloutcome == 1:
            print(self.Name + " Lazed around?")
        elif niloutcome == 2:
            print(self.Name + " Forgot what they were going to do????")
        elif niloutcome == 3:
            print(self.Name + " Tripped over their own feet?????")
        elif niloutcome == 4:
            print(self.Name + " Got distracted by a butterfly?")
        elif niloutcome == 5:
            print(self.Name + " Sneezed?")
        elif niloutcome == 6:
                print(self.Name + " Yawned.")
        elif niloutcome == 7:
                print(self.Name + " Stared at the wall.")
        elif niloutcome == 8: 
                print(self.Name + " Insulted your family. THat was pretty rude.")
        elif niloutcome == 9:
                print(self.Name + " Started thinking about what to have for dinner")
        elif niloutcome == 10:
                print(self.Name + " Gave up on what they were planning :/")

class Player(Humanoid):
    def __init__(self, name, stats, id):
        super().__init__(name, stats, id)
    
    def getTags(self):
        return super().getTags() + [
            Tags.PLAYER
        ]
    
    def equipWeapon(self, weapon : Core.Weapon):
        if weapon.checkStatRequirement(self) :
            self.Weapon = weapon
            print( self.Name + " Equipped " + weapon.Name)
        else :
            print("You do not meet the stat requirements to equip this weapon!")