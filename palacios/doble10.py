
import os
#declarar variables
cliente,vendedor,sandalias,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
sandalias=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(sandalias*pu)
#verificador
por_compras=(total>20)
comprador_compulsivo= (total>100)

#ouput

print("  BOLETA ELECTRONICA     ")
print(" PLATANITOS  ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("sandalias:",sandalias ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional doble
#si es comprador recurrente otorgar 2 cupones
if (por_compras==True):
    print("FELICIDADES GANASTE 2 CUPONES")
#si fuiste el que más compro en el año te ganas 1 par de tacos
if (comprador_compulsivo==True):
    print("FELICIDADES GANASTE 1 PAR DE TACOS")
