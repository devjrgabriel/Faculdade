def escrever_arquivo_aleatorio(qnt_de_numeros, nome_do_arquivo):
    arquivo_novo = open(nome_do_arquivo, 'w')
    for i in range(qnt_de_numeros):
        arquivo_novo.write(str(random.randint(0, 20)))
        arquivo_novo.write('\n')
        arquivo_novo.write('//nao copiar')
        arquivo_novo.write('\n')

    arquivo_novo.close()


def copiaArquivo(velhoArquivo, novoArquivo):
    f1 = open(velhoArquivo, "r")
    f2 = open(novoArquivo, "w")
    for texto in f1:
        frase = str(texto).startswith('//')
        if not frase:
            f2.write(texto)
    f1.close()
    f2.close()


copiaArquivo("arquivo01.txt", "arquivo02.txt")
