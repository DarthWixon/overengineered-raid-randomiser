import random

import wowerrors
from wowrole import healer, tank, zugger

role_list = [tank, healer, zugger]


# this makes it not random each time
# lets see if anyone notices
random.seed(42069)


class wowraid:
    def __init__(self, name, gamers):
        self.name = name
        self.gamers = gamers
        self.num_gamers = len(self.gamers)
        self.choose_comp()

    def choose_comp(self):
        self.num_tanks = 2
        if self.num_gamers < 14:
            self.num_healers = 2
        elif self.num_gamers < 18:
            self.num_healers = 3
        else:
            self.num_healers = 4
        self.num_zuggers = self.num_gamers - (self.num_tanks + self.num_healers)

    def assign_roles(self):
        self.assigned_tanks = []
        self.assigned_healers = []
        self.assigned_zuggers = []
        self.unassigned_gamers = self.gamers.copy()
        random.shuffle(self.unassigned_gamers)
        # assign tanks
        for gamer in self.unassigned_gamers:
            if tank not in gamer.banned_roles:
                self.assigned_tanks.append(gamer)
                self.unassigned_gamers.remove(gamer)
            if len(self.assigned_tanks) == self.num_tanks:
                break
        if len(self.assigned_tanks) < self.num_tanks:
            raise wowerrors.NotEnoughTanksError("You need more players to tank.")

        # assign healers
        for gamer in self.unassigned_gamers:
            if healer not in gamer.banned_roles:
                self.assigned_healers.append(gamer)
                self.unassigned_gamers.remove(gamer)
            if len(self.assigned_healers) == self.num_healers:
                break
        if len(self.assigned_healers) < self.num_healers:
            raise wowerrors.NotEnoughHealersError("You need more players to heal.")

        # assign DPS
        self.assigned_zuggers = self.unassigned_gamers

        for t in self.assigned_tanks:
            t.assign_role(tank)
        for h in self.assigned_healers:
            h.assign_role(healer)
        for z in self.assigned_zuggers:
            z.assign_role(zugger)

    def assign_classes(self):
        for gamer in self.gamers:
            gamer.roll_class()

    def assign_races(self):
        for gamer in self.gamers:
            gamer.roll_race()

    def pretty_print(self):
        divider_string = "===================="
        intro_string = (
            f"""
Guild Name: {self.name}
Number of Players: {self.num_gamers}
Number of Tanks: {self.num_tanks}
Number of Healers: {self.num_healers}
Number of Zuggers: {self.num_zuggers}
"""
            + divider_string
        )

        tank_string = (
            """
Tank Players:
"""
            + divider_string
        )

        healer_string = (
            """
Healer Players:
"""
            + divider_string
        )

        zugger_string = (
            """
Zugzug Players:
"""
            + divider_string
        )

        print(intro_string)
        print(tank_string)
        for gamer in self.assigned_tanks:
            gamer.pretty_print()
        print(healer_string)
        for gamer in self.assigned_healers:
            gamer.pretty_print()
        print(zugger_string)
        for gamer in self.assigned_zuggers:
            gamer.pretty_print()
