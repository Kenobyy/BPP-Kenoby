# Excepciones personalizadas 2 Parte

# Vamos a crear una excepción en el caso que un valor no se encuentre entre dos números

class ValorMinimo (Exception):
    
    def __init__(self, mensaje):
        
        self.mensaje = mensaje
        
    def __str__(self):
        
        return "Error de valor mínimo: {}".format (self.mensaje)
    
        
numero = 10
minimo = 20

try:
    
    if numero < minimo:
        
        numero = int (input ("Introduce un número entero: "))    
        raise ValorMinimo ("Se ha introducido un valor menor a {}".format (minimo))

except ValueError:
    
    print ("Error. Introduce un valor entero")

except ValorMinimo as e:
    
    print ("Error. ", e)
    
    
    



