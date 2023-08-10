class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_dados(self):
        print(f'Carro marca: {self.marca}, modelo: {self.modelo}.')


carro_1 = Carro('Ford', 'Edge')
carro_2 = Carro('Ford', 'Mustang')

carro_1.mostrar_dados()
carro_2.mostrar_dados()
