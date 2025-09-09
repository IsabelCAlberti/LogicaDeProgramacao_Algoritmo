# ===============================
# Exercício e – Operações diferentes em duas matrizes 12x2
# ===============================
print("\n=== Exercício e ===")
A = [float(input(f"A[{i}]: ")) for i in range(12)]
B = [float(input(f"B[{i}]: ")) for i in range(12)]
C = [[A[i]*2, B[i]-5] for i in range(12)]

print("\nMatriz A:", A)
print("Matriz B:", B)
print("Matriz C:")
for linha in C:
    print(linha)

