import os
lista = []

while True:
    print('Selecione um opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('valor: ')
        lista.append(valor)
    elif opcao == 'a':
        pass
    elif opcao == 'l':
        pass
    else:
        pass
