
# ===============================
# Exercício i – Junção de 3 vetores
# ===============================
print("\n=== Exercício i ===")
A = [float(input(f"A[{i}]: ")) for i in range(5)]
B = [float(input(f"B[{i}]: ")) for i in range(5)]
C = [float(input(f"C[{i}]: ")) for i in range(5)]
D = A + B + C
print("\nMatriz D (A+B+C):", D)
