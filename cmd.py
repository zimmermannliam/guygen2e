from enum import Enum
import char
from state import chars

SUCCESS = 0
QUIT = 1
ERR = 2

def mon_quit(argc: int, argv: [str]) -> int:
    """ Quit the program using the QUIT return flag"""
    return QUIT
    

def mon_help(argc: int, argv: [str]) -> int:
    """ Print help list"""
    for name, (_, desc) in cmds.items():
        print(f"{name}:\t{desc} ", end="")
        synonyms = [k for k,v in cmd_alt_names.items() if v == name]
        if synonyms:
            print(f"({', '.join(synonyms)})", end="")
        print()
            
    return SUCCESS

def mon_newcharacter(argc: int, argv: [str]) -> int:
    """ Make a new character and add it to state.chars"""
    global chars
    nchar = 1
    if argc > 1:
        nchar = int(argv[1])
    for i in range(nchar):
        chars.append(char.character_random())
    return SUCCESS

def mon_displaycharacters(argc: int, argv: [str]) -> int:
    """ Display all characters in a list"""
    print(f"name       g race\tstr dex con int wis cha \ttrait")
    for char in chars:
        
        print(f"{char.name:<11}{char.gender} {char.race}\t", end="")
        for s in char.stat:
            print(f"{s:3n} ", end="")
        print("\t", end="")
        print(char.trait, end="")
        print()

cmd_alt_names = {
    "h"     : "help",
    "q"     : "quit",
    "nc"    : "newcharacter",
    "dc"    : "displaycharacters"
}

cmds = {
    "help"          : (mon_help, "This command"),
    "quit"          : (mon_quit, "Quit the program"),
    "newcharacter"  : (mon_newcharacter, "Create a new character"),
    "displaycharacters" : (mon_displaycharacters, "Display all characters in state")

}
