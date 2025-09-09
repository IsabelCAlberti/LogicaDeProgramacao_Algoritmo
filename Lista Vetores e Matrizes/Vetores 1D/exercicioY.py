
# ===============================
# Exercício y – Contar elementos pares
# ===============================
print("\n=== Exercício y ===")
A = [int(input(f"A[{i}]: ")) for i in range(15)]
pares = sum(1 for x in A if x%2==0)
print("Total de pares:", pares)
