class Pessoa:
    def __init__(self):
        self.__nome = None
        self.__estado = True
        self.__idade = None

    def getNome(self):
        return self.__nome

    def setNome(self, novoNome):
        self.__nome = novoNome

    def getIdade(self):
        return self.__idade

    def setIdade(self, novaIdade):
        self.__idade = novaIdade

    def dormindo(self):
        self.__estado = False
        print(self.__estado, 'Esta dormindo')

    def acordado(self):
        self.__estado = True
        print(self.__estado, 'Esta acordado')

Fulano = Pessoa ()
Fulano.setNome('Tito')
Fulano.setIdade(18)
Fulano.acordado()


print(Fulano)
print()
print(Fulano.getNome())
print(Fulano.getIdade())

