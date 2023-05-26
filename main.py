""" Main functionality for guygen, including monitor"""
import cmd

def main():
    """ Main for all guygen"""
    print("Welcome to guygen 2e! Type \"help\" for more information.")
    monitor()

def monitor():
    """ Run monitor in a loop, taking user input and running the corresponding cmd"""
    ret = None
    last_cmd = ""
    while ret != cmd.QUIT:
        cmd_str = input("> ")
        

        # whitespace input
        if cmd_str.strip() == "":
            continue
        
        # ! input
        temp_cmd = cmd_str
        if cmd_str.strip() == "!":
            cmd_str = last_cmd
        else:
            last_cmd = temp_cmd

        cmd_args = cmd_str.split()

        if cmd_args[0] in cmd.cmd_alt_names:
            cmd_args[0] = cmd.cmd_alt_names[cmd_args[0]]

        if cmd_args[0] in cmd.cmds:
            ret = cmd.cmds[cmd_args[0]][0](len(cmd_args), cmd_args)
        else:
            print("Error: Command not found")

if __name__ == "__main__":
    main()
