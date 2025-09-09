

# ===============================
# Exercício c – Organizar vetor em matriz 4x5
# ===============================
print("\n=== Exercício c ===")
A = []
for i in range(4):
    linha = []
    for j in range(5):
        linha.append(int(input(f"A[{i}][{j}]: ")))
    A.append(linha)

print("\nMatriz A:")
for linha in A:
    print(linha)


