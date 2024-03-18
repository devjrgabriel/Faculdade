import random


def escrever_numero_aleatorio(qnt_de_numeros, nome_do_arquivo):
    arquivo_numero = open(nome_do_arquivo, 'w')
    for i in range(qnt_de_numeros):
        arquivo_numero.write(str(random.randint(0, 100)))
        arquivo_numero.write('\n')

    arquivo_numero.close()


def escrever_media(qnt_de_numeros, nome_do_arquivo):
    arquivo_numero = open(nome_do_arquivo)
    soma = 0
    for i in range(qnt_de_numeros):
        num = float(arquivo_numero.readline())
        soma += num
        arquivo_numero.close()
        return soma/qnt_de_numeros


def copiar_arquivo(velho_arquivo, novo_arquivo):
    f1 = open(velho_arquivo, "r")
    f2 = open(novo_arquivo, "w")
    for texto in f1:
        f2.write(texto)
    f1.close()
    f2.close()


escrever_numero_aleatorio(100, 'aleatorio.txt')
escrever_numero_aleatorio(100, 'media.txt')
copiar_arquivo("media.txt", "teste.txt")
print(escrever_media(100, 'media.txt'))
print(escrever_media(100, 'teste.txt'))
