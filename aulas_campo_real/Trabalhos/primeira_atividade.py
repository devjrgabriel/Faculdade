# Conjuntos
# 1. Crie um conjunto com os números de 1 a 10 e imprima o conjunto.
import time
import os


def finalizacao_do_sistema_de_conjuntos(timer):
    time.sleep(timer)
    os.system('cls')


def apresentacao_de_dados_de_conjunto(nome_do_conjunto):
    for elementos in nome_do_conjunto:
        print(elementos, end=' ')


conjunto_de_um_a_dez = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('Exercicio 01(Conjuntos) - Numeros de um a dez')

apresentacao_de_dados_de_conjunto(conjunto_de_um_a_dez)
finalizacao_do_sistema_de_conjuntos(3)

''' 2. Crie dois conjuntos, um com os números de 1 a 5 e outro com os números de
 3 a 7. Imprima a união, a interseção e a diferença simétrica dos conjuntos.'''
conjunto_de_um_a_cinco = {1, 2, 3, 4, 5}
conjunto_de_tres_a_sete = {3, 4, 5, 6, 7}

uniao = conjunto_de_um_a_cinco.union(conjunto_de_tres_a_sete)
interseccao = conjunto_de_um_a_cinco.intersection(conjunto_de_tres_a_sete)
diferenca = conjunto_de_um_a_cinco.difference(conjunto_de_tres_a_sete)

print('Exercicio 02(Conjuntos) - União, Intersecção e Diferença.  ')
print('\nConjunto 01:')
apresentacao_de_dados_de_conjunto(conjunto_de_um_a_cinco)
print('\nConjunto 02:')
apresentacao_de_dados_de_conjunto(conjunto_de_tres_a_sete)


print('\n\nA união dos itens: ')
apresentacao_de_dados_de_conjunto(uniao)
print('\nA intersecção dos itens: ')
apresentacao_de_dados_de_conjunto(interseccao)

print('\nA diferença dos itens: ')
apresentacao_de_dados_de_conjunto(diferenca)
finalizacao_do_sistema_de_conjuntos(6)

''' 3. Crie um conjunto com as vogais (a, e, i, o, u) e peça ao usuário para digitar
uma palavra. Imprima as vogais que aparecem na palavra digitada.'''
conjunto_de_vogais = {'a', 'e', 'i', 'o', 'u'}
vogais_que_apareceram = set()

print('Exercicio 03(Conjuntos) - Verificação de vogais.  ')
palavra_digitada = input('Digite a palavra: ').lower()

for i in palavra_digitada:
    if i in conjunto_de_vogais:
        vogais_que_apareceram.add(i)

print('Vogais que apareceram:')
apresentacao_de_dados_de_conjunto(vogais_que_apareceram)
finalizacao_do_sistema_de_conjuntos(3)

''' 4. Crie dois conjuntos com nomes de frutas e verifique se há alguma fruta em
 comum entre os conjuntos.'''

conjunto_de_frutas_um = {'melao', 'banana'}
conjunto_de_frutas_dois = {'laranja', 'banana'}
conjunto_de_frutas_iguais = conjunto_de_frutas_um.intersection(
    conjunto_de_frutas_dois)
print('Exercicio 04(Conjuntos) - Comparação de frutas.  ')
print('\nFrutas - Grupo 01:  ')
apresentacao_de_dados_de_conjunto(conjunto_de_frutas_um)

print('\n\nFrutas - Grupo 02:  ')
apresentacao_de_dados_de_conjunto(conjunto_de_frutas_dois)

print('\n\nFrutas que aparecem nos dois grupos:  ')
apresentacao_de_dados_de_conjunto(conjunto_de_frutas_iguais)
finalizacao_do_sistema_de_conjuntos(5)

# 5. Crie um conjunto com números inteiros aleatórios e imprima o maior e o
# menor número do conjunto.

numeros_aleatorios = {1, 2, 5, 8, 32, -1}
controle_atividade_cinco = 0
numero_maior = 0
numero_menor = 0
print('Exercicio 05(Conjuntos) - Numero maior e menor.  ')
print('Numeros recebidos:')
apresentacao_de_dados_de_conjunto(numeros_aleatorios)

