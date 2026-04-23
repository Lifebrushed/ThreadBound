import states

class Action():
    def __init__(self, name : str, key : str, displayname : str):
        self.Name = name
        self.DisplayName = displayname
        self.Key = key

        self.Enviorment = states.CurrentEnviorment.NoneUI
    
    def isTriggered(self, input : str, enviorment):
        if input == self.Key and enviorment == self.Enviorment:
            pass