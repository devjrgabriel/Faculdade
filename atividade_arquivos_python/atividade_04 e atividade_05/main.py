import random


def escrever_arquivo_aleatorio(qnt_de_numeros, nome_do_arquivo):
    arquivo_novo = open(nome_do_arquivo, 'w')
    for i in range(qnt_de_numeros):
        nota01 = str(random.randint(0, 10))
        nota02 = str(random.randint(0, 10))
        arquivo_novo.write(nota01)
        arquivo_novo.write(' ')
        arquivo_novo.write(nota02)
        arquivo_novo.write('\n')

    arquivo_novo.close()


# escrever_arquivo_aleatorio(20, 'notas.txt')


def criar_arquivos_de_media(arquivos_notas, arquivo_novo):
    numeros = open(arquivos_notas, "r")
    arquivo_media = open(arquivo_novo, "w")
    for notas in numeros:
        media = 0
        notas_separadas = notas.split()

        for i in notas_separadas:
            nota_convertida = int(i)
            media += nota_convertida
        media = media/2

        media = str(media)
        arquivo_media.write(media)
        arquivo_media.write("\n")

    arquivo_media.close()
    numeros.close()


# criar_arquivos_de_media('notas.txt', 'medias.txt')

def criar_arquivo_final(arquivos_com_nomes, arquivos_com_medias, arquivo_final):
    nomes = open(arquivos_com_nomes, 'r')
    notas = open(arquivos_com_medias, 'r')
    arquivo_com_nome_e_nota = open(arquivo_final, 'w')
    for i in range(20):
        nome = str(nomes.readline())
        media = str(notas.readline())
        print(f"NOME: {nome}")
        print(f"MEDIA: {media}")
        arquivo_com_nome_e_nota.write(f'Nome = {nome} Media = {media}')
    nomes.close()
    notas.close()
    arquivo_com_nome_e_nota.close()


# criar_arquivo_final('nomes.txt', 'medias.txt', 'nome_media.txt')

def alterar_segunda_nota(arquivos_com_nomes, arquivos_com_notas, arquivos_com_novas_notas):
    nomes = open(arquivos_com_nomes, 'r')
    notas = open(arquivos_com_notas, 'r')
    notas_alteradas = open(arquivos_com_novas_notas, 'w')

    for n in notas:
        notas_separadas = n.split()
        notas_separadas.pop()
        notas_separadas.append(str(random.randint(0, 10)))
        notas_convertidas = str(notas_separadas)
        notas_alteradas.write(notas_convertidas)
        notas_alteradas.write('\n')

    nomes.close()
    notas.close()
    notas_alteradas.close()


def formatar_lista(arquivos_com_notas, arquivo_formatado):
    str1 = ""
    numeros_validos = '1234567890 '
    formatacao = open(arquivos_com_notas, 'r')
    alteracao = open(arquivo_formatado, 'w')
    for n in formatacao:
        for i in n:
            if i in numeros_validos:
                str1 += i
            elif i == ']':
                alteracao.write(str1)
                alteracao.write('\n')
                str1 = ""

    alteracao.close()
    formatacao.close()


""" 
alterar_segunda_nota('nomes.txt', 'notas.txt', 'novas_notas.txt')
formatar_lista("novas_notas.txt", "arquivo_formatado.txt")
criar_arquivos_de_media('arquivo_formatado.txt', 'medias.txt')
criar_arquivo_final('nomes.txt', 'medias.txt', 'nome_media.txt')
 """
