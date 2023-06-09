
# RAISE:
# Nos permite lanzar cualquier tipo de Excepción.

#raise ZeroDivisionError ("INFO DE LA EXCEPCIÓN")

# EJEMPLO:

edad = 17
a = 1
b = 0

try:
    
    if type (b) != int:

        raise Exception

    else:
        
        print ("OK! Puede pasar")

except Exception:
    
    print ("NO ES MAYOR DE EDAD")    

print ("FIN")