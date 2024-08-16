saldo = 1000
saque = 250
limite = 200
conta_especial= True

if ((saldo >= saque and saque<=limite) or (conta_especial and saldo >= saque)):
    print("Ação realizada com sucesso")
else:
    print("Ação não permitida")