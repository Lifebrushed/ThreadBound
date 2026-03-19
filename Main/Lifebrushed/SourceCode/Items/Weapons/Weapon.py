import Items.ItemCore as Items
import Logic.Dnd as Dnd
import Logic.Tags as Tags
import Entites.EntityCore as Entities

class Slash():

    def __init__(self, name="Slash", id="attack:slash"):
        self.Name = name
        self.Description = self.getDescription()

    def getDescription(self):   
        desc = "A basic slash! Deals 1d8 + The player's strength bonus!"
        return desc

    def Use(self, player=Entities.Entity(), Enemy=Entities.Entity(), Damage=Dnd.d8(1)):
        stats = player.Stats
        roll = Dnd.d20

        Dmg = Damage

        

        if roll + player.getStatBonus(stats.strength) < Enemy.AC : 
            print("Missed!")
            return
        elif roll == 20 :
            Dmg = Dmg*2
        
        print(player.Name + " Attacked!")
        Enemy.TakeDamage(Dmg)



class Weapon(Items.Item):
    def __init__(self, name="placeholder item", rarity=Tags.COMMON, itemid="item:placeholder_item"):
        super().__init__(name, rarity, itemid)
        self.Attack = Slash()
    

    

        