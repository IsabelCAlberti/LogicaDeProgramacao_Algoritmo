# ===============================
# Exercício f – Fatorial em matriz 5x4
# ===============================
print("\n=== Exercício f ===")
A = []
B = []

for i in range(5):
    linhaA = []
    linhaB = []
    for j in range(4):
        valor = int(input(f"A[{i}][{j}]: "))
        linhaA.append(valor)
        linhaB.append(math.factorial(valor))
    A.append(linhaA)
    B.append(linhaB)

print("\nMatriz A:")
for linha in A:
    print(linha)
print("\nMatriz B (fatoriais):")
for linha in B:
    print(linha)
