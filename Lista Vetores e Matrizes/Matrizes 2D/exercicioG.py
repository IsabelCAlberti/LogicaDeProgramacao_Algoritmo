
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

print("\n[g] Temperaturas Celsius → Fahrenheit (4x5):")
A = [[float(input(f"Celsius A[{i}][{j}]: ")) for j in range(5)] for i in range(4)]
B = [[c * 9/5 + 32 for c in linha] for linha in A]
print("Celsius (A):")
for linha in A:
    print(linha)
print("Fahrenheit (B):")
for linha in B:
    print(linha)
