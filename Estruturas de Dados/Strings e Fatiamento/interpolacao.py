
nome = "Danrlei"
idade = 26
curso = "Python"
PI = 3.14159

print("Curso de: %s e tecnologia" %curso)

# Metodo convencional
print("Olá, eu me chamo %s, tenho %d anos e estou matriculado no curso de %s" %(nome,idade,curso))

#Metodo Format
print("Olá, eu me chamo {}, tenho {} anos e estou matriculado no curso de {}" .format(nome,idade,curso))

print("Olá, eu me chamo {2}, tenho {2} anos e estou matriculado no curso de {1}" .format(nome,idade,curso))

print("Olá, eu me chamo {name}, tenho {age} anos e estou matriculado no curso de {course}" 
.format(name = nome,age = idade,course = curso))

#Metodo f-string
print(f"Olá, eu me chamo {nome}, tenho {idade} anos e estou matriculado no curso de {curso}")
print(f"Valor de PI:{PI: .2f}")

