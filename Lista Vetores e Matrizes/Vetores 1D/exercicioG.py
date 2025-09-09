
# ===============================
# Exercício g – Junção de nomes
# ===============================
print("\n=== Exercício g ===")
A = [input(f"A[{i}]: ") for i in range(20)]
B = [input(f"B[{i}]: ") for i in range(30)]
C = A + B
print("\nMatriz C (junção de A e B):", C)
