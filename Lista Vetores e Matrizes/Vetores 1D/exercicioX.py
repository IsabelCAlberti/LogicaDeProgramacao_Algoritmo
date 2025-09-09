
# ===============================
# Exercício x – Reorganizar índices pares e ímpares
# ===============================
print("\n=== Exercício x ===")
A = [float(input(f"A[{i}]: ")) for i in range(6)]
B = [A[i-1] if i%2==0 else A[i+1] for i in range(6)]

print("Matriz B:", B)
