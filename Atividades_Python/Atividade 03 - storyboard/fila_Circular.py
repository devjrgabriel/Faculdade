import funcoes_filas
import time

fila_chamados = ['pessoa01', 'pessoa02', 'pessoa03', 'pessoa04', 'pessoa05']

loop_menu = True

while loop_menu:
    print('MENU INICIAL: ')
    print('[1] VER FILA DE CHAMADOS ')
    print('[2] INSERIR CHAMADO ')
    print('[3] EXCLUIR PRIMEIRO CHAMADO ')
    print('[4] EXCLUIR CHAMADO ')
    escolha = int(input('QUAL SUA OPÇÃO: '))
    if escolha == 1:
        funcoes_filas.limpesa_e_time(1)
        funcoes_filas.apresentacao_de_dados(fila_chamados)
        funcoes_filas.limpesa_e_time(5)
    elif escolha == 2:
        nome_do_usuario = input('Digite o nome do usuario: ')
        funcoes_filas.incersao_De_dados_enqueue(nome_do_usuario, fila_chamados)
        time.sleep(1)
        print('Novo chamado criado ...')
        funcoes_filas.limpesa_e_time(2)
    elif escolha == 3:
        print('Excluindo primeiro item...')
        funcoes_filas.remover_no_inicio_da_fila_dequeue(fila_chamados)
    elif escolha == 4:
        indice_para_remocao = int(
            input('Qual a posição do chamado para remover: '))
        funcoes_filas.remover_com_o_indice_desejado(
            fila_chamados, indice_para_remocao)

    else:
        print('Opção indisponivel.')
        funcoes_filas.limpesa_e_time(2)
