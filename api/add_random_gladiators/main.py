import os
import sys
import argparse
from random import randint

try:
    import requests
except ImportError:
    print(
        "Missing 'requests' module, "
        "please run `python -m pip install requests` to install it."
    )
    raise

parser = argparse.ArgumentParser(description="Add randomly-named gladiators to Ludus.")
parser.add_argument(
    "host", default="localhost", type=str, help="Hostname of targeted Ludus service"
)
parser.add_argument(
    "-p", "--port", default="8081", type=int, help="Port of targeted Ludus service"
)
parser.add_argument(
    "-n", "--number", default="20", type=int, help="Number of gladiator to add"
)

args = parser.parse_args()

script_root = os.path.dirname(os.path.abspath(sys.argv[0]))
latin_names_file = os.path.join(script_root, "latin_names.txt")
latin_names = open(latin_names_file, "r").read().splitlines()
latin_names_count = len(latin_names)
gladiator_types = ("MURMILLO", "THRAEX", "DIMACHAERUS")
gladiator_types_count = len(gladiator_types)
for i in range(args.number):
    gladiator = {
        "name": latin_names[randint(0, latin_names_count - 1)],
        "type": gladiator_types[randint(0, gladiator_types_count - 1)],
    }
    r = requests.post(
        url=f"http://{args.host}:{args.port}/gladiators",
        json=gladiator,
    )
    if r.status_code == 200:
        print(
            f"{gladiator['type'].capitalize()} {gladiator['name']}",
            "has been added to Ludus",
        )
    else:
        raise requests.RequestException(
            f"Could not add gladiator(s), returns error code {r.status_code}."
        )
