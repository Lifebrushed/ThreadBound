import Dnd

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
    def __init__(self, name, sides, count, id):
        self.Name = name
        self.Sides = sides
        self.Count = count
        self.ID = str("attack:" + str(id))
    
    def Use(self, user : Entity, victim : Entity):
        bonus = user.Stats.getStatBonus("Strength")
        roll = Dnd.roll20()
        dmg = Dnd.roll(self.Count, self.Sides)
        if roll == 20 :
            dmg = dmg*2
        elif roll + bonus < victim.AC :
            print("Missed!")
            return
        dmg = dmg + bonus

        victim.takeDamage(dmg)
    



        