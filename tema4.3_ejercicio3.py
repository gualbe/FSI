frase = "Fundamentos de Sistemas de Información"

# -----------
# Ejercicio 3
# -----------
# Crear dos diccionarios de palabras:
# - Uno que contenga la longitud de cada palabra.
# - Otro que contenga el número de vocales de cada palabra.
# Trate de reutilizar código, en la medida de lo posible.

def num_vocales(palabra):
    return sum(map(lambda x: x=='a' or x=='e' or x=='i' or x=='o' or x=='u', palabra))

def procesar_palabras(frase, func):
    palabras = frase.split()    
    resultados = map(func, palabras)
    return dict(zip(palabras, resultados))

print("Ejercicio 3")
print(procesar_palabras(frase, len))
print(procesar_palabras(frase, num_vocales))

