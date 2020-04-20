frase = "Fundamentos de Sistemas de Información"

# ------------- 
# Ejercicio 5
# -----------
# Crear un diccionario de palabras que contenga tanto la longitud, 
# como el número de vocales y consonantes de cada palabra 
# (los tres datos en una tupla por cada palabra).
# Trate de reutilizar código, en la medida de lo posible.

def num_vocales(palabra):
    return sum(map(lambda x: x=='a' or x=='e' or x=='i' or x=='o' or x=='u', palabra))

def procesar_palabras(frase, func):
    palabras = frase.split()    
    resultados = map(func, palabras)
    return dict(zip(palabras, resultados))

print("Ejercicio 5")
print(procesar_palabras(frase, lambda p: (len(p), num_vocales(p), len(p) - num_vocales(p))))
