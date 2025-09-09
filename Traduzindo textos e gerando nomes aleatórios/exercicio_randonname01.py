import randomname
import re

# dicionário de exemplo: chaves em inglês (lowercase) -> tradução em português
traducao = {
    "happy": "feliz",
    "investor": "investidor",
    "falls": "quedas",
    "ambitious": "ambicioso",
    "twitch": "tique",
    "dog": "cachorro",
    "cat": "gato",
    "pizza": "pizza",
    # adicione mais conforme for vendo nos outputs do randomname
}

def traduz_preservando_caso(match):
    palavra = match.group(0)
    chave = palavra.lower()
    traducao_palavra = traducao.get(chave)
    if not traducao_palavra:
        return palavra  # não encontrada: retorna original
    # preserva maiúsculas/minúsculas básicas
    if palavra.isupper():
        return traducao_palavra.upper()
    if palavra[0].isupper():
        return traducao_palavra.capitalize()
    return traducao_palavra

# gerar e traduzir
name_en = randomname.get_name()    # ex: "ambitious-twitch" ou "investor-falls"
name_pt = re.sub(r'\w+', traduz_preservando_caso, name_en)

print("Inglês:", name_en)
print("Português:", name_pt)
