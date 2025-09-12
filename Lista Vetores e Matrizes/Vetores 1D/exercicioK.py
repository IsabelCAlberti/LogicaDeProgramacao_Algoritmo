
# ===============================
# Exercício k – Negativo de elementos
# ===============================
print("\n=== Exercício k ===")
A = [int(input(f"A[{i}]: ")) for i in range(10)]
B = [-x for x in A]
print("\nMatriz B (negativo de A):", B)

A = [int(input("Digite um número: ")) for _ in range(10)]
B = [-x for x in A]
print(B)
