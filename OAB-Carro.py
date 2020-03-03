class Carro:
    #Definindo os Atributos
    def __init__ (self, marca, modelo, anoFabricacao):
       self.marca = marca
       self.modelo = modelo
       self.anoFabricacao = anoFabricacao

c1 = Carro('Ford', 'Fiesta', 2019)

print(c1.marca + ' - ' + c1.modelo)

c1.modelo = 'Fusca'

print(c1.marca + ' - ' + c1.modelo)


