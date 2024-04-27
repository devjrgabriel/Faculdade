import random
import os
import time


def escrever_idade_aleatorio(qnt_de_numeros, nome_do_arquivo):
    arquivo_numero = open(nome_do_arquivo, 'w')
    for i in range(qnt_de_numeros):
        arquivo_numero.write(str(random.randint(0, 20)))
        arquivo_numero.write('\n')

    arquivo_numero.close()


def escrever_altura_aleatorio(qnt_de_numeros, nome_do_arquivo):
    arquivo_numero = open(nome_do_arquivo, 'w')
    for i in range(qnt_de_numeros):
        arquivo_numero.write(str(random.randint(160, 190)))
        arquivo_numero.write('\n')

    arquivo_numero.close()


escrever_altura_aleatorio(20, 'altura.txt')


def gerar_nomes_aleatorios(qnt_de_numeros, arquivos_com_nomes, arquivos_com_sobrenomes, arquivo_com_idades, arquivo_com_altura):
    nomes = open(arquivos_com_nomes, 'r')
    sobrenomes = open(arquivos_com_sobrenomes, 'r')
    idades = open(arquivo_com_idades, 'r')
    alturas = open(arquivo_com_altura, 'r')
    for i in range(qnt_de_numeros):
        nome = str(nomes.readline())
        sobrenome = str(sobrenomes.readline())
        idade = str(idades.readline())
        altura = str(alturas.readline())
        print(f"NOME: {nome}")
        print(f"SOBRENOME:{sobrenome}")
        print(f"IDADE: {idade}")
        print(f"ALTURA: {altura}")
        time.sleep(2)
        os.system('cls')
    nomes.close()
    sobrenomes.close()
    idades.close()
    alturas.close()


gerador_De_numeros = int(input("Digite um valor: "))
gerar_nomes_aleatorios(gerador_De_numeros, 'nomes.txt',
                       'sobrenomes.txt', 'idade.txt', 'altura.txt')
