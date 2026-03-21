import Core
import Attacks

Fists = Core.Weapon(
    "Fists",
    "Your untrained fists. Worth a shot right?",
    Core.StatBlock(0,0,0,0,0,0,0,0,0,0),
    Attacks.Punch,
    'fist'
)

LumenitePolearm = Core.Weapon(
    "Lumenite Polearm",
    "A sturdy polearm forged from Lumenite.",
    Core.StatBlock(20,0,0,0,0,0,0,0,0,0),
    Attacks.Punch,
    "lumenite_polearm"
)