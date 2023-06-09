
# EJEMPLOS DE ASSERT:

# Se denominan TESTING:
# TRUCO: Podemos saltarnos los ASSERT ejecutando el programa: "python -O Ejercicio4.py"


# Ejemplo 1:

def calcular_media (lista):
    
    return sum (lista)/len(lista)


assert (calcular_media([5,5,5]) == 5)

# Ejemplo 2:

def suma (a,b):
    
    assert (type(a) == int)
    assert (type(b) == int)
    return a + b

print (suma (2,3))
    
    
# Ejemplo 3:

class Mi_1:
    pass

class Mi_2:
    pass

m1 = Mi_1 ()
m2 = Mi_2 ()

assert (isinstance (m1, Mi_2))

# (Assert siempre se utiliza cuando podemos hacer un condicional)

print ("FIN")