import Logic.Dnd as Dnd
import Logic.Tags as Tags

class CreatureBase() : # guys no one fucking touch this if you touch this the game will break
    def __init__(self, name="Placeholder Name", str=0, dex=0, con=0, wil=0, int=0, cha=0, align=Tags.TN, Id="entity:placeholder_name"):
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
        desc = "this is a placeholder description!"
        return desc
    
    def getTags(self):
        Tags = [
        
        ]
        return Tags