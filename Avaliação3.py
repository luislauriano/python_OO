class Aluno:
    def __init__(self):
        self.nome = None
        self.curso = None
        self.tempoSemDormir = None

    def estudar(self):
        horas = int(input('Quantidade de horas de estudo: '))
        self.tempoSemDormir += horas


    def dormir(self):
        self.tempoSemDormir = 0


