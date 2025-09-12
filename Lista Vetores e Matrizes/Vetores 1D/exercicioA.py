import math

# ===============================
# Exercício a – Ler 10 nomes e mostrar
# ===============================
print("\n=== Exercício a ===")
A = [input(f"Digite o nome {i+1}: ") for i in range(10)]
print("\nNomes digitados:")
print(A)

nomes = []
for _ in range(10):
    nome = input("Digite um nome: ")
    nomes.append(nome)

for nome in nomes:
    print(nome)

