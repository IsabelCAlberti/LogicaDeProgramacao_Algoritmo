
# ===============================
# Exercício g – Celsius para Fahrenheit 4x5
# ===============================
print("\n=== Exercício g ===")
A = []
B = []

for i in range(4):
    linhaA = []
    linhaB = []
    for j in range(5):
        c = float(input(f"A[{i}][{j}] (°C): "))
        linhaA.append(c)
        linhaB.append(c * 9/5 + 32)
    A.append(linhaA)
    B.append(linhaB)

print("\nMatriz A (°C):")
for linha in A:
    print(linha)
print("\nMatriz B (°F):")
for linha in B:
    print(linha)

