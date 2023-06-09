
# CREAR NUESTRAS PROPIAS EXCEPCIONES:

class miExcepcion (Exception):
    
    def __init__(self, parametro1, parametro2):
        
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        

try: 
    
    raise miExcepcion ("Este es mi mensaje de Error", "y aquí la información")

except miExcepcion as ex:
    
    p1, p2 = ex.args
    print (p1, p2)
    
    
print ("FIN")
