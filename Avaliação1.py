class triangulo:
    def __init__(self):
        self.LadoA = None
        self.LadoB = None
        self.LadoC = None

    def perim(self):
        perim = self.LadoA + self.LadoB + self.LadoC
        return perim

    def getMaiorLado(self):
     return self.__MaiorLado

    def getArea(self):
        return self.perim()
