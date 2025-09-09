# ===============================
# Exercício w – Quadrado da soma de vetores
# ===============================
print("\n=== Exercício w ===")
A = [int(input(f"A[{i}]: ")) for i in range(10)]
B = [int(input(f"B[{i}]: ")) for i in range(10)]
C = [(A[i]+B[i])**2 for i in range(10)]
print("\nMatriz C:", C)
