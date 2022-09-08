# Programa N.2 condiconales: Hallar el mayor de tres numeros enteros 

from ast import If


print("-----------------------------")
print("------- Mayor de 3 enteros --------")
print("-----------------------------")
print(" ")

#input
a=int(input("Ingrese el primer numero: "))
print(" ")
b=int(input("Ingrese el segundo numero: "))
print(" ")
c=int(input("Ingrese el tercer numero: "))
print(" ")

#processing 
if a>b:
    if a>c:
        mayor=a
    else:
        mayor=c
else:
    if b>c:
        mayor=b
    else:
        mayor=c

#output
print("El mayor de los numeros entre: "+str(a)+", "+str(b)+", "+str(c)+", es: "+str(mayor))

