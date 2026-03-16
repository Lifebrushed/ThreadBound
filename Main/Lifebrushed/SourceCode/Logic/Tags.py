# applicable tags onto stuff

#character alignments

LG = "alignment:lawful_good"
NG = "alignment:neutral_good"
CG = "alignment:chaotic_good"

LN = "alignment:lawful_neutral"
TN = "alignment:true_neutral"
CN = "alignment:chaotic_neutral"

LE = "alignment:lawful_evil"
NE = "alignment:neutral_evil"
CE = "alignment:chaotic_evil"

# elemental proccing

PYRE = "element:pyreweave"
TIDE = "element:tidetwine"
TEMPEST = "element:tempestcoil"
STONE = "element:stonebind"

# physical dmg types

BLUNT = "damagetypes:blunt"
SLASH = "damagetypes:slashing"
PIERCE = "damagetypes:piercing"

# item rarites

COMMON = "rarties:common"
UNCOMMON = "rarties:uncommon"
RARE = "rarties:rare"
EPIC = "rarties:epic"
LEGENDARY = "rarties:legendary"
MYTHIC = "rarties:mythic"

# size types (for entities)

TINY = "entitysizes:tiny"
SMALL = "entitysizes:small"
MEDIUM = "entitysizes:medium"
LARGE = "entitysizes:large"
MASSIVE = "entitysizes:massive"
GARGANTUAN = "entitysizes:gargantuan"

# creature types (for entities)

CELESTIAL = "creaturetypes:celestial"
FIEND = "creaturetypes:fiend"
CONSTRUCT = "creaturetypes:construct"
BEAST = "creaturetypes:beast"
DRAGON = "creaturetypes:dragon"
FEY = "creaturetypes:fey"
HUMANOID = "creaturetypes:humanoid"
UNDEAD = "creaturetypes:undead"

# item types
RESOURCE = "itemtype:resource"
EQUIPMENT = "itemtype:equipment"
WEAPON = "itemtype:weapon"

def findTagIn(tag=LG,list=[]):
    if tag in list :
        return True
    else :
        return False

