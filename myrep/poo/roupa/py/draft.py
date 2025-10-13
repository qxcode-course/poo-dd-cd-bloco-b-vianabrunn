class Roupa:
    def __init__(self, size: str):
        self.__tamanho = ""

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor:str):
        if valor == "PP" or valor == "P" or valor=="M" or valor=="G" or valor =="GG" or valor=="XG":
            self.__tamanho = valor
            
        else: 
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

    def __str__(self):
        return f"size: ({self.__tamanho})"
    
def main():
    roupa = Roupa("")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "show":
            print(roupa)
        if args[0] == "size":
            valor = args[1]
            roupa.setTamanho(valor)
        if args[0] == "end":
            break
        
main()