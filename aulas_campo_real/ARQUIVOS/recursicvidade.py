
# fatorial de 5

# no primeiro momento ira fazer a puxada da função
def fatorial(numero):
    # caso base
    if numero == 1:
        return 1
    # chamada recursiva
    return numero * fatorial(numero-1)


print(fatorial(5))

# após inciara as tentativas de numero == 1
# ele vai apresentar o teste fatorial(5) = 5 * fatorial (5 - 1)
# apos ira armazenar o valor = 5
# ele vai apresentar o teste fatorial(5) = 5 * fatorial (4 - 1)
# apos ira armazenar o valor = 4
# ele vai apresentar o teste fatorial(5) = 5 * fatorial (3 - 1)
# apos ira armazenar o valor = 3
# ele vai apresentar o teste fatorial(5) = 5 * fatorial (2 - 1)
# apos ira armazenar o valor = 2
# ele vai apresentar o teste fatorial(5) = 5 * fatorial (1)
# apos ira armazenar o valor = 1
# apos isso ira verificar os valores anteriores e multiplicara
