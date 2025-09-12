
# ===============================
# Exercício e – Fatorial de elementos
# ===============================
print("\n=== Exercício e ===")
A = [int(input(f"A[{i}]: ")) for i in range(15)]
B = [math.factorial(x) for x in A]
print("\nMatriz A:", A)
print("Matriz B (fatorial de A):", B)

import math

A = [int(input("Digite um número: ")) for _ in range(15)]
B = [math.factorial(x) for x in A]
print(B)
