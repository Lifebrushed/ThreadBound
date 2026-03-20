import Core

def main():
    testEntity = Core.Entity("Test", Core.StatBlock(10, 10, 10, 10, 10, 10, 0, 0, 0, 0), "test_entity")
    testEnemy = Core.Entity("TestEnemy", Core.StatBlock(10, 10, 10, 10, 10, 10, 0, 0, 0, 0), "test_enemy")
    testAttack = Core.Attack("Test", 2, 8, "attack_test")
    print(testEnemy.Health)
    testAttack.Use(testEntity,testEnemy)
    print(testEnemy.Health)
    
if __name__ == "__main__":
    main()