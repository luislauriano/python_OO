from Carro import Carro
from Moto import Moto

class Pessoa:
    def __init__(self):
        self.nome = None
        self.carro = None
        self.motos = []

    def comprouMoto(self, moto):
        self.motos.append(moto)
    def exibir(self):
      print(f'O nome é {self.nome} e tem um carro da marca {self.carro.marca}')

p1 = Pessoa()
p1.nome = 'Joao'

moto1 = Moto()
moto1.modelo = 'Bros'
moto2 = Moto()
moto2.modelo = 'Biz'


carroJoao = Carro()
carroJoao.marca = 'Ford'
carroJoao.cor = 'Azul'
carroJoao.modelo = 'Focus'

p1.carro = carroJoao
p1.comprouMoto(moto1)
p1.comprouMoto(moto2)

p1.exibir()

for moto in p1.motos:
    print(moto.modelo)