for i in numeros_aleatorios:
    if controle_atividade_cinco < 1:
        numero_menor = i
        numero_maior = i

    if i > numero_maior:
        numero_maior = i
    if i < numero_menor:
        numero_menor = i
    controle_atividade_cinco += 1


print(f'\n\nO maior numero inserido = {numero_maior}')
print(f'\nO menor numero inserido = {numero_menor}')
finalizacao_do_sistema_de_conjuntos(4)

'''6. Crie um conjunto com as cores do arco-íris (vermelho, laranja, amarelo, verde,
azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor
digitada está no conjunto e imprima uma mensagem correspondente.
'''
conjunto_do_arco_iris = {'vermelho', 'laranja', 'amarelo', 'verde',
                         'azul', 'anil', 'violeta'}
print('Exercicio 06(Conjuntos) - Cores do Arco-iris  ')
cor_digitada = input('Digite sua cor: ').lower()

if cor_digitada in conjunto_do_arco_iris:
    print(f'A cor {cor_digitada} esta no arco-iris.')
else:
    print(f'A cor {cor_digitada} não esta no arco-iris.')

finalizacao_do_sistema_de_conjuntos(3)

'''7. Crie um conjunto com os dias da semana (segunda, terça, quarta, quinta,
sexta, sábado, domingo) e remova os dias úteis (segunda a sexta). Imprima o
conjunto resultante.'''

dias_da_semana = {'segunda', 'terça', 'quarta', 'quinta',
                  'sexta', 'sábado', 'domingo'}
print('Exercicio 07(Conjuntos) - Dias da semana  ')
print('\nApresentação de todos os dias da semana:')
apresentacao_de_dados_de_conjunto(dias_da_semana)
print('\n')

print('Removendo segunda...')
time.sleep(0.7)
print('Removendo terça...')
time.sleep(0.7)
print('Removendo quarta...')
time.sleep(0.7)
print('Removendo quinta...')
time.sleep(0.7)
print('Removendo sexta...')
time.sleep(0.7)
dias_da_semana.remove('segunda')
dias_da_semana.remove('terça')
dias_da_semana.remove('quarta')
dias_da_semana.remove('quinta')
dias_da_semana.remove('sexta')

print('\nApresentando Resultados restantes: ')
apresentacao_de_dados_de_conjunto(dias_da_semana)
finalizacao_do_sistema_de_conjuntos(3)

'''8. Crie um conjunto com os números de 1 a 20 e outro conjunto com os
números pares de 1 a 10. Imprima a diferença entre os dois conjuntos.
'''
conjunto_de_um_a_vinte = set()
conjunto_de_pares_de_1_a_10 = set()

print('Exercicio 08(Conjuntos) - verificação de conjunto de numeros. ')

for i in range(20):
    i += 1
    conjunto_de_um_a_vinte.add(i)
for i in range(10):
    i += 1
    if i % 2 == 0:
        conjunto_de_pares_de_1_a_10.add(i)

diferenca_dos_conjuntos = conjunto_de_um_a_vinte.difference(
    conjunto_de_pares_de_1_a_10)

print('\nConjunto de numeros até 20:')
apresentacao_de_dados_de_conjunto(conjunto_de_um_a_vinte)
print('\nConjunto de numeros pares até 10:')
apresentacao_de_dados_de_conjunto(conjunto_de_pares_de_1_a_10)
print('\nA diferença entre os dois conjuntos:')
apresentacao_de_dados_de_conjunto(diferenca_dos_conjuntos)
finalizacao_do_sistema_de_conjuntos(6)

'''9. Crie um conjunto com as notas de um aluno em uma disciplina e verifique se
ele foi aprovado (média 7) ou reprovado (média abaixo de 7).'''
notas = {1, 2, 3, 4}
total_notas = 0
print('Exercicio 09(Conjuntos) - verificar se esta aprovado ou reprovado. ')
print('\nAs suas notas por bimestre:')
for i in notas:
    print(i, end=' ')
    total_notas = + i
print('\n\nCalculando sua media... ')
time.sleep(2)
print('Verificando se esta aprovado ou reprovado...')
time.sleep(2)
media = total_notas/len(notas)
if media > 7:
    print('Você foi aprovado :)')
else:
    print('Você foi reprovado :(')
