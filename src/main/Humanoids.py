import Core
import Weapons

class Humanoid(Core.Entity):
    def __init__(self, name, stats, id):
        super().__init__(name, stats, id)
        self.Weapon = Weapons.Fists