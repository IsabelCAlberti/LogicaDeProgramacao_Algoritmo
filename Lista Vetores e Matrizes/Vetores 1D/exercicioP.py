
# ===============================
# Exercício p – Multiplicar ímpares por 2
# ===============================
print("\n=== Exercício p ===")
A = [int(input(f"A[{i}]: ")) for i in range(12)]
B = [x*2 if x%2!=0 else x for x in A]
print("\nMatriz B:", B)

