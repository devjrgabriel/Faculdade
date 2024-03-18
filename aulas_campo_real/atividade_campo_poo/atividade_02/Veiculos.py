'''Herança de Veículos:
Crie uma classe Veiculo com atributos como tipo e velocidade e, 
em seguida, crie classes Carro e Moto que herdem de Veiculo.

Exercício 4: Herança
Sobrescrevendo Métodos:
Na classe Veiculo, crie um método chamado descricao() que 
imprima uma descrição básica do veículo.
Sobrescreva esse método nas classes Carro 
e Moto para fornecer descrições específicas para cada tipo de veículo.
'''


class Veiculos():
    def __init__(self, tipo_do_veiculo, velocidade_do_veiculo):
        self._tipo_do_veiculo = tipo_do_veiculo
        self._velocidade_do_veiculo = velocidade_do_veiculo

    def DadosMostrar(self):
        print(
            f'Tipo = {self._tipo_do_veiculo} Velocidade = {self._velocidade_do_veiculo} ')


class Motos(Veiculos):
    def __init__(self, tipo_do_veiculo, velocidade_do_veiculo):
        super().__init__(tipo_do_veiculo, velocidade_do_veiculo)

    def Alterar(self, objeto):
        tipo_do_veiculo = input('Qual o tipo do veiculo? ')
        velocidade_do_veiculo = input('Qual a velocidade do veiculo? ')
        self._tipo_do_veiculo = tipo_do_veiculo
        self._velocidade_do_veiculo = velocidade_do_veiculo

        print(
            f'O tipo do veiculo é {self._tipo_do_veiculo} e a velocidades é {self._velocidade_do_veiculo}')


class Carro(Veiculos):
    def __init__(self, tipo_do_veiculo, velocidade_do_veiculo):
        super().__init__(tipo_do_veiculo, velocidade_do_veiculo)

    def Alterar(self, objeto):
        tipo_do_veiculo = input('Qual o tipo do veiculo? ')
        velocidade_do_veiculo = input('Qual a velocidade do veiculo? ')
        self._tipo_do_veiculo = tipo_do_veiculo
        self._velocidade_do_veiculo = velocidade_do_veiculo

        print(
            f'O tipo do veiculo é {self._tipo_do_veiculo} e a velocidades é {self._velocidade_do_veiculo}')


Carro01 = Carro('Porsche', '2022')
Moto01 = Motos('Tiguer', '2024')

Carro01.DadosMostrar()
Carro01.Alterar(Carro01)
