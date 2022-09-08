#Programa N.3: Construir un programa que lea un número entero y determine si es un número positivo de 4 dígitos.
#Input
n=int(input("Ingrese un numero entero: "))
print(" ")

#Processing
if 1<= n/1000 <= 9.999:
    print("El numero ingresado es de cuatro cifras")
    print(" ")
else:
    print("El numero ingresado no es de cuatro cifras")
    print(" ")