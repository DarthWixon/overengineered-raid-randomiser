from pathlib import Path

import yaml

from wowclass import all_classes
from wowplayer import wowplayer
from wowraces import all_races
from wowraid import wowraid
from wowrole import healer, tank, zugger

role_list = [tank, healer, zugger]


def gamers_from_yaml(yaml_path):
    gamer_list = []
    with open(yaml_path, "r") as file:
        player_doc = yaml.safe_load_all(file)

        for player in player_doc:
            gamer = {}
            gamer["name"] = player["name"]
            gamer["banned_roles"] = []
            for role in role_list:
                if role.name in player["banned_roles"]:
                    gamer["banned_roles"].append(role)
            gamer["banned_classes"] = []
            for charclass in all_classes:
                if charclass.name in player["banned_classes"]:
                    gamer["banned_classes"].append(charclass)
            gamer["banned_races"] = []
            for race in all_races:
                if race in player["banned_races"]:
                    gamer["banned_races"].append(race)

            gamer_list.append(wowplayer.from_dict(player_dict=player))

    return gamer_list


def assign_roles(raid_group: wowraid):
    raid_group.assign_roles()


def roll_classes(raid_group: wowraid):
    raid_group.assign_classes()


def roll_races(raid_group: wowraid):
    raid_group.assign_races()


def print_raid_comp(raid_group: wowraid):
    raid_group.pretty_print()


def main():
    player_yaml = "players.yaml"
    raid = wowraid(name="Based on What", gamers=gamers_from_yaml(player_yaml))
    assign_roles(raid)
    roll_classes(raid)
    roll_races(raid)
    print_raid_comp(raid)


if __name__ == "__main__":
    main()
