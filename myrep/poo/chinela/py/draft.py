class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, valor: int):
        if  valor >= 20 and valor <=50 and valor %2 == 0:
            self.__tamanho = valor
            
    
chinela = Chinela ()
        
while chinela.getTamanho() == 0:
    print("Digite seu temanho de chinela")
    tamanho = int(input())
    chinela.setTamanho(tamanho)
            
print("Parabens, voce comprou uma chinela tamanho", chinela.getTamanho())