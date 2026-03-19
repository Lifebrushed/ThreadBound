import Logic.Dnd as Dnd
import Logic.Tags as Tags
import Logic.Statblock as Stat

class Entity() : # guys no one fucking touch this if you touch this the game will break
    def __init__(self, name="Placeholder Name", stats=Stat.statblock(), align=Tags.TN, Id="entity:placeholder_name"):
        self.Name = name
        self.Description = self.getDescription
        self.Stats = stats
        self.Levek = 1
        self.MaxHealth = self.getMaxHealth()
        self.Health = self.maxhealth
        self.AC = self.getArmorClass()
        self.Alignment = align

    def getMaxHealth(self):
        MaxHealth = Dnd.d12(self.level) + self.getStatBonus(self.constitution)
        return MaxHealth
    
    def TakeDamage(self, damage=0):
        self.Health = self.Health - damage

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


class Creature(Entity):
    
    def getBehavioralStats():
        pass
    
    def getBehavioralModifiers():
        pass
    
    
    
    