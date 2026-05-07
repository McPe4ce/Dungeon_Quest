#!/usr/bin/env python3

def start_choice():
    start = input("Do you want to enter the dungeon ? (yes/no) \n")
    return start

def next_choice():
    print("What do you want to do?")
    print("1. Enter the next room.")
    print("2. Quit and go cry in your mom's basement.")
    choice = input("Enter your choice: \n")
    return choice

def restart_choice():
    restart = input("Do you want to restart the game ? (yes/no) \n")
    return restart

def search_choice():
    search = input("Do you want to search the room ? (yes/no) \n")
    return search

