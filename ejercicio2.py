class TextFormatter:
    def __init__(self, texto):
        self.texto = texto

    def format_text(self):
        # Reemplazar "#" con "\n" para separar las frases
        texto_formateado = self.texto.replace("#", "\n")

        # Capitalizar la primera letra de cada frase
        texto_formateado = texto_formateado.capitalize()

        # Agregar un punto al final de cada frase si no lo tiene
        if not texto_formateado.endswith("."):
            texto_formateado += "."

        return texto_formateado


def main():
    texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

    formatter = TextFormatter(texto)
    texto_formateado = formatter.format_text()

    print(texto_formateado)



