class CPU:
    def __init__(self) -> None:
        # CPU registers: A, B, C, TEST
        self.reg:dict[str:str] = {"A":None,"B":None,"C":None,"TEST":None}

        # Instruction register
        self.ir:list[str] = []

        # Program counter
        self.pc:int = 0

        #
        self.mem:dict[str:str] = dict()
        self.progmem:list[str] = list()

    def exec(self, inst:str, param:str|None = None):
        """
        exec() takes an instruction, and optionally a parameter, if the instructions needs, and executes
        the instruction. Full list of instructions on docs/instructions.md
        """
        match inst:
            case "LOADA":
                try:
                    self.reg["A"] = self.mem[param]
                except KeyError:
                    raise(IndexError("La direccion de memoria no existe / no esta inicializada"))

            case "LOADB":
                try:
                    self.reg["B"] = self.mem[param]
                except KeyError:
                    raise(IndexError("La direccion de memoria no existe / no esta inicializada"))

            case "LOADC":
                try:
                    self.reg["C"] = self.mem[param]
                except KeyError:
                    raise(IndexError("La direccion de memoria no existe / no esta inicializada"))

            case "CONA":
                self.reg["A"] = param

            case "CONB":
                self.reg["B"] = param

            case "CONC":
                self.reg["C"] = param

            case "SAVEA":
                self.mem[param] = self.reg["A"]

            case "SAVEB":
                self.mem[param] = self.reg["B"]

            case "SAVEC":
                self.mem[param] = self.reg["C"]

            case "ADD":
                self.reg["C"] = str(int(self.reg["A"]) + int(self.reg["B"]))

            case "SUB":
                self.reg["C"] = str(int(self.reg["A"]) - int(self.reg["B"]))

            case "MUL":
                self.reg["C"] = str(int(self.reg["A"]) * int(self.reg["B"]))

            case "DIV":
                self.reg["C"] = str(int(self.reg["A"]) / int(self.reg["B"]))

            case "COM":
                if int(self.reg["A"]) < int(self.reg["B"]):
                    self.reg["TEST"] = "<"
                elif int(self.reg["A"]) > int(self.reg["B"]):
                    self.reg["TEST"] = ">"
                else:
                    self.reg["TEST"] = "="

            case "JUMP":
                self.pc = int(param)

            case "JEQ":
                if self.reg["TEST"] == "=":
                    self.pc = int(param)

            case "JNEQ":
                if self.reg["TEST"] != "=":
                    self.pc = int(param)

            case "JG":
                if self.reg["TEST"] == ">":
                    self.pc = int(param)

            case "JGE":
                if self.reg["TEST"] == ">" or self.reg["TEST"] == "=":
                    self.pc = int(param)

            case "JL":
                if self.reg["TEST"] == "<":
                    self.pc = int(param)

            case "JLE":
                if self.reg["TEST"] == "<" or self.reg["TEST"] == "=":
                    self.pc = int(param)

            case "STOP":
                self.pc = -1

            case _:
                raise(ValueError(f"Instruccion ({inst}) no admitida."))

    def load_prog(self, filename:str):
        """
        Load a program onto progmem, for it to be executed
        """
        with open(filename,"r") as f:
            raw = f.read()

        lined = raw.split("\n")

        while "" in lined:
            lined.remove("")

        self.progmem = lined

    def do_cycle(self):
        """
        Does one CPU cycle: load, increment, execute
        """
        self.ir = self.progmem[self.pc].split(" ")
        self.pc += 1
        if len(self.ir) == 1:
            self.exec(self.ir[0])
        else:
            self.exec(self.ir[0], self.ir[1])

    def print_state(self,mem:list[str] = []):
        """
        Prints the state of the CPU. Add a list of memory addresses for them to be displayed.
        For example, to display memory addresses 120 and 130, print_state(["120","130"])
        """
        state = \
        f"""Registros:
        A:{self.reg['A']}
        B:{self.reg['B']}
        C:{self.reg['C']}
        TEST:{self.reg['TEST']}
        IR:{self.ir}
        PC:{self.pc}\n"""

        memstr = "Memoria:\n"

        for i in mem:
            try:
                memstr += f"        {i}: {self.mem[i]}\n"
            except KeyError:
                memstr += f"        {i}: Vacio...\n"

        print(state+memstr)