import cmd

def main():
    print("Welcome to guygen 2e! Type \"help\" for more information.")
    monitor()

def monitor(): 
    ret = None
    while ret != cmd.QUIT:
        cmd_str = input("> ")

        cmd_args = cmd_str.split()
        
        # whitespace input
        if not cmd_args:
            continue

        ret = cmd.cmds[cmd_args[0]][0](len(cmd_args), cmd_args)
    

if __name__ == "__main__":
    main()
