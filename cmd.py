from enum import Enum
from char import char_random
import dice
from state import State


SUCCESS = 0
QUIT = 1
ERR = 2



def mon_quit(argc: int, argv: [str], state: State) -> int:
    """ Quit the program using the QUIT return flag"""
    return QUIT
    

def mon_help(argc: int, argv: [str], state: State) -> int:
    """ Print help list"""
    for name, (_, desc) in cmds.items():
        print(f"{name}:\t{desc} ", end="")
        synonyms = [k for k,v in cmd_alt_names.items() if v == name]
        if synonyms:
            print(f"({', '.join(synonyms)})", end="")
        print()
            
    return SUCCESS


def mon_newcharacter(argc: int, argv: [str], state: State) -> int:
    """ Make a new character and add it to state.chars"""
    nchar = 1
    if argc > 1:
        nchar = int(argv[1])
    for i in range(nchar):
        state.chars.append(char_random())
    return SUCCESS


def mon_displaycharacters(argc: int, argv: [str], state: State) -> int:
    """ Display all characters in a list"""
    print(f"name       g race\tstr dex con int wis cha \ttrait")
    for char in state.chars:
        print(f"{char.name:<11}{char.gender} {char.race}\t", end="")
        for s in char.stat:
            print(f"{s:3n} ", end="")
        print("\t", end="")
        print(char.trait, end="")
        print()


def mon_roll(argc: int, argv: [str], state: State) -> int:
    """ Roll a dice """
    if argc != 3:
        print("Bad args")
        return ERR
    print(dice.ndx(int(argv[1]), int(argv[2])))


cmd_alt_names = {
    "h"     : "help",
    "q"     : "quit",
    "nc"    : "newcharacter",
    "dc"    : "displaycharacters",
    "r"     : "roll"
}

cmds = {
    "help"          : (mon_help, "This command"),
    "quit"          : (mon_quit, "Quit the program"),
    "newcharacter"  : (mon_newcharacter, "Create a new character"),
    "displaycharacters" : (mon_displaycharacters, "Display all characters in state"),
    "roll"          : (mon_roll, "(2 args) Roll ndx")
}
