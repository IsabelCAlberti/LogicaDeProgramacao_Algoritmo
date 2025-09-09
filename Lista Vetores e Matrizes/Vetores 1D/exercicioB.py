import math

# ===============================
# Exercício b – Ler 8 números, multiplicar por 3
# ===============================
print("\n=== Exercício b ===")
A = [int(input(f"A[{i}]: ")) for i in range(8)]
B = [x*3 for x in A]
print("\nMatriz B (A*3):", B)
