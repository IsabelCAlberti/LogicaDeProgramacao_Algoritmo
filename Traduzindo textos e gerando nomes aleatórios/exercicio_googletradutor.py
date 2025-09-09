from googletrans import Translator

translator = Translator()
resultado = translator.translate("Olá mundo", src="pt", dest="en")

print(f"Texto traduzido: {resultado.text}")