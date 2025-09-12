vetor_a = [1,2,3,4,5]
vetor_b = [ 1,5,3,4,6]
vetor_c =[]

for i in range(len(vetor_a)):
    vetor_c.append(vetor_a[i] - vetor_b[i])


print(vetor_c)


vetor_a = [1, 2, 3, 4, 5]
vetor_b = [1, 5, 3]

# Preencher vetor_b com zeros até o tamanho de vetor_a
while len(vetor_b) < len(vetor_a):
    vetor_b.append(0)

vetor_c = [a - b for a, b in zip(vetor_a, vetor_b)]

print(vetor_c)


vetor_a = [1, 2, 3, 4, 5]
vetor_b = [1, 5, 3]

vetor_c = []
tamanho_min = min(len(vetor_a), len(vetor_b))

for i in range(tamanho_min):
    vetor_c.append(vetor_a[i] - vetor_b[i])

print(vetor_c)

vetor_a = [1, 2, 3, 4, 5]
vetor_b = [1, 5, 3]

vetor_c = []

tamanho_max = max(len(vetor_a), len(vetor_b))

for i in range(tamanho_max):
    a = vetor_a[i] if i < len(vetor_a) else None
    b = vetor_b[i] if i < len(vetor_b) else None
    
    if a is not None and b is not None:
        vetor_c.append(a - b)
    else:
    
        vetor_c.append(input("Digite um valor"))  

print(vetor_c)