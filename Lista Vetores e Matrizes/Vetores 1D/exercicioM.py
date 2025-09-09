
# ===============================
# Exercício m – Tabuada de um valor
# ===============================
print("\n=== Exercício m ===")
num = int(input("Digite o número da tabuada: "))
A = [num * i for i in range(1,11)]
print(f"\nTabuada de {num}:", A)
