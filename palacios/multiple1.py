import os
#declarar variables
cliente,vendedor,laptos,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
laptos=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(laptos*pu)
#verificador
cliente_estrella=(total>120)
comprador_anual= (total>1200)
comprador_compulsivo=(total>560)
#ouput

print("  BOLETA ELECTRONICA     ")
print("   RIPLEY        ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("laptos:",laptos ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional triple
#si es comprador recurrente otorgar un descuento del 10%
if (cliente_estrella==True):
    print("GANASTE TARJETA DE PLATA ")
#si fuiste el que más compro en el año
if (comprador_anual==True):
    print("FELICIDADES GANASTE UNA TARJETA LIBERADA")
#si eres comprador compulsivo te ganas 100 soles en productos
if (comprador_compulsivo==True):
    print("TE GANASTE 100 SOLES EN PRODUCTOS")
