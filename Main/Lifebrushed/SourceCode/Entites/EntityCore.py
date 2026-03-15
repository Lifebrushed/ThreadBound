import Logic.Dnd as Dnd
import Logic.Tags as Tags

class CreatureBase() : # guys no one fucking touch this if you touch this the game will break
    def __init__(self, name="placeholder_name", str=0, dex=0, con=0, wil=0, int=0, cha=0, align=Tags.TN):
        self.name = name
        self.description = self.getDescription
        self.strength = str
        self.dexterity = dex
        self.constitution = con
        self.willpower = wil
        self.intelligence = int
        self.charisma = cha
        self.level = 1
        self.maxhealth = self.getMaxHealth()
        self.health = self.maxhealth
        self.ac = self.getArmorClass()
        self.alignment = align

    def getMaxHealth(self):
        MaxHealth = Dnd.d12(self.level) + self.getStatBonus(self.constitution)
        return MaxHealth
    
    def TakeDamage(self, damage):
        self.health = self.health - damage

    def getArmorClass(self):
        AC = 10 + self.getStatBonus(self.constitution)
        return AC
    
    def getStatBonus(self, stat):
        StatBonus = (stat - 10)//2
        return StatBonus
    
    def getDescription(self):
        description = "the description was too long to put in the __init__ so i made it a function"
        return description