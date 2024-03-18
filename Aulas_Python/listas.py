import os
nome = ['gabriel','maria','rosa','gabi','mafe']
idade = [21,22,13,25,87]

for i in range (len(idade)):
    if idade[i] >= 18:
        print(f'maior de idade é nome: {nome[i]}')
        

novo_nome=input('digite seu nome: ')
nome.append(novo_nome)
nova_idade=int(input('digite sua idade: '))
idade.append(nova_idade)

for i in range (len(nome)):
    for i in range (len(idade)):
        print(f'nome = {nome[i]}')  
        print(f'idade = {idade[i]}')