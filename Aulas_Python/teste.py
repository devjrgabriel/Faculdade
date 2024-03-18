print(10*'🦕')
print(100*'🦈')

somar_numeros = []


def somar_com_recursividade(lista, parametro):
    # caso base
    if parametro > 1:
        return lista.append(parametro)
    # chamado recursiva
    return lista


argumento = int(input("Digite o seu numero: "))

print(f'A soma dos numeros é {somar_com_recursividade(argumento)}')
