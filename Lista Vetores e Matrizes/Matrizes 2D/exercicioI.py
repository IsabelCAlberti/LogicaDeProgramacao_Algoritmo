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
