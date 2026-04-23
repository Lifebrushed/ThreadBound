import states

actionlib = []

class Action():
    def __init__(self, name : str, key : str, displayname : str):
        self.Name = name
        self.Key = key
        self.DisplayName = str("-[ " + self.key + " ]- " + displayname)

        self.Enviorment = states.CurrentEnviorment.Main_Menu
    
    def isTriggered(self, input : str, enviorment):
        if input == self.Key and enviorment == self.Enviorment:
            return True
        else:
            return False
    
    def Use(self, player=None):
        print(self.Key)
        print(self.DisplayName)

def getCurrentAction(key, enviorment):
    for action in actionlib:
        if action.isTriggered(key, enviorment) == True:
            return action

    return None

def getUsableActions(enviorment):
    actionlist = []
    for action in actionlib:
        if action.Enviorment == enviorment:
            actionlist.append
    
    return actionlist


