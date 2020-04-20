frase = "Fundamentos de Sistemas de Información"

# -----------
# Ejercicio 1
# -----------
# Crear un diccionario de palabras que contenga la longitud de cada palabra,
# usando las funciones map, zip y dict.

def longitud_palabras(frase):
    palabras = frase.split()
    longitudes = map(len, palabras)
    return dict(zip(palabras, longitudes))

print("Ejercicio 1")
print(longitud_palabras(frase))

