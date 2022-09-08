#Programa No.5: Construir un programa que lea un número entero y que determine si sus dos últimos dígitos son iguales.

import math

#input
n=int(input("Ingrese un numero entero  : "))
print(" ")

#processing 
m1=n%10
m2= ((n%100)-m1)//10

if m1 == m2:
    print("Los ultimos dos digitos son iguales")
    print(" ")
else:
    print("Los ultimos dos digitos no son iguales")
    print(" ")