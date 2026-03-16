import Logic.Tags as tags

class item(): #istg i'm going insane please i beg you i need someone else to help me w/ this project
   def __init__(self, name="placeholder item", rarity=tags.COMMON, itemid="item:placeholder_item"):
        self.name = name
        self.description = self.getDescription()
        self.rarity = rarity
   
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
      
   
   