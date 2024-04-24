# Overengineered Raid Randomiser
This code is a massively overengineered way to generate
a random raid. I made it during meetings to do the MoP Rewind.

## Usage
All these instructions are \*nix based cos I don't have windows.

`git clone git@github.com:DarthWixon/overengineered-raid-randomiser.git`

`cd overengineered-raid-randomiser`

You can make a venv if you'd like. I assume you know how if you care.

`pip install -r reqs.txt`

Run with `python main.py` to produce output using the supplied `example_players.yaml`.

Pass in your own `yaml` file by running:

`python main.py -p <path/to/your/yaml>`

Pass in your own random seed using the `-s` or `--seed` argument:

`python main.py -s 123456`
