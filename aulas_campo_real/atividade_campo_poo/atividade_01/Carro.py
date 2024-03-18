'''
Atividade 01
Classe Básica com Encapsulamento:
Crie uma classe chamada Carro com atributos encapsulados (_modelo e _ano) e métodos para obter e definir esses atributos.
'''


class Carro:
    def __init__(self, modelo, ano):
        self._modelo = modelo
        self._ano = ano

    def DadosMostrar(self):
        print(f'modelo = {self._modelo} ano = {self._ano} ')

    def Buzinar(self):
        print(f'A marca {self._modelo} ano {self._ano} buzina.')

    def Alterar(self, objeto):
        modelonovo = input('Qual o novo modelo? ')
        anonovo = input('Qual o ano do modelo? ')
        self.__modelo = modelonovo
        self.__ano = anonovo

        print(f'O novo modelo é {self.__modelo} e o ano é {self.__ano}')


class CarroObjeto(Carro):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)


Carro01 = CarroObjeto('Porsche', '2022')
Carro02 = CarroObjeto('BMW', '2024')

Carro01.Buzinar()
Carro02.Buzinar()


'''
Atividade 02 
Protegendo Dados com Encapsulamento:
Modifique a classe Carro do exercício anterior para usar atributos privados (__modelo e __ano) 
e métodos de acesso para obter e definir esses atributos.
'''

Carro01.Alterar(Carro01)
Carro01.DadosMostrar()
