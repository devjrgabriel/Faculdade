frase = 'aaooooaaa'
i = 0
quantidade_que_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == '':
        i += 1
        continue
    qnt_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if quantidade_que_apareceu_mais_vezes < qnt_apareceu_mais_vezes_atual:
        quantidade_que_apareceu_mais_vezes = qnt_apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1


print(
    'a letra qu apareceu mais vezes foi'
    f'"{letra_que_apareceu_mais_vezes}" que apareceu'
    f'{quantidade_que_apareceu_mais_vezes}x'
)
