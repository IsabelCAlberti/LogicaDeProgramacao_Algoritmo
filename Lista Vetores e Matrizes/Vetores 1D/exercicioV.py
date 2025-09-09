
# ===============================
# Exercício v – Contar pares e ímpares
# ===============================
print("\n=== Exercício v ===")
A = [int(input(f"A[{i}]: ")) for i in range(30)]
pares = sum(1 for x in A if x%2==0)
impares = len(A) - pares
print(f"Pares: {pares}, Ímpares: {impares}")

