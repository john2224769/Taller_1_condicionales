#Programa N.7: Elaborar un programa para resolver una ecuación de primer grado.

from math import sqrt
#input
print( "----------------------------------------------------------------------------------------" )
print("Se dara solucion a la ecuacion de la forma ax + b = 0, ingrese los coeficionestes de a y b ")
print( "----------------------------------------------------------------------------------------" )
print(" ")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
print(" ")

#processing 
if a != 0:
        x = (-b/a)
        print("Solucion de la ecuacion: x= "+str(x))
        print(" ")
else:
    if  a == 0 and  b != 0:
        print("la ecuacion no tiene solucion ")
        print(" ")
    else:
        print("La ecuacion tiene infinitas soluciones")
print(" ")