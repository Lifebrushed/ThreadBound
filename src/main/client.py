import states
import actions

linetxt = "----------------------------------------------------------------------------------------"
title = "T H R E A D - B O U N D"
authors = "Lifebrush????"


Running = True
CurrentEnviorment = states.CurrentEnviorment.Main_Menu


def FramePause():
    h = input(linetxt)

def MainMenu():
    print(title)
    print("Made by " + authors)

def PlayerInput():
    Input = str(input("-+- "))
    return Input


def Play():
    
    pass

while Running:
    print(linetxt)
    PressedKey = PlayerInput()

    if PressedKey == None:
        PressedKey = "No Action"
    CurrentAction = actions.getCurrentAction(PressedKey, CurrentEnviorment)
    if CurrentAction:
        CurrentAction.Use()
    
    if CurrentEnviorment == states.CurrentEnviorment.Main_Menu:
        MainMenu()
    elif CurrentEnviorment == states.CurrentEnviorment.Game:
        Play()
    


    print(linetxt)