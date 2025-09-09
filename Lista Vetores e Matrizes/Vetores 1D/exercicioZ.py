
# ===============================
# Exercício z – Contar elementos ímpares e percentual
# ===============================
print("\n=== Exercício z ===")
A = [int(input(f"A[{i}]: ")) for i in range(10)]
impares = sum(1 for x in A if x%2!=0)
percentual = impares/len(A)*100
print(f"Ímpares: {impares}, Percentual: {percentual:.1f}%")