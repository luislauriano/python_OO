class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.acordado = True

    def fazNiver(self):
        self.idade = self.idade + 1

    def dormir(self):
        self.acordado = False
        print(self.nome + 'esta dormindo')

    def acordado(self):
        self.acordado = True
        print(self.nome + 'Acordou')


pessoa1 = Pessoa('Juvenal', 22, 333)
print(pessoa1.idade)
pessoa1.fazNiver()
print(pessoa1.idade)
print(pessoa1.acordado)