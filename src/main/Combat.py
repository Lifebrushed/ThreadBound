import Core
import EntityCore
import Weapons  
import Dnd
import Tags
import time

def Start(Player : EntityCore.Player, Enemy : EntityCore.Humanoid):
    print("Combat Started!")
    print(str(Player.Name) + " vs " + str(Enemy.Name))
    turn = 1
    while Player.Health > 0 and Enemy.Health > 0 :
        if turn % 2 == 0 :
            print(Player.Name + "'s Turn!")

        else :
            print(Enemy.Name + "'s Turn!")
        
        time.sleep(2.5)

        turn = turn + 1
        


