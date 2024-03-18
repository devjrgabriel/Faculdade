# laço que é utilizado para deixar repetitivo
while True:
    # recebimento de dados para verificação
    first_number = input('Digite o primeiro numero: ')
    second_number = input('Digite o segundo numero: ')
    operator = input('Digite o seu operador: ')
    first_number_float = 0
    second_number_float = 0

    # variavel de controle para acaso num for invalido
    valid_numbers = None

    try:
        # tentativa para converte oo numero apresentado para float
        first_number_float = float(first_number)
        second_number_float = float(second_number)
        # se efetuado com sucesso transforma numeros_validor para true
        valid_numbers = True
    except:
        # se sem sucesso a tentativa mantem numeros validos como none
        valid_numbers = None

    # verificação se os numeros estão validos
    if valid_numbers is None:
        print('numeros invalidos!! verifique:')
        continue
    # variavel que contem os operadores permitidos
    allowed_operator = '+-*/'
    # se o operador apresentado não estiver entre os permitidos faça:
    if operator not in allowed_operator:
        print('operador invalido')
        continue
    # se o operador inserido for maior que 01 ele acusara erro
    if len(operator) > 1:
        print('digite apenas um operador')
        continue
    # apresentação dos dados
    print('Segue abaixo seu resultado: ')
    # operaçoes dos dados
    if operator == '+':
        print(first_number_float + second_number_float)
    elif operator == '-':
        print(first_number_float - second_number_float)
    elif operator == '*':
        print(first_number_float * second_number_float)
    elif operator == '/':
        print(first_number_float / second_number_float)
    else:
        print('erro desconhecido')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
