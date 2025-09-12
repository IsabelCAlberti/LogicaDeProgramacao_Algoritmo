A = [[1, 2, 3] , [20,30,5]]
B = [[21,5, 3] , [40,1,0]]
C = []

for i in range(len(A)):
    linha = []
    for b in range(len(A[0])): #A[0] representa a primeira linha da matriz
        linha.append(A[i][b] - B[i][b])
    C.append(linha)

print("Matriz C é igual a matriz A - matriz B: ")
for linha in C:
    print(linha)