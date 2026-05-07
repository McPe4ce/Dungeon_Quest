#!/usr/bin/env python3

import random
from combat import dmg_compare
from unittest.mock import patch

def equipment():
        loot = ["Sun Monocle", "T-shirt", "Gel fixation beton",
                "Deodorant AXE Protection MAX", "Nu Pieds",
                "Baguette Magique", "Go(de)urdin"]


        loot = random.choices(loot, k=1)

        print(f"Ay Ay, look what bro just got, a freaking {loot}")

def health_points(health):
        variation = dmg_compare()

        if variation == False:
                health -= 1
        return health
