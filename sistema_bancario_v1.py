# menu básico do sistema
menu = """
 ------ bem vindo ao seu banco -----

    digite qual a operação desejada

    [1] Deposito
    [2] Saque
    [3] Extrato
    [0] Sair
"""
# configurações do sistema
LIMITE_OPERACAO = 500
LIMITE_SAQUE = 3
extrato_minicial= f"Histórico de movimentações:\n"

# dicionário com valores especificos da conta

conta ={
     'saldo' : 1000,
     'extrato' : "",
     'saques_realizados' : 0
}

#funções da aplicação

def depositar(conta):
    valor_depositado = float(input('qual o valor a ser depositado?: '))
    if valor_depositado > 0:
        conta['saldo'] += valor_depositado
        conta['extrato'] += f'depósito de R$ {valor_depositado:.2f}\n'
        print('valor depósitado com sucesso')
    else:
        print('Valor inválido para depósito, tente novamente.')
    return conta


def sacar(LIMITE_SAQUE, LIMITE_OPERACAO, conta):
    if conta['saques_realizados'] >= LIMITE_SAQUE:
           print('limite de operações diarias atingidos, tente novamente amanhã')
    else:
        valor_saque = float(input('digite o valor a ser sacado: '))
        if valor_saque <= 0:
            print('valor invalido para saque')
        elif valor_saque > LIMITE_OPERACAO:
                print('o valor solicitado supera o limite de saque da conta, tente novamente')
        elif valor_saque >  conta['saldo']:
                print("saldo insuficiente, tente novamente")
        else:
                conta['saldo'] -= valor_saque
                conta['saques_realizados'] += 1
                conta['extrato'] += f"saque de R$ {valor_saque:.2f}\n"
                print('saque realidado com sucesso')
    return conta


def mostar_extrato(extrato_minicial, conta):
    print('\n' , extrato_minicial)
    if not conta['extrato']:
        print(f"Nenhuma operação realizada nesta data")
    else:
        print(conta['extrato'])
    print(f'saldo dispónivel: R$ {conta['saldo']:.2f}')
    print("-" * 30) 

# programa principal

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        conta = depositar(conta)

    elif opcao == "2":
        conta = sacar(LIMITE_SAQUE, LIMITE_OPERACAO, conta)
        
    elif opcao == '3':
         mostar_extrato(extrato_minicial, conta)
         
    elif opcao == '0':
        
        print('obrigado por utilizar nossos serviços, volte sempre')
        break
    
    else:
        print('opção inválida, tente novamente')