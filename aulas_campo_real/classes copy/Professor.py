from Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def saudar(self):
        return f'OLA, EU SOU O PROFESSOR {self.nome}'
