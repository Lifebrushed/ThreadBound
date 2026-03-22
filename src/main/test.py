import Core
import EntityCore
import Weapons
import os
import Combat

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

def main():
    Lifebrush = EntityCore.Humanoid(
        "Lief Brusche",
        Core.StatBlock(
            13,
            15,
            18,
            14,
            12,
            10,
            10,
            10,
            10,
            10
        ),
        "lifebrush"
    )
    Enemy = EntityCore.Humanoid(
        "Test Enemy",
        Core.StatBlock(
            20,
            15,
            10,
            13,
            11,
            10,
            12,
            0,
            15,
            0
        ),
        "enemy_test"
    )

    Combat.Start(Lifebrush, Enemy)
if __name__ == "__main__":
    main()