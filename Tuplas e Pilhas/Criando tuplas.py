# Criando tuplas
coordenadas = (10, 20)
pessoa = ('Ana', 29, 'Engenheira')
tupla_vazia = ()
tupla_unica = (42)  # Vírgula é necessária!

# Acessando elementos
print(coordenadas[0])
print(pessoa[1]) 
print(tupla_unica)    

# Desempacotamento
x, y = coordenadas
nome, idade, profissao = pessoa
print(pessoa)

#nome, idade = pessoa
#print(pessoa)

# Tuplas são imutáveis
#coordenadas[0] = 15

numeros = (1, 2, 3, 2, 4, 2)
print(numeros.count(2))    # Saída: 3
print(numeros.index(4))    # Saída: 4


t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)      
# Saída: (1, 2, 3, 4)
print(t1 * 3)       
# Saída: (1, 2, 1, 2, 1, 2)
print(1 in t1)      
# Saída: True
print(len(t1 + t2)) 
# Saída: 4