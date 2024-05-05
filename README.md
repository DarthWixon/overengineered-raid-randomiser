# Overengineered Raid Randomiser
This code is a massively overengineered way to generate
a random raid, taking into account player preferences.

## Installation
All these instructions are \*nix based cos I don't have windows. A guildmate
has tested it on windows and apparently it works just fine.

Get the code: 

`git clone git@github.com:DarthWixon/overengineered-raid-randomiser.git`

Get the requirements installed:

```bash
cd overengineered-raid-randomiser
pip install -r reqs.txt
```
You can make a venv if you'd like, but there aren't many requirements. I assume you know how if you care.


## Usage
To try it out, just run `python main.py` inside your installation folder. This will generate
a sample output like the one below.

To pass in your own raid team, you can either modify the given `example_players.yaml` file, or write your
own (I hope the format is self-explanatory - you need quotes where I've put them!) and pass it to the 
programme with the `-p` command line argument like so:

`python main.py -p <custom-player-file>.yaml`

To get your own guild name involved, use the `-g` option (if your guild name contains spaces
you need to wrap it in quotation marks): 

`python main.py -p <custom-player-file>.yaml -g <"Guild Name">`

If you want to restrict your raid to only the Alliance or Horde you could just ban all the
races in the config file, but for convenience you can use the `-A` command line flag to
generate an alliance raid, and the `-H` flag to generate a horde raid. If you pass both of
them you'll get a horde raid - behaviour I'm not changing so don't ask.

`python main.py -p <custom-player-file>.yaml -g <"Guild Name"> -H`

Finally, if you'd like your output to be repeatable (for the same inputs), you can pass
a specific random seed with the `-s` flag. For example, to generate the sample raid below
you can run `python main.py -s 42`.

### Sample Output
```
====================
Guild Name: The Bridgeburners
Number of Players: 10
Number of Tanks: 2
Number of Healers: 2
Number of Zuggers: 6
====================
Tank Players:
====================
Player Name: Fiddler
Role: Tank
Character: Troll Brewmaster Monk
==========
Player Name: Mallet
Role: Tank
Character: Worgen Protection Warrior
==========
Healer Players:
====================
Player Name: Detoran
Role: Healer
Character: Tauren Restoration Druid
==========
Player Name: Whiskeyjack
Role: Healer
Character: Lightforged Draenei Holy Paladin
==========
Zugzug Players:
====================
Player Name: Quick Ben
Role: Zugger
Character: Dracthyr Devastation Evoker
==========
Player Name: Kalam
Role: Zugger
Character: Void Elf Survival Hunter
==========
Player Name: Picker
Role: Zugger
Character: Mag'Har Orc Shadow Priest
==========
Player Name: Hedge
Role: Zugger
Character: Human Frost Mage
==========
Player Name: Sorry
Role: Zugger
Character: Lightforged Draenei Frost Death Knight
==========
Player Name: Blend
Role: Zugger
Character: Kul Tiran Balance Druid
==========
```
