
# ===============================
# Exercício j – Operação com pares e ímpares 6x5
# ===============================
print("\n=== Exercício j ===")
A = []
B = []

for i in range(6):
    linhaA = []
    linhaB = []
    for j in range(5):
        valor = int(input(f"A[{i}][{j}]: "))
        linhaA.append(valor)
        if valor % 2 == 0:
            linhaB.append(valor + 5)
        else:
            linhaB.append(valor - 4)
    A.append(linhaA)
    B.append(linhaB)

print("\nMatriz A:")
for linha in A:
    print(linha)
print("\nMatriz B:")
for linha in B:
    print(linha)