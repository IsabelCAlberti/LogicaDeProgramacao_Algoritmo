from deep_translator import GoogleTranslator

texto_para_traduzir = "Desculpa."
traduzido = GoogleTranslator(source='pt', target='en').translate(texto_para_traduzir)

print(f"Texto traduzido: {traduzido}")