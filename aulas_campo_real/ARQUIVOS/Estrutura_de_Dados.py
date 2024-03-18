# conjuntos

# Criando um conjunto vazio
meu_conjunto = set()

# conjunto com valor
meu_conjunto2 = {1, 2, 3, 4}

meu_conjunto2.add(8)
meu_conjunto2.remove(2)
# print(meu_conjunto)
# print(meu_conjunto2)

# verificar se um elemento esta no conjunto
'''if 3 in meu_conjunto2:
    print(True)
else:
    print(False)
    '''

# Operações Loli
# Uniao
conjuntoA = {1, 2, 3, 4, 5}
conjuntoB = {3, 4, 7, 89}

conjunto_c = conjuntoA.union(conjuntoB)
# print(conjunto_c)

# intesecçao
interseccao = conjuntoA.intersection(conjuntoB)
# print(interseccao)


# diferença
diferenca = conjuntoA.difference(conjuntoB)
# print(diferenca)

# dicionarios ---

meu_dicionario = {}

meu_dicionario2 = {
    'nome': 'Gabriel',
    'idade': 21,
    'cidade': 'Guarapuava',
    'Brasileiro': True,
    'bancos': {

    }
}

# print(meu_dicionario2['idade'])
# Adicionar elementos
meu_dicionario2['profissao'] = 'programador'
# remover elementos
del meu_dicionario2['bancos']
# verificar a existencia
# if 'idade' in meu_dicionario2:
# print(True)


chaves = meu_dicionario2.keys()
valores = meu_dicionario2.values()

# for chave, valor in meu_dicionario2.items():
#   print(chave, ': ', valor)

# Tuplas
minha_tupla = ('efg', False)
minha_tupla2 = (1, 2, 3, 'abc', True)

concatenacao = minha_tupla2+minha_tupla

# print(minha_tupla2[0])
# print(concatenacao)

# if 'abc' in minha_tupla2:
#    print(True)

# percorrer
# for elemento in minha_tupla2:
#   print(elemento)

# desafio
'''
1. crie um conjunto de 1 a 10 e imprima
2.crie um dicionario vazio e adicione duas chaves a ele
3. crie uma tupla com numeros de um a 5 e imprima
'''

conjunto_1_a_10 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

dicionario_ex = {}

tupla_um_a_cinco = (1, 2, 3, 4, 5)

print('Conjunto')
# conjunto
for numeros in conjunto_1_a_10:
    print(numeros)

print('Tuplas: ')

# tupla
for numeros in tupla_um_a_cinco:
    print(numeros)

dicionario_ex['nome'] = 'Gabriel'
dicionario_ex['idade'] = 21

print('Dicionario:')
for chave, valor in dicionario_ex.items():
    print(chave, ': ', valor)
