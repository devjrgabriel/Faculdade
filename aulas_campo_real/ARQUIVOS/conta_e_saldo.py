taxa_da_conta = 0
conta = int(input('Digite o numero da conta: '))

while (conta != -1):
    saldo = float(input('Digite o saldo da conta: R$ '))
    if saldo >= 10000:
        taxa_da_conta = saldo * 0.001
        print(f'A Taxa da sua conta é {taxa_da_conta}')
    else:
        taxa_da_conta = saldo * 0.003
        print(f'A Taxa da sua conta é {taxa_da_conta}')

    novo_saldo = saldo-taxa_da_conta
    print(f'O seu novo saldo = R$ {novo_saldo}')
    
    conta = int(input('Digite o numero da conta: '))
