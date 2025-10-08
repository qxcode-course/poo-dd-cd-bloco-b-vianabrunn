class Camisa:
    def __init__(self, tamanho:str):
        self.__tamanho = tamanho

    def getTamanho(self) ->str:
        return self.__tamanho
    
    def setTamanho (self, valor: str):
        if valor == "PP" or valor =="P" or valor=="M" or valor=="G" or valor =="GG" or valor=="XG":
            self.__tamanho = valor 
    
camisa = Camisa("")

while camisa.getTamanho() == "":
    tamanho = input("Digite seu tamanho de blusa: ")
    camisa.setTamanho(tamanho)

print("Parabens, você comprou uma roupa tamanho", camisa.getTamanho())