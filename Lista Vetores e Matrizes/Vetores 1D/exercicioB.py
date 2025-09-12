import math

# ===============================
# Exercício b – Ler 8 números, multiplicar por 3
# ===============================
print("\n=== Exercício b ===")
A = [int(input(f"A[{i}]: ")) for i in range(8)]
B = [x*3 for x in A]
print("\nMatriz B (A*3):", B)

A = []
for _ in range(8):
    A.append(int(input("Digite um número: ")))

B = [x * 3 for x in A]
print(B)
