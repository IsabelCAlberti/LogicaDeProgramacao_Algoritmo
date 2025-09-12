# ===============================
# Exercício l – Metade de cada elemento
# ===============================
print("\n=== Exercício l ===")
A = [int(input(f"A[{i}]: ")) for i in range(10)]
B = [x/2 for x in A]
print("\nMatriz A:", A)
print("Matriz B (metade de A):", B)

A = [int(input("Digite um número: ")) for _ in range(10)]
B = [x / 2 for x in A]
print(B)
