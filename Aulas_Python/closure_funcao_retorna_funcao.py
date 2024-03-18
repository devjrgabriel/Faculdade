"""
Closure e funções que retornam outras funções
"""
# criação da função que recebera o dado


def criar_saudacao(saudacao):
    # aqui é aonde ira receber o segundo argumento que o nome
    def saudar(nome):
        # retornara f'bom dia' 'Gabriel'
        return f'{saudacao}, {nome}!'
    # retornara a função que retorna a mensagem
    return saudar


# neste momento é o recebimento da saudação
speak_good_morning = criar_saudacao('Bom dia')
speak_good_night = criar_saudacao('Boa noite')
# aqui é aonde é recebido os nome que ira retornar a mensagem
for name in ['Maria', 'Joana', 'Luiz']:
    print(speak_good_morning(name))
    print(speak_good_night(name))
