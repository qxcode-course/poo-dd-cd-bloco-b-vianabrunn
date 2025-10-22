class Pessoa:
    def __init__(self, nome: str, dinheiro: int ):
        self.__nome = nome
        self.__din = dinheiro

    def get_nome (self):
        return self.__nome
    
    def get_din (self):
        return self.__din

    def __str__(self):
        return f'{self.__nome}:{self.__din}'

class Moto:
    def __init__(self, motorista: Pessoa, passageiro: Pessoa):
        self.__custo: int = 0
        self.__motorista = None
        self.__passageiro = None

    def get_custo (self):
        return self.__custo

    def get_motorista (self):
        return self.__motorista

    def get_passegeiro (self):
        return self.__passageiro

    def set_drive(self, motorista: Pessoa):
        if self.__motorista == None:
            self.__motorista = motorista
            return True
        else:
            return False


    def __str__(self):
        return f'Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}'




def main():
    moto = Moto("", "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str]= line.split()

        if args[0] == "end":
            break

        if args[0] == "show":
            print(moto)

        if args[0] == "setDriver":
            nome = args[1]
            din = int(args[2])
            motorista = Pessoa(nome, din)
            
            moto.set_drive(motorista)

    
main()

