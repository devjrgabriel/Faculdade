import re
import random


def escrever_arquivo_aleatorio(qnt_de_numeros, nome_do_arquivo):
    arquivo_novo = open(nome_do_arquivo, 'w')
    for i in range(qnt_de_numeros):
        num01 = str(random.randint(1, 200))
        num02 = str(random.randint(0, 255))
        num03 = str(random.randint(0, 269))
        num04 = str(random.randint(0, 300))

        arquivo_novo.write(num01)
        arquivo_novo.write('.')
        arquivo_novo.write(num02)
        arquivo_novo.write('.')
        arquivo_novo.write(num03)
        arquivo_novo.write('.')
        arquivo_novo.write(num04)

        arquivo_novo.write('\n')

    arquivo_novo.close()


# escrever_arquivo_aleatorio(1, 'ip_originais.txt')


def verificacao_de_ip(arquivo_com_ip):
    arquivoips = open(arquivo_com_ip, 'r')
    for i in arquivoips:
        for n in i:
            if n != '.':

                print(n)


verificacao_de_ip("ip_originais.txt")


def validar_endereco_ip(ip):
    # Verifica se o endereço IP está no formato correto
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if not re.match(ip_pattern, ip):
        return False

    # Divide o endereço IP em partes
    partes = ip.split('.')

    # Verifica se o primeiro número está no intervalo válido
    if not 1 <= int(partes[0]) <= 255:
        return False

    # Verifica se os outros números estão no intervalo válido
    for num in partes[1:]:
        if not 0 <= int(num) <= 255:
            return False

    return True


def separar_ips_validos_e_invalidos(arquivo_entrada, arquivo_ips_validos, arquivo_ips_invalidos):
    with open(arquivo_entrada, 'r') as arquivo:
        ips = arquivo.read().splitlines()

    ips_validos = []
    ips_invalidos = []

    for ip in ips:
        if validar_endereco_ip(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

    # Escreve os IPs válidos e inválidos em arquivos separados
    with open(arquivo_ips_validos, 'w') as arquivo_validos:
        arquivo_validos.write('\n'.join(ips_validos))

    with open(arquivo_ips_invalidos, 'w') as arquivo_invalidos:
        arquivo_invalidos.write('\n'.join(ips_invalidos))


# Exemplo de uso da função
separar_ips_validos_e_invalidos(
    'lista_ips.txt', 'ips_validos.txt', 'ips_invalidos.txt')
