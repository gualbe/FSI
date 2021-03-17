import Venta1, Venta2, Venta3
import sys

print(sys.version, "\n")

print("Venta 1")
v1 = Venta1.Venta(1000)
print(v1.importe)
v1.importe = 2000
print(v1.importe,"\n")

print("Venta 2\n")
v2 = Venta2.Venta(1000)
# print(v2.importe)
# v2.__importe = 2000
# print(v2.__importe)

print("Venta 3")
v3 = Venta3.Venta(1000)
print(v3.importe)
v3.importe = 2000
print(v3.importe)
