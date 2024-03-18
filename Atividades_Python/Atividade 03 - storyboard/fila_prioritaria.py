import funcoes_filas_prioridade
import time

fila_de_chamados_por_prioridade = {
    'prioridade01': 1,
    'prioridade02': 2,
    'gabriel': 1,

}


loop_menu = True

while loop_menu:
    valores_dos_chamado = list(fila_de_chamados_por_prioridade.keys())
    chaves_da_fila = fila_de_chamados_por_prioridade.values()
    prioridade01 = []
    prioridade02 = []
    funcoes_filas_prioridade.armazenamento_de_dados(
        prioridade01, prioridade02, fila_de_chamados_por_prioridade)
    print('MENU INICIAL: ')
    print('[1] VER FILA DE CHAMADOS ')
    print('[2] INSERIR CHAMADO ')
    print('[3] EXCLUIR PRIMEIRO CHAMADO ')
    print('[4] EXCLUIR CHAMADO ')
    escolha = int(input('QUAL SUA OPÇÃO: '))
    if escolha == 1:
        funcoes_filas_prioridade.limpesa_e_time(1)
        funcoes_filas_prioridade.apresentacao_de_dados_dicionarios(
            prioridade01, prioridade02)
        funcoes_filas_prioridade.limpesa_e_time(5)
    elif escolha == 2:
        funcoes_filas_prioridade.limpesa_e_time(2)
        print('[1] URGENCIA')
        print('[2] CHAMADO COMUM')
        prioridade_do_chamado = int(input('Qual a prioridade do chamado: '))
        if prioridade_do_chamado in chaves_da_fila:
            nome_do_usuario = input('Digite o nome do usuario: ')
            if prioridade_do_chamado in chaves_da_fila:
                fila_de_chamados_por_prioridade[nome_do_usuario] = prioridade_do_chamado
            else:
                print('Urgencia não identificada...')
            time.sleep(1)
            print('Novo chamado criado ...')
            funcoes_filas_prioridade.limpesa_e_time(2)
        else:
            print('Não foi possivel identificar a prioridade...')
            funcoes_filas_prioridade.limpesa_e_time(2)
    elif escolha == 3:
        print('Excluindo primeiro item...')
        chamado_inicial = valores_dos_chamado[0]
        del fila_de_chamados_por_prioridade[chamado_inicial]
        funcoes_filas_prioridade.limpesa_e_time(2)
    elif escolha == 4:
        variavel_coringa = 0
        funcoes_filas_prioridade.limpesa_e_time(2)
        print('TODOS OS CHAMADOS')
        for chave, valor in enumerate(valores_dos_chamado):
            print(f'NUMERO DO CHAMADO = {chave} | NOME DO USUARIO = {valor}')
            time.sleep(1)
        indice_para_remocao = int(
            input('Qual o numero do chamado para remover: '))

        funcoes_filas_prioridade.remover_com_o_indice_desejado(
            valores_dos_chamado, variavel_coringa, indice_para_remocao, fila_de_chamados_por_prioridade)

    else:
        print('Opção indisponivel.')
        funcoes_filas_prioridade.limpesa_e_time(2)
