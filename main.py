from simplecpu import CPU
from os import name as osname, system

def clear():
    if osname == "nt":
        system("cls")
    elif osname == "posix":
        system("clear")

def main() -> None:
    wait:bool = True

    cpu = CPU()
    cpu.load_prog("programs/fact.txt")
    
    while cpu.pc != -1:
        clear()
        cpu.print_state(["128","129"])
        cpu.do_cycle()
        if wait:
            inp = input("[Enter] to step, [S] to skip, [X] to exit")
            if inp.lower() == "s":
                wait = False
            if inp.lower() == "x":
                break

    print("PROGRAM END")
    

if __name__=="__main__":
    main()