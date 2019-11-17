import os
#declarar variables
cliente,vendedor,zapatillas,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
zapatillas=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(zapatillas*pu)
#verificador
por_compras=(total>600)
comprador_compulsivo= (total>1200)

#ouput

print("  BOLETA ELECTRONICA     ")
print("   RIPLEY        ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("manteles:",zapatillas ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional doble
#si es comprador recurrente otorgar una tarjeta
if (por_compras==True):
    print("GANASTE TARJETA DE ORO")
#si fuiste el que más compro en el año te otorgaran un plus
if (comprador_compulsivo==True):
    print("FELICIDADES GANASTE UN PLUS")


