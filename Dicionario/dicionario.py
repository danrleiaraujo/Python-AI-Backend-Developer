#Criando um dicionario
pessoa = { "nome": "Danrlei" , "idade": 26} 
''' 
outra forma:
pessoa = dict(nome = "Danrlei", idade = 28)
'''

#mudando valores
pessoa["nome"] = "Maria"
pessoa["idade"] = 20

#print(pessoa)

#dicionarios dentro de um dicionario
contatos = { 
    "danrleiaraujo@bol.com" :{ "nome": "Danrlei Araujo", "telefone" : "12 1234-4321"},
    "mariajose@bol.com" :{ "nome": "Maria Jose", "telefone" : "12 4321-1234"}
} 

#print(contatos)

#Acessando dados do dicionario com dicionario dentro
telefone = contatos["danrleiaraujo@bol.com"]["telefone"]
#print(telefone)

#Percorrendo um dicionario:

''' for chave in contatos:
    print(chave, contatos[chave])

Outra forma:
for chave, valor in contatos.items():
    print(chave,valor)
'''

'''Metodos:'''
copia = contatos.copy() #copia um dicionario
contatos.clear() # Apaga todos os valores do dicionario
copia.fromkeys(["endereco"]) #Cria chaves com valor None
copia.get("danrleiaraujo@bol.com") #forma de verificar se a chave existe
copia.keys() #retorna as chaves
copia.values #retorna os valores
copia.setdefault("idade", 20) #coloca uma chave e valor default caso não tenha
#copia.update() para atualizar algo do dicionario ou acrescentar caso não exista
del copia["mariajose@bol.com"] #Deleta a chave e seus valores
print(copia)
