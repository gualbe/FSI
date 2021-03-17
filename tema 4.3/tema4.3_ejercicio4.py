frase = "Fundamentos de Sistemas de Información"

# -------------
# Ejercicio 4
# -----------
# Crear un diccionario de palabras que contenga el número de consonantes de cada palabra.
# Suponga que cada palabra solo puede tener vocales o consonantes. 
# Trate de reutilizar código, en la medida de lo posible.

def num_vocales(palabra):
    return sum(map(lambda x: x=='a' or x=='e' or x=='i' or x=='o' or x=='u', palabra))

def procesar_palabras(frase, func):
    palabras = frase.split()    
    resultados = map(func, palabras)
    return dict(zip(palabras, resultados))

print("Ejercicio 4")
print(procesar_palabras(frase, lambda p: len(p) - num_vocales(p)))
