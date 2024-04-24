import random

from main import RANDOM_SEED
from wowclass import healer_classes, tank_classes, zuggger_classes

random.seed(RANDOM_SEED)


class wowrole:
    def __init__(self, name, classes, tank_flag=False, healer_flag=False):
        self.name = name
        self.classes = classes
        self.tank_flag = tank_flag
        self.healer_flag = healer_flag

    def roll_class(self, banned_classes):
        choice = random.choice(self.classes)
        if choice in banned_classes:
            return self.roll_class(banned_classes)
        else:
            return choice


tank = wowrole(name="tank", classes=tank_classes, tank_flag=True)
healer = wowrole(name="healer", classes=healer_classes, healer_flag=True)
zugger = wowrole(name="zugger", classes=zuggger_classes)
