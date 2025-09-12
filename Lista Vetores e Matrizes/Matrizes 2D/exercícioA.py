import math

# ===============================
# Exercício a – Soma de duas matrizes 5x3
# ===============================
print("\n=== Exercício a ===")
A = []
B = []
C = []

for i in range(5):
    linhaA = []
    linhaB = []
    linhaC = []
    for j in range(3):
        linhaA.append(int(input(f"A[{i}][{j}]: ")))
        linhaB.append(int(input(f"B[{i}][{j}]: ")))
        linhaC.append(linhaA[-1] + linhaB[-1])
    A.append(linhaA)
    B.append(linhaB)
    C.append(linhaC)

print("\nMatriz C (soma de A e B):")
for linha in C:
    print(linha)

print("\n[a] Soma de duas matrizes 5x3:")
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(3)] for i in range(5)]
B = [[int(input(f"B[{i}][{j}]: ")) for j in range(3)] for i in range(5)]
C = [[A[i][j] + B[i][j] for j in range(3)] for i in range(5)]
print("Matriz C (A + B):")
for linha in C:
    print(linha)