finalizacao_do_sistema_de_conjuntos(2)

'''10. Crie um conjunto com os números primos de 1 a 20 e verifique se um número
digitado pelo usuário está no conjunto.'''
numeros_primos = {2, 3, 5, 7, 11, 13, 17, 19}
loop_numeros_primos = True
numero_digitado_ex_10_int = 0
print('Exercicio 10(Conjuntos) - Numeros primos. ')
while loop_numeros_primos:
    numero_primo_digitado_valido = None
    numero_digitado_ex_10 = input('Digite o numero para verificação: ')
    try:
        numero_digitado_ex_10_int = int(numero_digitado_ex_10)
        numero_primo_digitado_valido = True
    except:
        print('Numero invalido. Digite um numero inteiro.')

    if numero_primo_digitado_valido is True:
        print('Numero digitado corretamente. Verificando...')
        time.sleep(2)
        if numero_digitado_ex_10_int in numeros_primos:
            print('O seu numero é primo.')
        else:
            print('O seu numero não é primo.')
        execucao_sistema_primos = input(
            'Deseja sair do sistema? [S]air ').lower().startswith('s')
        os.system('cls')
        if execucao_sistema_primos is True:
            loop_numeros_primos = False
finalizacao_do_sistema_de_conjuntos(2)

# Dicionários


def apresentacao_De_Dados_De_Didicionarios(nome_do_dicionario):
    for chave, valor in nome_do_dicionario.items():
        print(chave, ': ', valor)
        time.sleep(1)


def finalizacao_do_sistema_de_dicionarios(timer):
    time.sleep(timer)
    os.system('cls')


'''1. Crie um dicionário vazio e adicione duas chaves e valores a ele.
'''
print('Exercicio 01(Dicionarios) - Dicionarios Vazios. ')
dicionario_01 = {}

dicionario_01['Nome'] = 'Gabriel'
dicionario_01['Sobrenome'] = 'Souza'
print('Criando Chaves...')
time.sleep(1)
print('Adicionando Valores... ')
time.sleep(1)
print('Aqui esta seu Dicionario... ')
time.sleep(1)
apresentacao_De_Dados_De_Didicionarios(dicionario_01)
time.sleep(1)
finalizacao_do_sistema_de_dicionarios(5)

'''2. Crie um dicionário com as chaves nome, idade e cidade; e preencha com
seus dados. Imprima o dicionário.'''
dicionario_02_meus_dados = {
    'Nome': '',
    'Idade': 0,
    'Cidade': '',
}

print('Exercicio 02(Dicionarios) - Nome, Idade e Cidade. ')
nome_informado = input('Digite o seu nome: ').capitalize()
Idade_informada = int(input('Digite a sua idade: '))
Cidade_informada = input('Digite a sua cidade: ').capitalize()
print('Recebendo os dados... ')
time.sleep(1)
print('Armazenando os dados... ')
time.sleep(1)
print('Seu Dicionario com suas infomações = ')
time.sleep(1)
dicionario_02_meus_dados['Nome'] = nome_informado
dicionario_02_meus_dados['Idade'] = Idade_informada
dicionario_02_meus_dados['Cidade'] = Cidade_informada
apresentacao_De_Dados_De_Didicionarios(dicionario_02_meus_dados)
finalizacao_do_sistema_de_dicionarios(5)

'''3. Crie um dicionário com o nome e o preço de três produtos diferentes.
Imprima o dicionário.(verificar)'''
dicionario_03_nome_e_preco = {
    'nome_do_produto': ('a', 'b', 'c'),
    'valor_do_produto': ('1', '2', '3')

}
print('Exercicio 03(Dicionarios) - Nome e preço de produtos. ')
apresentacao_De_Dados_De_Didicionarios(dicionario_03_nome_e_preco)
finalizacao_do_sistema_de_dicionarios(3)

'''4. Crie um dicionário com o nome de três estados e suas respectivas capitais.
Peça ao usuário para digitar um estado e imprima a capital correspondente.'''


def verificacao_de_capital(estado):
    if estado == 'PR':
        mensagem = ('A capital é Curitiba')
    elif estado == 'SC':
        mensagem = ('A capital é Florianopolis')
    elif estado == 'RJ':
        mensagem = ('A capital é Rio De Janeiro')
    return mensagem


