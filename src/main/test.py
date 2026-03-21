import Core
import EntityCore
import Weapons
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

def main():
    testEntity = EntityCore.Player("Test Human", Core.StatBlock(20,20,20,20,20,20,20,13,20,15), "test_player")
    testEnemy = EntityCore.Player("Test Enemy", Core.StatBlock(10,20,20,20,20,20,20,13,20,15), "test_player")
    testEntity.equipWeapon(Weapons.LumenitePolearm)
    testEnemy.equipWeapon(Weapons.LumenitePolearm)
    testEntity.Weapon.Use(testEntity, testEnemy)
    print(testEnemy.Health)
    
if __name__ == "__main__":
    main()