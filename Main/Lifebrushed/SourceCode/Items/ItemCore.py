import Logic.Tags as Tags
import Logic.Statblock as Stat
import Entites.EntityCore as Entities


class Item(): #istg i'm going insane please i beg you i need someone else to help me w/ this project

   def __init__(self, name="placeholder item", rarity=Tags.COMMON, itemid="item:placeholder_item"):  
        self.Name = name
        self.Description = self.getDescription()
        self.Rarity = rarity
        self.ID = itemid

   
   def isEnchantable(self): #check if its enchantable
        return False
   
   def isDroppable(self): #for once we start adding mutliplayer
        return True
   
   def getTags(self): # use this when u want to proc certain talents!
        tags = [
      
        ]
        return tags
   
   def getDescription(self):   
        desc = "this is a placeholder description!"
        return desc
   
class requirementItem(Item):
   def __init__(self, name="placeholder requirement item", rarity=Tags.COMMON, itemid="item:placeholder_requirement_item"):
       super().__init__(name, rarity, itemid)

   def getRequirements(self):
       req = Stat.statblock()
       return req

   def checkRequirement(self, player=Entities.Entity()):
       req = self.getRequirements()
       stats = player.Stats

       # physical req
       if stats.strength < req.strength:
           return False
       if stats.dexterity < req.dexterity:
           return False
       if stats.constitution < req.constitution:
           return False
       if stats.willpower < req.willpower:
           return False
       if stats.intelligence < req.intelligence:
           return False
       if stats.charisma < req.charisma:
           return False
       
       # magic req
       if stats.tempestcoil < req.tempestcoil:
           return False
       if stats.pyreweave < req.pyreweave:
           return False
       if stats.tidetwine < req.tidetwine:
           return False
       if stats.stonebind < req.stonebind:
           return False
       
       #if none of them r lower than req
       
       return True
          

       
       
       
       
       
   
   