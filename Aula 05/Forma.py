import math


class Forma:

    def calcula_area(self):
        pass


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcula_area(self):
        return round((math.pi * self.raio) ** 2, 2)


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcula_area(self):
        return self.largura * self.altura


circulo = Circulo(5)
retangulo = Retangulo(10, 20)

print(f'A área do círculo é de {circulo.calcula_area()} e a área do retângulo é de {retangulo.calcula_area()}.')
