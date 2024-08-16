''' 
    Fomos contratados por um grande banco para desenvolver o seu novo sistema.
    Esse banco deseja modernizar suas operações e para isso escolheu a liguagem Python.
    Para sua primeira versão do sistema devemos implementar apenas 3 operações:
    
    * Depósito
        Deve ser possível depositar valores positivos para a minha conta bancária. 
        A v1 do projeto trabalha com apenas um usuário, dessa forma não é necessário nos preocuparmos em conta e agencia.
        Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
    
    * Saque:
        O sistema deve permitir realizar 3 saques diários com o limite máximo de R$ 500,00
        Caso não tenha saldo em conta o sistema deve exibir uma mensagem informando que não será possivel sacar
        Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
    
    * Extrato:
        Essa operação deve listar todos os depósitos e saques realizados na conta.
        No fim da listagem deve ser exibido o saldo atual da conta.
        Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45
'''

menuTitulo = " Menu ".center(40,"=")
menu = """[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menuTitulo)
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")