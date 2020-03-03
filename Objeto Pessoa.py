class Pessoa:
    def __init__(self):
        self.__nome = None
        self.__cpf = None
        self.__altura = None



    def getAltura(self):
       return self.__altura

    def setAltura(self, novaAltura):
       self.__altura = novaAltura

    def getNome(self):
        return self.__nome

    def setNome(self, novoNome):
        self.__nome = novoNome

    def getCpf(self):
        return self.__cpf

    def setCpf(self, novoCpf):
        self.__cpf = novoCpf

fulano = Pessoa ()
fulano.setNome('Juvenal')
fulano.setCpf(123)


cicrano = Pessoa()
cicrano.setNome('Juvenal')
cicrano.setCpf(3321)


print(fulano)
print(cicrano)
print()
print(fulano.getNome())
print(cicrano.getNome())
