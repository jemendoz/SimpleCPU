from simplecpu import CPU
from os import name as osname, system
from os.path import exists

def clear():
    if osname == "nt":
        system("cls")
    elif osname == "posix":
        system("clear")

def main() -> None:
    wait:bool = True

    cpu = CPU()

    print("Que programa quieres ejecutar? (ubicado en /programs)")
    progname = input("Programa: ")

    if not exists(f"programs/{progname}"):
        print("El programa indicado no existe...")
        return

    cpu.load_prog(f"programs/{progname}")

    print("Escoge las direcciones de memoria a visualizar (separadas por comas)")
    memaddr = [ x.lstrip().rstrip() for x in input("Direcciones: ").split(",") ]
    
    while True:
        clear()

        cpu.print_state(memaddr)
        if cpu.state == "halt":
            break
        cpu.do_cycle()

        if wait:
            inp = input("[Enter] para un ciclo, [S] para finalizar, [X] para salir: ")
            if inp.lower() == "s":
                wait = False
            if inp.lower() == "x":
                break

    print("FIN DEL PROGRAMA")
    

if __name__=="__main__":
    main()