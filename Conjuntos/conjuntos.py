lista = [1,2,2,3,4,5,5,7]
listaSemRepeticao = set (lista)
print(listaSemRepeticao) # 1 2 3 4 5 7

tecnologias = {"Python", "C", "Java", "Python", "PHP"}
cursos= {"Backend", "Frontend", "FullStack"}

# Tira redundancias
listaTecnologias = set (tecnologias)
print(listaTecnologias) # {"Python", "C", "Java", "PHP"}

# Une duas listas
cursos_e_tecnologias = cursos.union(tecnologias)
print(cursos_e_tecnologias) # {"Backend", "Frontend", "FullStack", "Python", "C", "Java", "PHP"}

#Interseção de duas listas
cursos_e_tecnologias = cursos.intersection(tecnologias)
print(cursos_e_tecnologias)
