# pilhas
def criar_pilhas():
    pilha = []
    return pilha


def verificar_vazio(pilha):
    return len(pilha) == 0

# empilhar


def push(pilha, item):
    pilha.append(item)

# desempilhar


def pop(pilha):

    if not verificar_vazio(pilha):
        return pilha.pop()
    else:
        return "A pilha esta vazia"

# topo da pilha


def peek(pilha):
    if not verificar_vazio(pilha):
        return pilha[-1]
    else:
        return 'a pilha esta vazia'


def size(pilha):
    return len(pilha)


'''pilha_criada = criar_pilhas()
print(verificar_vazio(pilha_criada))

push(pilha_criada, 45678)
push(pilha_criada, 9876)

print(peek(pilha_criada))
print(pop(pilha_criada))
print(verificar_vazio(pilha_criada))

print(peek(pilha_criada))
print(pop(pilha_criada))
print(peek(pilha_criada))
'''
