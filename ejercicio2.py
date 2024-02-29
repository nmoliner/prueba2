texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Reemplazar "#" con "\n" para separar las frases
texto_formateado = texto.replace("#", "\n")

# Capitalizar la primera letra de cada frase
texto_formateado = texto_formateado.capitalize()

# Agregar un punto al final de cada frase si no lo tiene
if not texto_formateado.endswith("."):
    texto_formateado += "."

print(texto_formateado)