# ===============================
# Exercício r – Separar índices ímpares e pares
# ===============================
print("\n=== Exercício r ===")
A = [int(input(f"A[{i}]: ")) for i in range(6)]
B = [int(input(f"B[{i}]: ")) for i in range(6)]
C = [A[i] for i in range(6) if i%2!=0] + [B[i] for i in range(6) if i%2!=0]
D = [A[i] for i in range(6) if i%2==0] + [B[i] for i in range(6) if i%2==0]
print("\nMatriz C (índices ímpares):", C)
print("Matriz D (índices pares):", D)
