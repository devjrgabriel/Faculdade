from abc import ABC, abstractclassmethod


class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractclassmethod
    def saudar(self):
        pass
