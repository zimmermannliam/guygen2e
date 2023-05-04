from enum import Enum

SUCCESS = 0
QUIT = 1
ERR = 2

def mon_q(argc: int, argv: [str]) -> int:
    return QUIT
    

def mon_help(argc: int, argv: [str]) -> int:
    for name, (_, desc) in cmds.items():
        print(f"{name}:\t{desc}")
    return SUCCESS

cmds = {
    "help"      : (mon_help, "This command"),
    "q"         : (mon_q, "Quit")

}
