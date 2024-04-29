import random

import wowraces


class wowclass:
    def __init__(self, name, races, tank_specs=[], healer_specs=[], zugger_specs=[]):
        self.name = name
        self.races = races
        self.tank_specs = tank_specs
        self.healer_specs = healer_specs
        self.zugger_specs = zugger_specs

    def roll_spec(self, role):
        tank_flag = role.tank_flag
        healer_flag = role.healer_flag
        if tank_flag is True:
            return random.choice(self.tank_specs)
        elif healer_flag is True:
            return random.choice(self.healer_specs)
        else:
            return random.choice(self.zugger_specs)

    def roll_race(self, banned_races, horde_only=False, alliance_only=False):
        # these should only be set on the first call to prevent infinite length lists
        if horde_only:
            banned_races = banned_races + wowraces.alliance_races
        elif alliance_only:
            banned_races = banned_races + wowraces.horde_races
        choice = random.choice(self.races)
        if choice in banned_races:
            return self.roll_race(banned_races)
        else:
            return choice


death_knight = wowclass(
    name="death knight",
    races=wowraces.dk_races,
    tank_specs=["blood"],
    zugger_specs=["frost", "unholy"],
)
demon_hunter = wowclass(
    name="demon hunter",
    races=wowraces.dh_races,
    tank_specs=["vengeance"],
    zugger_specs=["havoc"],
)
druid = wowclass(
    name="druid",
    races=wowraces.druid_races,
    tank_specs=["guardian"],
    healer_specs=["restoration"],
    zugger_specs=["balance", "feral"],
)
evoker = wowclass(
    name="evoker",
    races=wowraces.evoker_races,
    healer_specs=["preservation"],
    zugger_specs=["augmentation", "devastation"],
)
hunter = wowclass(
    name="hunter",
    races=wowraces.hunter_races,
    zugger_specs=["beast mastery", "marksmanship", "survival"],
)
mage = wowclass(
    name="mage", races=wowraces.mage_races, zugger_specs=["arcane", "fire", "frost"]
)
monk = wowclass(
    name="monk",
    races=wowraces.monk_races,
    tank_specs=["brewmaster"],
    healer_specs=["mistweaver"],
    zugger_specs=["windwalker"],
)
paladin = wowclass(
    name="paladin",
    races=wowraces.paladin_races,
    tank_specs=["protection"],
    healer_specs=["holy"],
    zugger_specs=["retribution"],
)
priest = wowclass(
    name="priest",
    races=wowraces.priest_races,
    healer_specs=["discipline", "holy"],
    zugger_specs=["shadow"],
)
rogue = wowclass(
    name="rogue",
    races=wowraces.rogue_races,
    zugger_specs=["assasination", "outlaw", "subtlety"],
)
shaman = wowclass(
    name="shaman",
    races=wowraces.shaman_races,
    healer_specs=["restoration"],
    zugger_specs=["elemental", "enhancement"],
)
warlock = wowclass(
    name="warlock",
    races=wowraces.warlock_races,
    zugger_specs=["affliction", "demonology", "destruction"],
)
warrior = wowclass(
    name="warrior",
    races=wowraces.warrior_races,
    tank_specs=["protection"],
    zugger_specs=["arms", "fury"],
)

tank_classes = [death_knight, demon_hunter, druid, monk, paladin, warrior]
healer_classes = [druid, evoker, monk, paladin, priest, shaman]
zuggger_classes = [
    death_knight,
    demon_hunter,
    druid,
    evoker,
    hunter,
    mage,
    monk,
    paladin,
    priest,
    rogue,
    shaman,
    warlock,
    warrior,
]
all_classes = zuggger_classes
