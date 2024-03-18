def somar_com_recursividade(parametro):
    # caso base
    if parametro == 1:
        return 1
    # chamado recursiva
    return parametro+somar_com_recursividade(parametro - 1)


argumento = int(input("Digite o seu numero: "))

print(f'A soma dos numeros é {somar_com_recursividade(argumento)}')
