class Pessoa:
    def __init__(self, age:int , name:str):
        self.__age = age
        self.__name = name
    
    def getName(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def __str__(self):
        return f'{self.__name}:{self.__age}'

class Motoca:
    def __init__(self, potencia: int, time:int, pessoa: Pessoa):
        self.__potencia = potencia
        self.__time = time
        self.__pessoa = None

    
    def inserir(self, pessoa: Pessoa):
        if self.__pessoa != None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = pessoa
        return True
    

    
    def remover(self, pessoa: Pessoa):
        if self.__pessoa == None:
            print("fail: empty motorcycle")
            self.__pessoa = None
        else:
            print(pessoa)
        aux = self.__pessoa
        self.__pessoa = None
        return aux
    

    
    def buyTime(self, time: int):
        self.__time += time
        return self.__time
    

    
    def drive(self, time: int):
        if self.__time == 0:
            print("fail: buy time first")

        elif self.__pessoa == None:
            print("fail: empty motorcycle")


        elif self.__pessoa.get_age() > 10 :
            print("fail: too old to drive")
            
        elif time > self.__time:
            time -= self.__time
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0

        elif time <=0:
            print("fail: time finished after X minutes")

        else: 
            self.__time -= time
        return self.__time
    

    def honk(self):
        buzina = "P" + "e"* self.__potencia + "m"
        return f"{buzina}"
    
    def __str__(self):
        if self.__pessoa is None:
            return f"power:{self.__potencia}, time:{self.__time}, person:(empty)"
        else:
            return f"power:{self.__potencia}, time:{self.__time}, person:({self.__pessoa})"
    
def main():
    motoca = Motoca(1, 0, "")
    pessoa = Pessoa("", "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()
        
        if args[0] == "end":
            break

        if args[0] == "show":
            print(motoca)

        if args[0] == "enter":
            nome = args[1]
            idade = int(args[2])

            pessoa = Pessoa(idade, nome)
            motoca.inserir(pessoa)

        if args[0] == "init":
            potencia = int(args[1])
            motoca = Motoca(potencia, 0, None)

        if args[0] == "leave":
            motoca.remover(pessoa)
            
        if args[0] == "buy":
            time = int(args[1])
            motoca.buyTime(time)

        if args[0] == "drive":
            time = int(args[1])
            motoca.drive(time)

        if args[0] == "honk":
            print(motoca.honk())


main()

## o grafico ta assim pq eu tava fazendo no lugar errado e tive que copiar e colar aqui dps, dai meu processo se perdeu