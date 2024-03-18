'''Principais operações em fila:
Inserção: Adiciona um novo elemento.
Remoção: Remove o elemento que está no início da fila.
Busca: procura um elemento específico na fila.
enqueue(): insere um novo elemento no final da fila.
dequeue(): remove o primeiro elemento da fila.
peek(): retorna o primeiro elemento da fila, sem removê-lo.
is_empty(): verifica se a fila está vazia.
is_full(): verifica se a fila está cheia (em algumas implementações, há um limite  de tamanho para a fila).
'''

#Inserção - no final
def enqueue(fila, elemento):
    fila.append(elemento)
#Remoção - no inicio
def dequeue(fila):
    if len(fila) == 0:
        return "A fila está vazia, não é possível remover"
    else:
        return fila.pop(0)

#Primeiro elemento - peek
def peek(fila):
    if len(fila) == 0:
        return "Fila vazia"
    else:
        return fila[0]
def is_empty(fila):
    return len(fila) == 0

def size(fila):
    return len(fila)
#Reverse
def queueReverser(fila):
    filaReversa = []
   # return fila [::-1]
    while not is_empty(fila):
        item = fila.pop()#dequeue(fila)
        enqueue(filaReversa,item)
    return filaReversa
fila = []
enqueue(fila, 1)
enqueue(fila, 2)
enqueue(fila, 3)
enqueue(fila, 4)

#print(dequeue(fila))
#print(peek(fila))
#print(peekis_empty(fila))
#print(size(fila))
#print(queueReverser(fila))

"""Desafio: Uma pessoa está em uma fula de um parque de diversões e deseja saber qual é o tempo de espera estimado para
chegar ao brinquedo. Cade pessoa leva um determinado tempo para utilizar o brinquedo e, em seguida, sai da fila. 
A pessoa quer saber qual será a sua posição na fila e quanto tempo ela terá que esperar para chegar no brinquedo"""
