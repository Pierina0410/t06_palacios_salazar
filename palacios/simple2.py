import os
#declarar variables
cliente,vendedor,polos,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
polos=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(polos*pu)
#verificador
cliente_estrella=(total>120)
#ouput

print("  BOLETA ELECTRONICA     ")
print("   RIPLEY        ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("polos:",polos ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional simple
#si es comprador compulsivo otorgar un descuento del 10%
if (cliente_estrella==True):
    print("GANASTE TARJETA DE PLATA ")
