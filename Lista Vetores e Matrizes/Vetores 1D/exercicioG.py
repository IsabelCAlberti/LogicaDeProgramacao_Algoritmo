
# ===============================
# Exercício g – Junção de nomes
# ===============================
print("\n=== Exercício g ===")
A = [input(f"A[{i}]: ") for i in range(20)]
B = [input(f"B[{i}]: ") for i in range(30)]
C = A + B
print("\nMatriz C (junção de A e B):", C)

A = [input("Digite um nome para A: ") for _ in range(20)]
B = [input("Digite um nome para B: ") for _ in range(30)]
C = A + B
print(C)
