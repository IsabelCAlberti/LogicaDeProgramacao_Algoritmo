# ===============================
# Exercício d – Quadrado de elementos
# ===============================
print("\n=== Exercício d ===")
A = [int(input(f"A[{i}]: ")) for i in range(15)]
B = [x**2 for x in A]
print("\nMatriz A:", A)
print("Matriz B (quadrado de A):", B)
