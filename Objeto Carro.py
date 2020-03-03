class Carro:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__anoFabricacao = ano
        self.__velocidade = 0

    #Encapsulamento
    #def getMarca(self):
        #return self.__marca
    #def setMarca(self, novaMarca):
        #self.__marca = novaMarca

    #def getMode(self):
        #return self.__modelo
    #def setModelo(self, novoModelo):
        #return self.__modelo = novoModelo

    #def getAnoFabricacao(self):
        #return self.__anoFabricacao
    #def setNovoAno(self, novaFabricacao):
        #return self.__anoFabricacao = novaFabricacao

    def getVelocidade(self):
        return self.__velocidade
    def setVelocidade(self):
        self.__velocidade = velocidade

    def acelerar(self):
        self.__velocidade += 10

    def freiar(self):
        self.__freiar -= 10

    def exibirStatus(self):
        status = f'modelo: {self.__modelo} velocidade: {self.__velocidade}'
        return status

golzinho = Carro()
golzinho.setMarca('Vol')
golzinho.setModelo('G1')
golzinho.setAnoFabricacao(19)
print(golzinho.exibirStatus())
golzinho.freiar()
print(golzinho.getMarca())