nome_dos_estados = {
    'nomes': ['PR', 'RJ', 'SC']
}
print('Exercicio 04(Dicionarios) - Estados e suas Capitais. ')

print('Estados listados: ')
for nome, lista in enumerate(nome_dos_estados['nomes']):
    print(lista, end=' ')

estado_digitado = input('\nDigite o estado: ').upper()
mensagem_estados = verificacao_de_capital(estado_digitado)
if estado_digitado in nome_dos_estados['nomes']:
    print(mensagem_estados)
else:
    print('Estado ditado incorretamente.')

finalizacao_do_sistema_de_dicionarios(3)
'''5. Crie um dicionário com o nome de cinco cidades e suas respectivas
populações. Imprima a cidade com a maior população.(fazer)'''
nome_da_cidade_e_populacao = {
    'cidade_01': 12,
    'cidade_02': 15,
    'cidade_03': 17,
    'cidade_04': 19,
    'cidade_05': 10,
}

print('Exercicio 05(Dicionarios) - Cidade e população. ')
print('Cidades e suas populações: ')
for i, valor in nome_da_cidade_e_populacao.items():
    print(i, valor, sep=' = ', end='      ')
    time.sleep(1)
maior_populacao = 0
nome_da_cidade = ''
for i, valor in nome_da_cidade_e_populacao.items():
    if valor > maior_populacao:
        nome_da_cidade = i
        maior_populacao = valor

print('\nA maior cidade e sua população: ')
time.sleep(2)
print(f'Nome Da cidade: {nome_da_cidade}')
print(f'População Da cidade: {maior_populacao}')
finalizacao_do_sistema_de_dicionarios(5)
'''6. Crie um dicionário com o nome de três alimentos e suas respectivas calorias.
Peça ao usuário para digitar um alimento e imprima a quantidade de calorias
correspondente.'''
dicionario_de_alimentos = {
    'alimentos_01': 'a',
    'alimentos_02': 'e',
    'alimentos_03': 'i',
    'calorias_alimento_01': 2,
    'calorias_alimento_02': 4,
    'calorias_alimento_03': 6
}
nome_dos_alimento = dicionario_de_alimentos['alimentos_01'] + \
    dicionario_de_alimentos['alimentos_02'] + \
    dicionario_de_alimentos['alimentos_03']

print('Exercicio 06(Dicionarios) - Alimentos e caloria. ')
print(f'Os Alimentos Disponiveis')
print(dicionario_de_alimentos['alimentos_01'],
      dicionario_de_alimentos['alimentos_02'], dicionario_de_alimentos['alimentos_03'])
alimento_digitado = input('Digite o alimento para saber a caloria: ').lower()

if alimento_digitado == dicionario_de_alimentos['alimentos_01']:
    caloria_alimentos_digitado = dicionario_de_alimentos['calorias_alimento_01']
    print(f'A caloria do alimento = {caloria_alimentos_digitado}')
elif alimento_digitado == dicionario_de_alimentos['alimentos_02']:
    caloria_alimentos_digitado = dicionario_de_alimentos['calorias_alimento_02']
    print(f'A caloria do alimento = {caloria_alimentos_digitado}')
elif alimento_digitado == dicionario_de_alimentos['alimentos_03']:
    caloria_alimentos_digitado = dicionario_de_alimentos['calorias_alimento_03']
    print(f'A caloria do alimento = {caloria_alimentos_digitado}')
else:
    print('Alimento indisponivel.')

finalizacao_do_sistema_de_dicionarios(3)

'''7. Crie um dicionário com o nome de cinco animais e suas respectivas
classificações (mamífero, ave, réptil, etc.). Imprima apenas os nomes dos
animais.'''

dicionarios_dos_animais = {
    'animal1': 'mamífero',
    'animal2': 'ave',
    'animal3': 'réptil',
    'animal4': 'mamífero',
    'animal5': 'réptil'
}
print('Exercicio 07(Dicionarios) - Animais e suas especies. ')

print('Nome dos animais: ')
for chave, valor in dicionarios_dos_animais.items():
    print(chave, end=' ')
