# ===============================
# Exercício o – Celsius para Fahrenheit
# ===============================
print("\n=== Exercício o ===")
A = [float(input(f"A[{i}]: ")) for i in range(25)]
B = [x*9/5+32 for x in A]
print("\nMatriz A (°C):", A)
print("Matriz B (°F):", B)
