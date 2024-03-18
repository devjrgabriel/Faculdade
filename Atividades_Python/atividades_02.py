import os
import time

'''1. Escreva uma função recursiva em Python que calcule a soma dos primeiros N
números inteiros positivos.'''


def soma_dos_numeros(numero):
    # Caso base
    if numero <= 0:
        return 0
    # chamada recursiva
    return numero + soma_dos_numeros(numero - 1)


numero_digitado = int(input('Digite um Numero para somar ele: '))

somas = soma_dos_numeros(numero_digitado)
print(F'A SOMA DOS NUMEROS É {somas}')
time.sleep(4)
os.system('cls')

'''2. Escreva uma função recursiva para calcular o número fatorial de um número inteiro
positivo.'''


def fatorial_de_numero_x(numero):
    # caso base
    if numero <= 1:
        return 1
    return numero*fatorial_de_numero_x(numero-1)


numero_digitado_fatorial = int(input('Digite um Numero para fatoração: '))
fatoracao = fatorial_de_numero_x(numero_digitado_fatorial)
print(F'A FATORAÇÃO DOS NUMEROS É {fatoracao}')
time.sleep(4)
os.system('cls')

'''3. Escreva uma função que use uma pilha para inverter uma string.'''


def funcao_para_inverter_string(palavra):
    return palavra[::-1]


palavra_digitada = input('Digite a palavra para inversão: ')
palavra_invertida = funcao_para_inverter_string(palavra_digitada)

print(f'A palavra invertida fica "{palavra_invertida}"')
time.sleep(4)
os.system('cls')
'''4. Escreva uma função que converte um número decimal em sua representação binária
usando uma pilha.'''

pilha_de_numero_binario = []


def numero_decimal_para_binario(numero, pilha):
    if numero < 2:

        pilha.append(int(numero))
        return numero
    else:
        pilha.append(int(numero % 2))
    numero = numero/2
    int(numero)
    return numero_decimal_para_binario(numero, pilha)


def apresentacao_de_pilha(pilha):
    print('Segue o numero decimal em binario: ')
    for i in pilha:
        print(i, end='')


numero_decimal = float(input('Digite um numero para converter para binario: '))

numero_inteiro = int(numero_decimal)

numero_binario = numero_decimal_para_binario(
    numero_inteiro, pilha_de_numero_binario)

apresentacao_de_pilha(pilha_de_numero_binario)
time.sleep(4)
os.system('cls')
'''
5. Implemente um histórico de comandos de um editor de texto simples usando uma
pilha. A cada vez que um comando é executado, ele é adicionado à pilha.
Implemente a capacidade de desfazer um comando usando a pilha.'''

lopp_ex_5 = True
numero_correto = False
comandos = []


def apresentacao_de_comando(lista):
    for i in lista:
        print(i, end='  |  ')


while lopp_ex_5:
    escolha_menu = 0
    print('Menu inicial: ')
    print('[1] INSERIR ')
    print('[2] EXCLUIR ULTIMO COMANDO ')
    print('[3] VIZUALIZAR ')
    print('[4] SAIR ')
    escolha_menu = input('Digite o numero de sua opção: ')
    try:
        escolha_menu = int(escolha_menu)
        numero_correto = True
    except:
        print('Digite um numero...')
        print('Reniciando...')
        time.sleep(2)
        os.system('cls')

    if numero_correto is True:
        time.sleep(1)
        os.system('cls')
        if escolha_menu == 1:
            inserir_comando = input('Digite o comando para inserir: ')
            comandos.append(inserir_comando)
            print('Inserindo Comando... ')
            time.sleep(2)
            print('Inserido...')
        elif escolha_menu == 2:
            print('Deletando ultimo item... ')
            time.sleep(2)
            print('Deletado...')
            comandos.pop()
        elif escolha_menu == 3:
            print('Apresentação de comandos: ')
            apresentacao_de_comando(comandos)
        elif escolha_menu == 4:
            print('Saindo do sistema... ')
            lopp_ex_5 = False

    time.sleep(2)
    os.system('cls')