finalizacao_do_sistema_de_dicionarios(6)
'''8. Crie um dicionário com o nome de cinco países e suas respectivas bandeiras.
Imprima apenas os nomes dos países.'''
dicionarios_dos_paises = {
    'Pais 1': 'Bandeira1',
    'Pais 2': 'Bandeira2',
    'Pais 3': 'Bandeira3',
    'Pais 4': 'Bandeira4',
    'Pais 5': 'Bandeira5'
}
print('Exercicio 08(Dicionarios) - Paises e sua bandeira. ')

print('Nome dos Paises: ')
for chave, valor in dicionarios_dos_paises.items():
    print(chave, end=' | ')
finalizacao_do_sistema_de_dicionarios(6)
'''9. Crie um dicionário com o nome de cinco frutas e suas respectivas cores.
Imprima o nome de cada fruta seguido de sua cor.'''

frutas_e_sua_cor = {
    'Fruta 1': 'Cor 1',
    'Fruta 2': 'Cor 2',
    'Fruta 3': 'Cor 3',
    'Fruta 4': 'Cor 4',
    'Fruta 5': 'Cor 5'

}
print('Exercicio 09(Dicionarios) - Fruta e sua cor. ')

print('Nome da fruta e sua cor: ')
for chave, valor in frutas_e_sua_cor.items():
    print(chave, valor, sep=' = ', end=' | ')
finalizacao_do_sistema_de_dicionarios(5)

'''10. Crie um dicionário com o nome de três jogos e a quantidade de jogadores
necessária. Peça ao usuário para digitar um jogo e imprima a quantidade de
jogadores correspondente.'''
dicionario_dos_jogos = {
    'def': 123,
    'abc': 456,
    'tre': 789,

}
print('Exercicio 10(Dicionarios) - Jogos e seus Players. ')

print('Nome dos jogos: ')
for chave, valor in dicionario_dos_jogos.items():
    print(chave, end=' | ')
chaves = dicionario_dos_jogos.keys()
jogo_digitado = input('\nDigite o nome do jogo: ').lower()

if jogo_digitado in chaves:
    for chave, valor in dicionario_dos_jogos.items():
        if jogo_digitado == chave:
            print(f'O numero de jogadores = {valor}')
finalizacao_do_sistema_de_dicionarios(3)

'''Tuplas
1. Crie uma tupla com os números de 1 a 5 e imprima a tupla.'''
tupla_ex_01 = (1, 2, 3, 4, 5)
print('Exercicio 01(Tuplas) - tupla de 01 a 05. ')

for i in tupla_ex_01:
    print(i, end=' | ')

finalizacao_do_sistema_de_conjuntos(4)
'''2. Crie uma tupla com os nomes de três países e imprima o segundo elemento
da tupla.'''
print('Exercicio 02(Tuplas) - Nome de tres paises. ')
nome_dos_paises = ('abc', 'def', 'ghi')
print(f'Segundo pais inserido: {nome_dos_paises[1]}')
finalizacao_do_sistema_de_conjuntos(4)
'''3. Crie uma tupla com os valores de uma conta de restaurante (valor da
refeição, taxa de serviço e valor total). Imprima a tupla.'''
tupla_restaurante = (135, 13.2, 148.2)
print('Exercicio 03(Tuplas) - conta de um restaurante. ')
print(f'O valor da refeição: {tupla_restaurante[0]}')
print(f'O valor da taxa de serviço: {tupla_restaurante[1]}')
print(f'O valor total da refeição: {tupla_restaurante[2]}')
finalizacao_do_sistema_de_conjuntos(5)

'''4. Crie uma tupla com os nomes de cinco pessoas e peça ao usuário para
digitar um número entre 1 e 5. Imprima o nome correspondente ao número
digitado.'''
tupla_cinco_pessoas = ('nome01', 'nome02', 'nome03', 'nome04', 'nome05')
print('Exercicio 04(Tuplas) - Posições de uma tupla. ')

posicao_digitada = int(input('Digite um numero de 1 a 5: '))
posicao_digitada -= 1
print(f'A posição pertence a {tupla_cinco_pessoas[posicao_digitada]}')
finalizacao_do_sistema_de_conjuntos(5)
'''5. Crie uma tupla com as notas de um aluno em uma disciplina e imprima a
média das notas.'''
tupla_media_de_aluno = (1, 3, 5, 7)
print('Exercicio 05(Tuplas) - Media de um aluno. ')
totais_notas = 0
print('Notas inseridas: ')
for i in tupla_media_de_aluno:
    totais_notas += i
    print(i, end=" | ")
