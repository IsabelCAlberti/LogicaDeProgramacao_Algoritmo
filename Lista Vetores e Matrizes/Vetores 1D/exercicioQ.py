# ===============================
# Exercício q – Índices pares e ímpares
# ===============================
print("\n=== Exercício q ===")
A = [float(input(f"A[{i}]: ")) for i in range(15)]
B = [A[i]/2 if i%2==0 else A[i]*1.5 for i in range(15)]
print("\nMatriz B:", B)

