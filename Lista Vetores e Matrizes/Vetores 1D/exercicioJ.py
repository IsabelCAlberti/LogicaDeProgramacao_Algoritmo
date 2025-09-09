
# ===============================
# Exercício j – Somatório de 1 até elemento
# ===============================
print("\n=== Exercício j ===")
A = [int(input(f"A[{i}]: ")) for i in range(20)]
B = [sum(range(1, x+1)) for x in A]
print("\nMatriz B (somatório até A[i]):", B)
