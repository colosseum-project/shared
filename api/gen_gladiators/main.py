import os
import sys
import requests
from random import randint

HOST = "localhost"
PORT = "8081"
GLADIATORS_COUNT = 20

script_root = os.path.dirname(os.path.abspath(sys.argv[0]))

with open(os.path.join(script_root, "latin_names.txt")) as f:
    latin_names = f.readlines()
latin_names_count = len(latin_names)

gladiator_types = ("MURMILLO", "THRAEX", "DIMACHAERUS")
gladiator_types_count = len(gladiator_types)

for i in range(GLADIATORS_COUNT):
    requests.post(
        url=f"http://{HOST}:{PORT}/gladiators",
        json={
            "name": latin_names[randint(0, latin_names_count - 1)].replace("_", " "),
            "type": gladiator_types[randint(0, gladiator_types_count - 1)],
        },
    )
