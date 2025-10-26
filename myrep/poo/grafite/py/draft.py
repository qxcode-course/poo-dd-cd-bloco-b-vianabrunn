class Grafite:
    def __init__(self, calibreG: float, dureza: str, size: int):
        self.__calibreG = calibreG
        self.__dureza = dureza
        self.__size = size

    def get_size(self):
        return self.__size

    def get_calibreG(self):
        return self.__calibreG 

    def get_dureza(self):
        return self.__dureza


class Pencil:
    def __init__(self, calibre: float, grafite: Grafite | None):
        self.__calibre = calibre
        self.__grafite = grafite

    def get_calibre(self):
        return self.__calibre

    def get_grafite(self): 
        return self.__grafite



    def insert (self, grafite: Grafite):
        if self.__grafite != None:
            print("fail: ja existe grafite")
            return
        lif self.__calibre == grafite.get_calibreG():
            self.__grafite = gerafite

        else: 
            print("fail: calibre incompativel")

    def remove (self):
        self.__grafite = None 
 


    def __str__(self):
        if self.__grafite != None:
            return f'calibre: {self.__calibre}, grafite: [{self.__grafite.get_calibreG()}:{self.__grafite.get_dureza()}:{self.__grafite.get_size()}]'
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
            pencil = Pencil(calibre, None)
        if args[0] == "show":
            print(pencil)
        if args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            size = int(args[3]) 
            grafite = Grafite(calibre, dureza, size)
            pencil.insert(grafite)
        if args[0] == "remove":
            pencil.remove()
            



main()


