nome = input('Digite Seu Nome: ')
idade = input('Digite sua Idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if '' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome nao contem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
else:
    print('Um ou mais campos vazios.')
