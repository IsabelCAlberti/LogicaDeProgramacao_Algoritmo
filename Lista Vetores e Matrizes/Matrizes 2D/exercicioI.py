import math
# ===============================
# Exercício i – Somatório e fatorial na diagonal 7x7
# ===============================
print("\n=== Exercício i ===")
A = []
B = []

for i in range(7):
    linhaA = []
    linhaB = []
    for j in range(7):
        valor = int(input(f"A[{i}][{j}]: "))
        linhaA.append(valor)
        if i == j and (i % 2 == 0):
            linhaB.append(math.factorial(valor))
        else:
            linhaB.append(sum(range(1, valor+1)))
    A.append(linhaA)
    B.append(linhaB)

print("\nMatriz A:")
for linha in A:
    print(linha)
print("\nMatriz B:")
for linha in B:
    print(linha)
    
    print("\n[i] Matriz B com somatórios e fatoriais (7x7):")
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(7)] for i in range(7)]
B = []
for i in range(7):
    linha = []
    for j in range(7):
        val = A[i][j]
        if i == j and i % 2 == 1:
            linha.append(math.factorial(val))
        else:
            linha.append(sum(range(1, val + 1)))
    B.append(linha)
print("Matriz B:")
for linha in B:
    print(linha)

