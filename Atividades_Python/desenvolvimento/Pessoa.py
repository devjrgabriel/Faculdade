class Pessoa:
    # construtor
    def __init__(self, nome, idade, refeicao=False, comunicacao=False):
        self._nome = nome
        self._idade = idade
        self._refeicao = refeicao
        self._comunicacao = comunicacao
    # get

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def refeicao(self):
        return self._refeicao

    @property
    def comunicacao(self):
        return self._comunicacao

    # set

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @idade.setter
    def idade(self, nome):
        self._idade = idade

    @refeicao.setter
    def nome(self, nome):
        self._refeicao = refeicao

    @comunicacao.setter
    def comunicacao(self, nome):
        self._comunicacao = comunicacao

    # metodos
    def falar(self, assunto):
        if self._refeicao:
            print(f'{self._nome} não pode falar de boca cheia!!')
            return

        if self._comunicacao:
            print(f'{self._nome} ja esta falando!')
            return
        print(f'{self._nome} esta falando sobre {assunto}.')
        self._comunicacao = True

    def pararFala(self):
        if not self.comunicacao:
            print(f'{self._nome} não esta falando')
            return
        print(f'{self.nome} pare de falar')
        self._comunicacao = False

    def comer(self, alimento):
        if self._refeicao:
            print(f'{self._nome} não pode comer.')
            return
        if self._comunicacao:
            print(f'{self._nome} não pode comer falando')
            return
        print(f'{self._nome} pode come {alimento}')
        self._refeicao = True

    def pararComer(self):
        if not self._refeicao:
            print(f'{self._nome} não esta comendo')
            return
        print(f'{self._nome} pare de comer')
        self._refeicao = False
