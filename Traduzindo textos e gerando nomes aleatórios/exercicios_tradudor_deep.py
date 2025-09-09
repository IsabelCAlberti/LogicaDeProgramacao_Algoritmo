from deep_translator import GoogleTranslator

texto_para_traduzir = "i'm sorry."
traduzido = GoogleTranslator(source='en', target='pt').translate(texto_para_traduzir)

print(f"Texto traduzido: {traduzido}")