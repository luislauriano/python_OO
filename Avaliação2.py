class Funcionario:
    def __init__(self):
        self.nome = None
        self.salario = None

    def aumentarSalario (self):
        self.salario + (self.salario * 10 / 100)

