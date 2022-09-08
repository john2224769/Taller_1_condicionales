#Programa N.9: Calcular el valor a pagar por un cliente dependiendo del tipo de cliente y del medio de pago 

c=input("ingrese el tipo de cliente: G para general y A para afiliado ")
print(" ")
f=input("ingrese el medio de pago del cliente: C para pago de contado y P para pago a plazos ")
print(" ")
m=(float(input("ingrese el valor de la compra: ")))
print(" ")

#processing 
if c == 'G'and f == 'C':
    t=m-(m*0.15)
    print("Cliente general, con metodo de pago de contado, descuento de 15%. Valor total a pagar: "+str(t))
    print(" ")
else:
    if c == 'G' and f == 'P':
        t=m+(m*0.10)
        print("Cliente General, metodo de pago a plazos, recargo de 10%. Valor total a pagar: "+str(t))
        print(" ")
    else:
        if c == 'A' and f == 'C':
            t=m-(m*0.2)
            print("Cliente Afiliado, metodo de pago de contado, descuento de 20%. Valor total a pagar: "+str(t))
            print(" ")
        else:
            if c == 'A' and f == 'P':
                t=m+(m*0.05)
                print("Cliente Afiliado, metodo de pago a plazos, recargo de 5%. Valor total a pagar: "+str(t))
                print(" ")
            else: 
                print("Las opciones ingresadas fueron incorrectas verifiquelas por favor. ")
