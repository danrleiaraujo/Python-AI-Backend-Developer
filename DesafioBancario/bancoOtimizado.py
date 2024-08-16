import textwrap
''' 
Separar funções existentes de saque, depósito e extrato em funções. Criar novas funções:
    - Cadastrar Usuário (Cliente)
    - Cadastrar conta bancária

    "Precisamos deixar nosso código mais modularizado, para isso
    vamo criar funções para as operações existentes: 
    - Sacar
    - Depositar
    - Visualizar histórico
    Alem disso, vamos para a versão 2 do nosso sistema, precisamos criar
    duas novas funções:
    - Criar usuario (cliente do banco)
    - Criar conta corrente (vincular com o usuário)"
'''

''' 
Saque:
    argumentos:
        Saldo, valor, extrato, limite, numero_saques, limites_saques
    Retorno:
        Saldo e extrato
'''
def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato
            
''' 
Deposito:
    argumentos:
        Saldo, valor, extrato.
    Retorno:
        Saldo e extrato
'''
def depositar (saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

''' 
Extrato:
    argumentos:
        Saldo, extrato
'''
def exibirExtrato (saldo, / , * , extrato):
        print("================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

''' 
criarUsuario()
Argumentos:
    Nome, data de nascimento, cpf e endereco (logadouro- bairro - cidade/sigla estado)
'''
def criarUsuario(usuarios):    
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("Já existe esse CPF cadastrado")
        return
    
    nome = input ("Informe o nome completo: ")
    data_nascimento = input ("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input ("Informe o endereço (logradouro, numero - bairro - cidade / sigla estado): ")
    
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco": endereco})
    print("Usuario cadastrado com sucesso!") 

''' 
criarContaCorrente()
Argumentos:
    Agencia, numero da conta e usuario
O numero da agencia é fixo "0001" e o usuario pode ter mais de uma conta, mas
a conta só pertence a um usuario
'''
def criarContaCorrente(agencia,numero_conta, usuarios):    
    cpf = input("Informe o CPF(somente números) do usuario: ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("Conta Criada com sucesso!")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    print("Usuario não encontrado! Fluxo de criação de conta encerrado.")

def filtrarUsuario(cpf, usuarios):    
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listarContas(contas):    
    for conta in contas:
        linha = f"""
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("="*100)
        print(textwrap.dedent(linha))

def menu():
    menuTitulo = " Menu ".center(40,"=")
    textomenu = """
        [d]  Depositar
        [s]  Sacar
        [e]  Extrato
        [nc] Nova Conta
        [lc] Listar Contas
        [nu] Novo Usuario
        [q]  Sair
        => """
    menu = menuTitulo + textomenu
    
    return input(textwrap.dedent(menu))

def main():
    ''' CONSTANTES'''
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    '''variaveis'''
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
                )

        elif opcao == "e":
            exibirExtrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criarUsuario(usuarios)
       
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criarContaCorrente(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listarContas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()