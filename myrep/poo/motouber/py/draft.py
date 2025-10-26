class Pessoa:
    def __init__(self, nome: str, dinheiro: int ):
        self.__nome = nome
        self.__din = dinheiro

    def get_nome (self):
        return self.__nome
    
    def get_din (self):
        return self.__din

    def crediar(self, valor: int):
        if self.__din > valor:
            self.__din -= valor
            return
        else:
            self.__din = 0
            return

    def debitar(self, valor: int):
        self.__din += valor

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

    def set_drive_m (self, motorista: Pessoa):
        if self.__motorista == None:
            self.__motorista = motorista
            return True
        else:
            return False

    def set_drive_p (self, passageiro: Pessoa):
        if self.__passageiro == None:
            self.__passageiro = passageiro
            return True
        else:
            return False
            
    def drive(self, valor: int):
        if self.__motorista != None and self.__passageiro != None:
            self.__custo += valor

    def leavePass(self):
        if self.__passageiro == None:
            return

        elif self.__passageiro.get_din() < self.__custo:
            print("fail: Passenger does not have enough money")
            self.__passageiro.crediar(self.__custo)
            self.__motorista.debitar(self.__custo)
            print(f'{self.__passageiro} left')
            self.__custo = 0
            self.__passageiro = None
        
        else:
            
            self.__passageiro.crediar(self.__custo)
            self.__motorista.debitar(self.__custo)
            print(f'{self.__passageiro} left')
            self.__passageiro = None
            self.__custo = 0    
            

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
            
            moto.set_drive_m(motorista)

        if args[0] == "setPass":
            nome = args[1]
            din = int(args[2])
            passageiro = Pessoa(nome, din)
            
            moto.set_drive_p(passageiro)

        if args[0] == "drive":
            din = int(args[1])
            moto.drive(din)

        if args[0] == "leavePass":
            moto.leavePass()
            
            

    
main()

