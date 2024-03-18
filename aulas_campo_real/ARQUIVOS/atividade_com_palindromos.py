import os
import time
palavra_digitada = []
palavra_invertida = []
palavra_correta = []
palavra_correta_inversa = []


def push(pilha, item):
    pilha.append(item)


def palavra_quebrada(palavra, lista):
    for i in palavra:
        push(lista, i)
        print(i, end=' ')
    return lista


def inversao_da_palavra(lista_palavra, lista_para_inserir):
    for i in lista_palavra[::-1]:
        push(lista_para_inserir, i)

        print(i, end=' ')
    return palavra_invertida


def verificacao_Da_palavra(lista01, lista02, lista_para_colocar_correto, lista_para_colocar_inverso):
    for i in lista01:
        if ' ' == i:
            print('removendo espaço...')
            time.sleep(1)
        else:
            push(lista_para_colocar_correto, i)

    for i in lista02:
        if ' ' == i:

            time.sleep(1)
        else:
            push(lista_para_colocar_inverso, i)


palavra_informada = input('Digite sua palavra: ').lower()
time.sleep(1)
print('palavra correta: ')
palavra_quebrada(palavra_informada, palavra_digitada)

time.sleep(2)
print('\npalavra invertida: ')
inversao_da_palavra(palavra_digitada, palavra_invertida)

time.sleep(2)
print('\nVerificando a palavra:')
time.sleep(1)
verificacao_Da_palavra(palavra_digitada, palavra_invertida,
                       palavra_correta, palavra_correta_inversa)
if palavra_correta == palavra_correta_inversa:
    print('as palavras sao PALINDROMOS')
else:
    print('as palavras nao sao PALINDROMOS')
