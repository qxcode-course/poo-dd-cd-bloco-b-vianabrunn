class Relogio:
    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.__h = 0
        self.__m = 0
        self.__s = 0
        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

    def set_hora(self, valor: int):
        if 0 <= valor <= 23:
            self.__h = valor
        else:
            print("fail: hora invalida")

    def set_minuto(self, valor: int):
        if 0 <= valor <= 59:
            self.__m = valor
        else:
            print("fail: minuto invalido")

    def set_segundo(self, valor: int):
        if 0 <= valor <= 59:
            self.__s = valor
        else:
            print("fail: segundo invalido")

    def get_hora(self):
        return self.__h

    def get_minuto(self):
        return self.__m

    def get_segundo(self):
        return self.__s

    def nextSecond(self):
        self.__s += 1
        if self.__s > 59:
            self.__s = 0
            self.__m += 1
            if self.__m > 59:
                self.__m = 0
                self.__h += 1
                if self.__h > 23:
                    self.__h = 0

    def __str__(self):
        return f"{self.__h:02d}:{self.__m:02d}:{self.__s:02d}"


def main():
    hora = Relogio()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()

        if args[0] == "show":
            print(hora)

        elif args[0] == "set":
            h, m, s = int(args[1]), int(args[2]), int(args[3])
            hora.set_hora(h)
            hora.set_minuto(m)
            hora.set_segundo(s)

        elif args[0] == "init":
            h, m, s = int(args[1]), int(args[2]), int(args[3])
            hora = Relogio()
            hora.set_hora(h)
            hora.set_minuto(m)
            hora.set_segundo(s)

        elif args[0] == "next":
            hora.nextSecond()

        elif args[0] == "end":
            break
main()