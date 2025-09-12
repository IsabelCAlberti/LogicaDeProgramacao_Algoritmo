import math

# ===============================
# Exercício d – Vetor A para matriz C 10x3
# ===============================
print("\n=== Exercício d ===")
A = [int(input(f"A[{i}]: ")) for i in range(10)]
C = []
for valor in A:
    linha = [valor + 5, math.factorial(valor), valor ** 2]
    C.append(linha)

print("\nMatriz C:")
for linha in C:
    print(linha)


