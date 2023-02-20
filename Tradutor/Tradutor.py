from translate import Translator

texto = input("Texto a ser traduzido: ")
traduzir = input("Deseja traduzir para o inglês? (s/n): ")

if traduzir.lower() == "s":
    translator = Translator(from_lang="pt-br", to_lang="en")
    traduzido = translator.translate(texto)
    print("Texto traduzido:", traduzido)
else:
    traduzido = texto
