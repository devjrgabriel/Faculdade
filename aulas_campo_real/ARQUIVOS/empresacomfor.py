# 10 primeiros clientes com descontos
# 20% se for maior ou igual 1500
# 15% se for menor
# ler nome eo valor da compra
# calcular o desconto e
# apresentar junto com o nome desconte e o valor da compra
# total de desconto dado
import os

descontos_lista = []
valor_da_compra_lista = []
nome_dos_clientes_lista = []
desconto_total = 0
indice = 0

for indice in range(2):
    indice += 1
    nome_dos_clientes = input('Digite o seu nome: ')
    nome_dos_clientes_lista.append(nome_dos_clientes)
    valor_da_compra = float(input('Digite sua compra: R$'))
    valor_da_compra_lista.append(valor_da_compra)

    if valor_da_compra >= 1500:
        descontos = valor_da_compra * 0.20
        descontos_lista.append(descontos)

        print(f'o valor do desconto R${descontos}')
        desconto_total += descontos

    elif valor_da_compra >= 1:
        descontos = valor_da_compra * 0.15
        descontos_lista.append(descontos)

        print(f'o valor do desconto R${descontos}')
        desconto_total += descontos

    else:
        print('o valor é invalido')
        desconto_total += 0

os.system('clear')
print('Apresentação dos dados')

for nomes in range(len(nome_dos_clientes_lista)):
    print(f'O nome do cliente= R${nome_dos_clientes_lista[nomes]}')
    for valor_compra in valor_da_compra_lista:
        print(
            f'O valor da compra= R${valor_da_compra_lista[nomes]}')
        for desconto_dado in descontos_lista:
            print(
                f'O desconto da compra= R${descontos_lista[nomes]}')
    nomes += 1

print(f'O total de descontos = R${desconto_total}')
