from Animal import Animal


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Cachorro")
        self.raca = raca

    def emitirsom(self):
        print(f"{self.nome} late.")

    def buscar(self):
        print(f"{self.nome} busca um bola.")

    def alimentar(self, alimento):
        print(f"{self.nome} come {alimento}")
