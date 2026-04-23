

linetxt = "----------------------------------------------------------------------------------------"
title = "T H R E A D - B O U N D"
authors = "Lifebrush????"


Running = True


def FramePause():
    h = input(linetxt)

def MainMenu():
    print(linetxt)
    print(title)
    print("Made by " + authors)

def PlayerInput():
    Input = str(input("-+- "))
    return Input


def Play():
    pass

while Running:
    PressedKey = PlayerInput()

    MainMenu()
    