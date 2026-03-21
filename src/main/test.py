import Core
import Humanoids
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

def main():
    testEntity = Humanoids.Humanoid("Test Human", Core.StatBlock(20,20,20,20,20,20,20,13,20,15), "test_human")
    testEnemy = Humanoids.Humanoid("Test Enemy", Core.StatBlock(20,20,20,20,20,20,20,13,20,15), "test_human")
    print(testEnemy.Health)
    testEntity.Weapon.Use(testEntity, testEnemy)
    print(testEnemy.Health)
    
if __name__ == "__main__":
    main()