class wowplayer:
    def __init__(self, name, banned_roles, banned_classes, banned_races):
        self.name = name
        self.banned_roles = banned_roles
        self.banned_classes = banned_classes
        self.banned_races = banned_races
        self.assigned_role = None
        self.assigned_class = None
        self.assigned_race = None
        self.assigned_spec = None

    @classmethod
    def from_dict(cls, player_dict):
        return cls(
            name=player_dict["name"],
            banned_roles=player_dict["banned_roles"],
            banned_classes=player_dict["banned_classes"],
            banned_races=player_dict["banned_races"],
        )

    def assign_role(self, assigned_role):
        self.assigned_role = assigned_role

    def roll_class(self):
        self.assigned_class = self.assigned_role.roll_class(self.banned_classes)
        self.assigned_spec = self.assigned_class.roll_spec(self.assigned_role)

    def roll_race(self, horde_only=False, alliance_only=False):
        self.assigned_race = self.assigned_class.roll_race(
            self.banned_races, horde_only=horde_only, alliance_only=alliance_only
        )

    def pretty_print(self):
        divider_string = "=========="
        player_string = (
            f"""Player Name: {self.name.title()}
Role: {self.assigned_role.name.title()}
Character: {self.assigned_race.title()} {self.assigned_spec.title()} {self.assigned_class.name.title()}
"""
            + divider_string
        )
        print(player_string)
