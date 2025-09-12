import math

# ===============================
# Exercício b – Junção de dois vetores em matriz 7x2
# ===============================
print("\n=== Exercício b ===")
A = [int(input(f"A[{i}]: ")) for i in range(7)]
B = [int(input(f"B[{i}]: ")) for i in range(7)]
C = [[A[i], B[i]] for i in range(7)]

print("\nMatriz C (junção de A e B):")
for linha in C:
    print(linha)

print("\n[b] Vetores A e B para matriz C (7x2):")
A = [int(input(f"A[{i}]: ")) for i in range(7)]
B = [int(input(f"B[{i}]: ")) for i in range(7)]
C = [[A[i], B[i]] for i in range(7)]
print("Matriz C:")
for linha in C:
    print(linha)
