
# ===============================
# Exercício u – Condições múltiplos com exclusão
# ===============================
print("\n=== Exercício u ===")
A = [i*2 for i in range(1,13) if i*2%2==0 or i*2%3==0]
B = [i for i in range(1,13) if i%5!=0]
C = A + B
print("\nMatriz C (A+B):", C)
