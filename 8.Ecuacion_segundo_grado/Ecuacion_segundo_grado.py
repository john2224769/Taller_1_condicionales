#Programa N.8: Elaborar un programa que obtenga las raíces de una ecuación de segundo grado.

import math
from math import sqrt
print("-------------------------------------------------------------------------------------------------------------------")
print("--- Programa para solucionar una ecuacion de la forma: ax² + bx + c = 0, ingrese los coeficionestes de a, b y c ---")
print("-------------------------------------------------------------------------------------------------------------------")
print(" ")

#input
a= int(input("Ingrese el valor de a: "))
b= int(input("Ingrese el valor de b: "))
c= int(input("Ingrese el valor de c: "))

#processing
d = (b*b)-(4*a*c)
if d > 0:
    r=sqrt(d)
    x1=(b+r)/(2*a)
    x2=(b-r)/(2*a)
    print("La primer raiz X1 es: "+str(x1))
    print("La segunda raiz X2 es: "+str(x2))
    print(" ")
else:
    print("La ecuacion no tiene solucion en los reales")
    print(" ")