media_da_nota = totais_notas/len(tupla_media_de_aluno)
print(f'\nA media do aluno é = {media_da_nota}')

finalizacao_do_sistema_de_conjuntos(5)
'''6. Crie uma tupla com as cores do arco-íris (vermelho, laranja, amarelo, verde,
azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor
digitada está na tupla e imprima uma mensagem correspondente.'''
print('Exercicio 06(Tuplas) - Cor do arco iris. ')

tupla_arco_iris = ('vermelho', 'laranja', 'amarelo', 'verde',
                   'azul', 'anil', 'violeta')
cor_Digitada_tupla = input('Digite a cor para verificação: ').lower()
if cor_Digitada_tupla in tupla_arco_iris:
    print('A cor pertence ao arco iris')
else:
    print('A cor nao pertence ao arco iris')
finalizacao_do_sistema_de_conjuntos(5)

'''7. Crie uma tupla com as temperaturas de uma semana (sete dias) e imprima a
temperatura máxima e mínima da semana.'''
tupla_temperatura_da_semana = (3, 5, 2, 8, 6, 1, 3)
temperatura_maior = 0
temperatura_menor = 0
controle_tupla_07 = 0
print('Exercicio 07(Tuplas) - Temperatura de uma semana. ')
for i in tupla_temperatura_da_semana:
    if controle_tupla_07 < 1:
        temperatura_menor = i
        temperatura_maior = i
    if i > temperatura_maior:
        temperatura_maior = i
    if i < temperatura_menor:
        temperatura_menor = i

    controle_tupla_07 += 1
print(f'A maior temperatura esta semana foi = {temperatura_maior}')
print(f'A menor temperatura esta semana foi = {temperatura_menor}')
finalizacao_do_sistema_de_conjuntos(4)
'''8. Crie uma tupla com os nomes de cinco frutas e suas respectivas cores.
Imprima o nome de cada fruta seguido de sua cor.'''
tupla_cinco_frutas = ('fruta01', 'cor01', 'fruta02', 'cor02',
                      'fruta03', 'cor03', 'fruta04', 'cor04', 'fruta05', 'cor05')
controle_tupla_08 = 0
tamanho_tupla = len(tupla_cinco_frutas)
repeticoes = int(tamanho_tupla/2)
print('Exercicio 08(Tuplas) - Frutas e suas cores. ')

for i in range(repeticoes):
    print(f'\nNOME DA FRUTA = {tupla_cinco_frutas[controle_tupla_08]}', end='')
    controle_tupla_08 += 1
    for i in range(1):
        print(
            f'\nCOR DA FRUTA = {tupla_cinco_frutas[controle_tupla_08]}', end='')
        if controle_tupla_08 < len(tupla_cinco_frutas):
            controle_tupla_08 += 1
finalizacao_do_sistema_de_conjuntos(4)

'''9. Crie uma tupla com os números de 1 a 10 e outra tupla com os números de 5
a 15. Imprima a interseção entre as duas tuplas.'''
tupla_numeros_de_um_a_dez = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla_numeros_de_cinco_a_quinze = (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
interseccao_das_tuplas = []
for i in tupla_numeros_de_um_a_dez:
    if i in tupla_numeros_de_cinco_a_quinze:
        interseccao_das_tuplas.append(i)


print(f'A intersecção das tuplas:')
for i in interseccao_das_tuplas:
    print(i, end=' | ')
finalizacao_do_sistema_de_conjuntos(4)

'''10. Crie uma tupla com as letras do alfabeto e uma segunda tupla com as vogais.
Imprima a diferença entre as duas tuplas.
'''
tupla_alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
tupla_vogais = ('a', 'e', 'i', 'o', 'u')
diferenca_das_tuplas_vogais = []
for i in tupla_alfabeto:
    if i not in tupla_vogais:
        diferenca_das_tuplas_vogais.append(i)


print(f'A diferenca das tuplas:')
for i in diferenca_das_tuplas_vogais:
    print(i, end=' | ')
