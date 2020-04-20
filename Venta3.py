class Venta:
    
    __importe = 0
    
    def __init__(self, x):
        self.__importe = x
        
    @property
    def importe(self):
        return self.__importe
    
    @importe.setter
    def importe(self, importe):
        self.__importe = importe
