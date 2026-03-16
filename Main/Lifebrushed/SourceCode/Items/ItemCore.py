import Logic.Tags as tags

class item(): #istg i'm going insane please i beg you i need someone else to help me w/ this project
   def __init__(self, name="placeholder_name_item", rarity=tags.COMMON):
      self.name = name
      self.description = self.getDescription()
      self.rarity = rarity
   
   def isEnchantable(self): #check if its enchantable
      return false
   
   def isDroppable(self): #for once we start adding mutliplayer
      return true
   
   def getTags(self): # use this when u want to proc certain talents!
      tags = [
      
      ]
      return tags
   
   def getDescription(self):
      desc = "this is a placeholder description!"
      return desc
      
   
   