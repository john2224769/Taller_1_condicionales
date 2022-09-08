# Programa que calcula el valor de una llamada basado en su duracion 

#input
m=int(input("ingrese la cantidad de minutos de la llamada "))
print(" ")

#processing 
if m < 3:
    v=300
else:
    v=300+((m-3)*50)

#Output
print("El valor total de la llamada es de: "+str(v))
print(" ")