def num_vocales(palabra):
    return sum(map(lambda x: x=='a' or x=='e' or x=='i' or x=='o' or x=='u', palabra))

def procesar_palabras(frase, func):
    palabras = frase.split()    
    resultados = map(func, palabras)
    return dict(zip(palabras, resultados))
