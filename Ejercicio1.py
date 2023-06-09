
# EXCEPCIONES:

a = 5
b = 1

try:
    
    a/b

    
except ZeroDivisionError as e:
    
    print ("ERROR: DIVISIÓN ENTRE 0", e)
    
except TypeError:
    
    print ("ERROR: Tipo de Dato")

# Tambien podemos utilizar excepciones de esta forma:

except (ZeroDivisionError, TypeError):
    
    print ("Error")
    
except Exception as e:
    
    print ("ERROR GENERAL: ", e)
    
else: 
    
    print ("Entra en este bloque si no existe ninguna EXCEPCIÓN")
    
finally:
    
    print ("!Este bloque se ejecuta siempre!")

print ("Fin")