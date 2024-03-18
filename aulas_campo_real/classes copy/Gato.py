from Animal import Animal


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, especie="gato")
        self.cor = cor

    def abrirporta(self):
        print(f"{self.nome} abre porta.")

    def emitirsom(self):
        print(f'{self.nome} faz miau.')

    def arranhar(self):
        print(f'{self.nome} arranha.')

    def alimentar(self, alimento, alimento01):
        print(f"{self.nome} come {alimento} e {alimento01}")
