#!/usr/bin/env python3

import random

def dice_player():
    number_user = random.randint(1, 10)
    print(f"The player did: {number_user}")
    return number_user

def dice_monster():
    number_monster = random.randint(1, 10)
    print(f"The monster did: {number_monster}")
    return number_monster

def dmg_compare():
    while(1):
        monster_roll = dice_monster()
        player_roll = dice_player()

        if monster_roll > player_roll:
            print("The monster won")
            return False
        elif monster_roll < player_roll:
            print("The player slayed the monster")
            return True


if __name__ == "__main__":
    dmg_compare()
