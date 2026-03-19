import Logic.Tags as tags
import Logic.Statblock as Stat

class Item(): #istg i'm going insane please i beg you i need someone else to help me w/ this project
   def __init__(self, name="placeholder item", rarity=tags.COMMON, itemid="item:placeholder_item"):
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
   def __init__(self, name="placeholder requirement item", rarity=tags.COMMON, itemid="item:placeholder_req_item"):
      super().__init__(name, rarity, itemid)
      self.StatRequirement = getRequirements()
   
   def getRequirements(self):
      req = Stat.statblock()
      return req

   def checkRequirement(self, player)
      pass
   
   