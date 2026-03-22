import Dnd
import Tags


class StatBlock(): # 7th time rewriting the code. I'M GOING INSANE
    def __init__(self, str, con, dex, intel, wil, cha, pyreweave, tidetwine, stonebind, tempestcoil):
        self.Strength = str
        self.Constitution = con
        self.Dexterity = dex
        self.Intelligence = intel
        self.Willpower = wil
        self.Charisma = cha
        self.Pyreweave = pyreweave
        self.Tidetwine = tidetwine
        self.Stonebind = stonebind
        self.Tempestcoil = tempestcoil
    
    def getStatBonus(self, stat_name: str):
        value = getattr(self, stat_name)
        value = (value - 10) // 2
        return value

class Entity():
    def __init__(self, name : str, stats : StatBlock, id : str):
        self.Name = name
        self.Stats = stats
        self.ID = str("entity:" + str(id))
        self.MaxHealth = self.getMaxHealth()
        self.Health = self.MaxHealth
        self.AC = self.getArmorClass()
    
    def getActions(self):
        actions = [
            
        ]
        return actions
    
    def getInitiative(self):
        initiative = Dnd.roll20() + self.Stats.getStatBonus("Dexterity")
        return initiative

    def getTags(self):
        return [
            Tags.ENTITY
        ]
    
    def checkPlayer(self):
        if Tags.findTagIn(Tags.PLAYER, self.getTags()) :
            return True
        else :
            return False
    
                

    def getArmorClass(self):
        bonus = self.Stats.getStatBonus("Constitution")
        ac = 10 + bonus
        return ac
    
    def getMaxHealth(self):
        return 10 + self.Stats.getStatBonus("Constitution")
    
    def takeDamage(self, damage):
        print(str(self.Name) + " took damage!")

        self.Health -= damage
        if self.Health < 0:
            print(str(self.Name) + " Died!")
            self.Health = 0
        
        



class Attack():
    def __init__(self, name, count, sides, id):
        self.Name = name
        self.Sides = sides
        self.Count = count
        self.ID = str("attack:" + str(id))
    
    def getTags(self):
        return [
            Tags.ATTACK
        ]
    
    def __str__(self):
        return self.Name
        
    

    
    def Use(self, user : Entity, victim : Entity):
        bonus = user.Stats.getStatBonus("Strength")
        roll = Dnd.roll20()
        dmg = Dnd.roll(self.Count, self.Sides)

        print(str(dmg))

        if roll == 20 :
            dmg = dmg*2
        elif roll + bonus < victim.AC :
            print("Missed!")
            return
        dmg = dmg + bonus


        victim.takeDamage(dmg)
    
class Item():
    def __init__(self, name : str, description : str, id):
        self.Name = name
        self.ID = str("item:" + str(id))
        self.Description = description

class Weapon(Item): # IT FUCKING WORKS
    def __init__(self, name, description, statreq : StatBlock, attack : Attack, id):
        super().__init__(name, description, id)
        self.Attack = attack
        self.StatRequirements = statreq
    
    def Use(self, user, victim):
        self.Attack.Use(user, victim)

    
    def checkStatRequirement(self, user : Entity):
        if self.StatRequirements.Strength > user.Stats.Strength :
            return False
        if self.StatRequirements.Dexterity > user.Stats.Dexterity :
            return False
        if self.StatRequirements.Constitution > user.Stats.Constitution :
            return False
        if self.StatRequirements.Willpower > user.Stats.Willpower :
            return False
        if self.StatRequirements.Intelligence > user.Stats.Intelligence :
            return False
        if self.StatRequirements.Charisma > user.Stats.Charisma :
            return False
        
        if self.StatRequirements.Pyreweave > user.Stats.Pyreweave :
            return False
        if self.StatRequirements.Tempestcoil > user.Stats.Tempestcoil :
            return False
        if self.StatRequirements.Tidetwine > user.Stats.Tidetwine :
            return False
        if self.StatRequirements.Stonebind > user.Stats.Stonebind :
            return False
        
        return True
