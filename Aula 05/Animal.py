class Animal:

    def nome(self, nome: str):
        self.nome = nome

    def especie(self, especie: str):
        self.especie = especie

    def emitir_som(self, som: str):
        self.som = som


class Cachorro(Animal):

    def raca(self, _raca: str):
        self._raca = _raca

    def obter_raca(self):
        return self._raca

    def emitir_som(self):
        return 'au au'


class Gato(Animal):

    def pelagem(self, _pelagem: str):
        self._pelagem = _pelagem

    def obter_pelagem(self):
        return self._pelagem

    def emitir_som(self):
        return 'miau'


Gatinho = Gato()
Doguinho = Cachorro()

Gatinho.nome('Fifi')
Doguinho.nome('Rex')

Gatinho.especie('Felis catus')
Doguinho.especie('Canis lupus familiaris')

Gatinho.pelagem('Pelo longo')
Doguinho.raca('Golden retriever')

print(Gatinho.emitir_som())
print(Doguinho.emitir_som())

print(Gatinho.obter_pelagem())
print(Doguinho.obter_raca())
