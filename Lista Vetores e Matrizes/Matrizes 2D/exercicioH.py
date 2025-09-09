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

