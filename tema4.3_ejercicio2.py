frase = "Fundamentos de Sistemas de Información"

# -----------
# Ejercicio 2
# -----------
# Crear un diccionario de palabras que contenga la longitud de cada palabra,
# usando dict-comprehension.

def longitud_palabras2(frase):
    return {palabra:len(palabra) for palabra in frase.split()}

print("Ejercicio 2")
print(longitud_palabras2(frase))

