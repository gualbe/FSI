class Clase:
    def __init__(self):
        self.x = 15

def funcion (entero, bool, lista, tupla, objeto):
    entero = 5
    bool = True
    lista[0] = "Pepe"
    lista.append(10)
    tupla = (1,2)
    objeto.x = 10

e = 1
b = False
l = [4,6]
t = (3,4,5)
o = Clase()

print("Before: ", e, b, l, t, o.x)

funcion(e, b, l, t, o)

print("After: ", e, b, l, t, o.x)

# Los tipos simple se pasan por copia a las funciones
# Los objetos (listas, objetos, ...) se pasan por referencia
# Si se pasa un objeto (tupla, p.ej.) a una funcion y se asigna (machaca) otro valor al parametro, no tiene efecto. 