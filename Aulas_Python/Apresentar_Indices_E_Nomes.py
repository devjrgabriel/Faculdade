# definição de variaveis
name = 'Gabriel souza'
index = 0
new_name = ''

# condicional para fazer enquanto indice for menor que o tamanho do nome
while index < len(name):
    # criação de uma nova variavel para receber a letra atual
    letter = name[index]
    # criação da variavel novo_nome e incrementando novo_nome + letra atual + *
    new_name += f'*{letter}'
    # controle do while para alterar o indice
    index += 1
# novo nome recebe * para fechar a*b*c'*'<- este ultimo teste *
new_name += '*'
print(new_name)
