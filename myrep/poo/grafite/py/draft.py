class Grafite:
    def __init__(self, calibreG: float, dureza: str, size: int):
        self.__calibreG = calibreG
        self.__dureza = dureza
        self.__size = size

    def get_size(self):
        self.__size = size

    def get_calibreG(self):
        self.__calibreG = calibreG

    def get_dureza(self):
        self.__dureza = dureza


class Pencil:
    def __init__(self, calibre: float, grafite: Grafite | None):
        self.__calibre = calibre
        self.__grafite = None

    def get_calibre(self):
        self.__calibre = calibre
    
    def set_calibre(self, calibre: float):
        self.__calibre = calibre

    def get_calibre(self):
        self.__calibre = calibe()

    def get_grafite(self):
        self.__grafite = grafite

    def __str__(self):
        if self.__grafite != None:
            return f'calibre: {self.__calibre}, grafite: [{self.__calibre.get_calibreG()}:{self.__dureza.get_dureza()}:{self.__size.get_size()}] '
        else:
            return f'calibre: {self.__calibre}, grafite: null'
    

class main:
    pencil = Pencil(0.0, None)
    grafite = Grafite(0.0, " ", 0)
    while True:
        line = input()
        print("$"+ line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        if args[0] == "init":
            calibre = float(args[1])
            pencil.set_calibre(calibre)

        if args[0] == "show":
            print(pencil)


main()


