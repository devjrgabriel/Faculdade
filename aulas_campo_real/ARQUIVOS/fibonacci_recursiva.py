def fibonatti(posicao):
    if posicao == 0:
        return 0
    elif posicao == 1:
        return 1
    else:
        return fibonatti(posicao - 1) + fibonatti(posicao-2)


def tribonacci(posicao):
    if posicao == 0:
        return 0
    elif posicao == 1:
        return 0
    elif posicao == 2:
        return 1
    else:
        return tribonacci(posicao - 1) + tribonacci(posicao-2) + tribonacci(posicao-3)


pos = int(input('digite a posição: '))

print(fibonatti(pos))
print(tribonacci(pos))
