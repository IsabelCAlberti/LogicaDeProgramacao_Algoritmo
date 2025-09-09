
# ===============================
# Exercício c – Subtração de dois vetores
# ===============================
print("\n=== Exercício c ===")
A = [float(input(f"A[{i}]: ")) for i in range(20)]
B = [float(input(f"B[{i}]: ")) for i in range(20)]
C = [A[i]-B[i] for i in range(20)]
print("\nMatriz C (A-B):", C)

