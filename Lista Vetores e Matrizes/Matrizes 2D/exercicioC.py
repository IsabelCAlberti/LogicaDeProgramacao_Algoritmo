

# ===============================
# Exercício c – Organizar vetor em matriz 4x5
# ===============================
print("\n[c] Organizar 20 números em matriz 4x5:")
A = []
for i in range(4):
    linha = []
    for j in range(5):
        linha.append(int(input(f"A[{i}][{j}]: ")))
    A.append(linha)

print("\nMatriz A:")
for linha in A:
    print(linha)

numeros = [int(input(f"Digite o número {i+1}: ")) for i in range(20)]
matriz = [numeros[i*5:(i+1)*5] for i in range(4)]
for linha in matriz:
    print(linha)

