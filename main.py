#!/usr/bin/env python3

from combat import dmg_compare
from action import start_choice
from action import next_choice
from action import restart_choice
from action import search_choice

if __name__ == "__main__":
    print("Welcome to Dungeon Quest! ")
    start = start_choice()
    if start == "yes":
        print("Let's start your adventure!")
        alive = True
        while(alive):
            choice = next_choice()

            if choice == "1":
                print("You push the door and step into the next room.")
                print("The door closes behind you")
                print("Your face a ugly and really badly dressed Goblin!")
                fight_result = dmg_compare()
                if fight_result == False:
                    print("You die bitch!")
                    retry = restart_choice()
                    if retry == "yes":
                        print("Restarting the game...")
                        # We can add code here to reset the game state if needed
                    else:
                        print("Goodbye limp dick!")
                        alive = False
                else:
                    print("You defeated the Goblin!")

            elif choice == "2":
                print("You decide to quit and go cry in your mom's basement.")
                restart = restart_choice()
                if restart == "yes":
                    print("Restarting the game...")
                    # We can add code here to reset the game state if needed
                else:
                    print("Game over")
                    print("Goodbye limp dick!")
                    alive = False
    else:
        print("Ok, nice to meet you.. asshole")
