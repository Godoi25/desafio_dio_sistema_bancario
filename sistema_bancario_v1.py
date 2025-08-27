
menu = """
 ------ bem vindo ao seu banco -----

    digite qual a operação desejada

    [1] Deposito
    [2] Saque
    [3] Extrato
    [0] Sair
"""
saques_realizados = 0
saldo = 1000
valor_saque = 0
LIMITE_OPERACAO = 500
LIMITE_SAQUE = 3
extrato_minicial= f"Histórico de movimentações:\n"
extrato = ""

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        deposito= float(input("qual o valor a ser depositado?: "))
        if deposito <= 0:
            print('valor inválido para deposito, tente novamente')
        else:
            saldo = saldo + deposito
            extrato += f"depósito de R$ {deposito:.2f}\n"
            print("valor depositado com sucesso!")               
        

    elif opcao == "2":

        if saques_realizados >= LIMITE_SAQUE:
           print('limite de operações diarias atingidos, tente novamente amanhã')
        else:
            valor_saque = float(input('digite o valor a ser sacado: '))
            if valor_saque <= 0:
                print('valor invalido para saque')
            elif valor_saque > LIMITE_OPERACAO:
                print('o valor solicitado supera o limite de saque da conta, tente novamente')
            elif valor_saque >  saldo:
                print("saldo insuficiente, tente novamente")
            else:
                saldo = saldo - valor_saque
                saques_realizados = saques_realizados + 1
                extrato += f"saque de R$ {valor_saque:.2f}\n"
                print('saque realidado com sucesso')
        
    elif opcao == '3':

        if extrato == "":
            print( extrato_minicial , f"Nenhuma operação realizada nesta data, saldo disponivel R$ {saldo:.2f}")
        else:
            print( extrato_minicial , extrato , f"saldo disponivel R$ {saldo:.2f}")

    elif opcao == '0':
        
        print('obrigado por utilizar nossos serviços, volte sempre')
        break
    
    else:
        print('opção inválida, tente novamente')