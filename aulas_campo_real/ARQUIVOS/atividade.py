""" 
❖ Devolve a quantidade de notas acima e igual a media.

❖ Devolve a maior nota.

❖ Devolve a menor nota. """

import os
grade_lists = []
approved = []
grades_above_six = []
grades_below_six = []
grades_above_average = 0
highest_grade = 0
lowest_grade = 10
total_grades = 0.0
grade_point_average = 0.0
grade_float = 0.0
while True:
    while True:
        # variaveis de controle
        grade_is_a_number = None
        grade_is_between_zero_and_ten = None

        # recebimentos de dados
        grade = input('DIGITE SUA NOTA: ')

        # verificação para conversão
        try:
            grade_float = float(grade)
            grade_is_a_number = True
        except:
            grade_is_a_number = None

        # verificação entre 0 e 10
        try:
            if grade_float <= 10 and grade_float >= 0:
                grade_is_between_zero_and_ten = True
        except:
            grade_is_between_zero_and_ten = None

        # verificação de erros
        if grade_is_a_number is None:
            print('APENAS NUMEROS SÃO PERMITIDOS.')
            continue
        if grade_is_between_zero_and_ten is None:
            print('APENAS NUMEROS ENTRE 0 E 10 SÃO PERMITIDOS.')
            continue

        # totais de notas inseridas
        grade_lists.append(grade_float)

        # variavel para somas as notas para a media
        total_grades += grade_float

        # medias das notas baseado no len
        grade_point_average = total_grades/len(grade_lists)

        # verificação se nota menor que 6
        if grade_float < 6.0:
            grades_below_six.append(grade_float)

        # verificação se esta entre 6 e 10
        elif grade_float >= 6.0 and grade_float <= 10.0:
            grades_above_six.append(grade_float)

        # nunca deveria chegar aqui
        else:
            print('não deveria ocorrer!')

        # verificar se é a maior nota
        if grade_float > highest_grade:
            highest_grade = grade_float

        # verificar se é a menor nota
        if grade_float < lowest_grade:
            lowest_grade = grade_float

        if len(grade_lists) > 5:
            # verificação para interromper o sistema
            exit = input('Quer sair? [s]im: ').lower().startswith('s')
            os.system('clear')

            if exit is True:
                break
    # verificação para o for de notas ser menor que o tamanho da lista notas
    for notas in range(len(grade_lists)):
        # verificação para se a nota apresentada for maior que a media faça algo
        if grade_lists[notas] > grade_point_average:
            # se nota acima da media for maior ela incrementa 1 no total de notas acima
            grades_above_average += 1

    os.system('clear')
    print('Apresentação de dados')
    print(f'O total de notas informadas = {len(grade_lists)}')
    print(f'A media da turma = {grade_point_average}')
    print(f'O Total de aprovados = {len(grades_above_six)} ')
    print(f'O Total de reprovados = {len(grades_below_six)} ')
    print(f'Notas acima da media= {grades_above_average}')
    print(f'A maior nota= {highest_grade}')
    print(f'A menor nota = {lowest_grade}')
    # verificação para definir se inicia o processo
    exit = input('Quer sair? [s]im: ').lower().startswith('s')
    os.system('clear')
    if exit is True:
        break
