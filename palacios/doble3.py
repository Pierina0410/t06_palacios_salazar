import os
#declarar variables
cliente,vendedor,manteles,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
manteles=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(manteles*pu)
#verificador
cliente_medio=(total>120)
comprador_alto= (total>1200)

#ouput

print("  BOLETA ELECTRONICA     ")
print("   RIPLEY        ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("manteles:",manteles ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional doble
#si es comprador recurrente otorgar una tarjeta
if (cliente_medio==True):
    print("GANASTE TARJETA DE PLATA")
#si fuiste el que más compro en el año te otorgaran un viaje
if (comprador_alto==True):
    print("FELICIDADES GANASTE UN VIAJE POR FIESTAS PATRIAS")
