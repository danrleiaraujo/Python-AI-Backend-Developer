nome_tecnologia = "PyThOn"

maiuscula = nome_tecnologia.upper() #Função que deixa as letras em maiuscula

minuscula = nome_tecnologia.lower()#Função que deixa as letras em minuscula

titulo = nome_tecnologia.title()#Função que deixa a primeira letra em maiuscula

print(maiuscula,minuscula,titulo)

curso = "    Python "

curso_sem_espaco = curso.strip()
print(curso_sem_espaco)

curso_sem_espaco_esquerda = curso.lstrip()
print(curso_sem_espaco_esquerda)

curso_sem_espaco_direita = curso.rstrip()
print(curso_sem_espaco_direita)

curso_centralizado = curso.center(12,"#")
print(curso_centralizado)

curso_pontilhado = ".".join(curso)
print(curso_pontilhado)