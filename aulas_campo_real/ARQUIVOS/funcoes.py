""" def primeirafuncao():  # assinatura da função
    print('abc')


primeirafuncao()


def print_name(name):
    print(f'{name}, Good Night !!!')


name = input('What your name? ')

print_name(name)


def my_computer(cpu, memory, storage):
    print(f' ->{cpu=}\n ->{memory=}\n -> {storage=} !!!')


cpu = input('What your cpu? ')
memory = input('What your memory? ')
storage = input('What your storage? ')

my_computer(cpu, memory, storage)
 """

""" def soma_dos_valores(valor01, valor02):
    soma = valor01+valor02
    return soma


resultado = soma_dos_valores(1, 2)
print(f'a soma = {resultado}')
print(f'a soma == {soma_dos_valores(1,2)}')
 """
soma = 0
number_valid = None


def soma_dos_valores(valor_01, soma):
    for number in range(valor_01+1):
        soma += number
        print(f'A soma = {soma}')
    return (f'A soma dos valores é = {soma}')


while True:
    value_01_str = input('Digite o seu numero: ')

    try:
        value_01 = int(value_01_str)
        if value_01 > 0:
            number_valid = True
    except:
        print('valor indisponivel')
        continue

    print(soma_dos_valores(value_01, soma))
