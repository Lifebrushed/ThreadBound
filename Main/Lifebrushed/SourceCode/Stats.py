import Dnd

class CreatureBase() :
    def __init__(self, str=0, dex=0, con=0, wil=0, int=0, cha=0):
        self.strength = str
        self.dexterity = dex
        self.constitution = con
        self.willpower = wil
        self.intelligence = int
        self.charisma = cha
        self.level = 0
        self.maxhealth = self.getMaxHealth()
        self.health = self.maxhealth
        self.ac = self.getArmorClass()

    def getMaxHealth(self):
        MaxHealth = Dnd.d12(self.level)
        return MaxHealth
    
    def TakeDamage(self, damage):
        self.health = self.health - damage

    def getArmorClass(self):
        AC = 10 + self.constitution
    
    def getStatBonus(stat):
        StatBonus = (stat - 10)//2
        return StatBonus
    



        


    