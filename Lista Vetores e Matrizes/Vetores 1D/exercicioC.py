
# ===============================
# Exercício c – Subtração de dois vetores
# ===============================
print("\n=== Exercício c ===")
A = [float(input(f"A[{i}]: ")) for i in range(20)]
B = [float(input(f"B[{i}]: ")) for i in range(20)]
C = [A[i]-B[i] for i in range(20)]
print("\nMatriz C (A-B):", C)

A = [int(input("Digite um número para A: ")) for _ in range(20)]
B = [int(input("Digite um número para B: ")) for _ in range(20)]
C = [a - b for a, b in zip(A, B)]
print(C)
