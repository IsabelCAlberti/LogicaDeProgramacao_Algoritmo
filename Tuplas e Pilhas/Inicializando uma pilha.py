# Inicializando uma pilha
pilha = []

# Operação Push (Empilhar)
pilha.append('Prato 1')
pilha.append('Prato 2')
pilha.append('Prato 3')
print(f"Pilha após push: {pilha}")

# Operação Pop (Desempilhar)
topo_removido = pilha.pop()
print(f"Elemento removido: {topo_removido}")
print(f"Pilha após pop: {pilha}")

# Operação Peek (Espiar o topo)
# Verifica se a pilha não está vazia antes de espiar
if pilha:
    topo = pilha[-1]
    print(topo)
    pilha.clear()
    print("Pilha esvaziada:", pilha)  # []
    
    print(f"Elemento no topo (peek): {topo}")
else:
    print("Pilha vazia, não há o que espiar.")

# Operação isEmpty (Verificar se está vazia)
print(f"A pilha está vazia? {not bool(pilha)}")

# Operação Size (Tamanho da pilha)
print(f"Tamanho da pilha: {len(pilha)}")

pilha = []

# Empilhar
pilha.append("A")
pilha.append("B")
pilha.append("C")
print("Pilha:", pilha)  # ['A', 'B', 'C']

# Ver topo
print("Topo:", pilha[-1])  # C

# Desempilhar
print("Removido:", pilha.pop())  # C
print("Pilha agora:", pilha)  # ['A', 'B']

# Tamanho
print("Tamanho:", len(pilha))  # 2

# Esvaziar
pilha.clear()
print("Depois do clear:", pilha)  # []
