class Animal:
    def falar(self): ...


class Cachorro(Animal):
    def falar(self):
        return 'au au'


class Gato(Animal):
    def falar(self):
        return 'miau'


def animal_falando(animal):
    print(animal.falar())


doguinho = Cachorro()
gatinho = Gato()

animal_falando(doguinho)
animal_falando(gatinho)
