#Programa No. 4: Construir un programa que lea un número entero y que determine si si último dígito es un número par.

import math

#Input
n=int(input("Digite un numero entero  : "))
print(" ")

#Processing
if (n%10)%2 == 0:
    print("El ultimo dígito "+str(n%10) +", es un numero par")
    print(" ")
else:
    print("El ultimo dígito "+str(n%10) +", no es un numero par")
    print(" ")
