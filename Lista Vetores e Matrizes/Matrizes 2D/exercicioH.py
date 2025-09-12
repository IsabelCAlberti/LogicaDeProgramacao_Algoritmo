# ===============================
# Exercício h – Dobro e triplo com diagonal principal 5x5
# ===============================
print("\n=== Exercício h ===")
A = []
B = []

for i in range(5):
    linhaA = []
    linhaB = []
    for j in range(5):
        valor = int(input(f"A[{i}][{j}]: "))
        linhaA.append(valor)
        if i == j:
            linhaB.append(valor * 3)
        else:
            linhaB.append(valor * 2)
    A.append(linhaA)
    B.append(linhaB)

print("\nMatriz A:")
for linha in A:
    print(linha)
print("\nMatriz B:")
for linha in B:
    print(linha)

print("\n[h] Matriz B = 2x A (exceto diagonal = 3x A) - 5x5:")
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(5)] for i in range(5)]
B = [[A[i][j]*3 if i==j else A[i][j]*2 for j in range(5)] for i in range(5)]
print("Matriz B:")
for linha in B:
    print(linha)

