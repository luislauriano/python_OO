from veiculo import veiculo

#Classe Carro herdando da classe Veiculo

class Carro(Veiculo):
    def __init__(self):
        self.__qtdPortas = None

    def getQtdPortas(self):
        return self.qtdPortas

    def setQtdPortas(self, portas):
        self.qtdPortas = portas

