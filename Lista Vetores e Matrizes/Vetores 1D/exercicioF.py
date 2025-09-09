
# ===============================
# Exercício f – Junção de vetores
# ===============================
print("\n=== Exercício f ===")
A = [int(input(f"A[{i}]: ")) for i in range(15)]
B = [int(input(f"B[{i}]: ")) for i in range(15)]
C = A + B
print("\nMatriz C (A + B):", C)
