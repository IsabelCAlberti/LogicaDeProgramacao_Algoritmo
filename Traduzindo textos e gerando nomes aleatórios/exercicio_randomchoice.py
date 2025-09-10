import random

adjetivos = ["feliz", "triste", "rápido", "forte", "fofo", "gelado"]
substantivos = ["cachorro", "gato", "carro", "pizza", "livro", "bolo"]

def nome_pt():
    return f"{random.choice(adjetivos).capitalize()} {random.choice(substantivos).capitalize()}"
for _ in range(10):
    print(nome_pt())
