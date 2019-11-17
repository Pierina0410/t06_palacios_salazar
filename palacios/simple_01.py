import os
#declarar variables
cliente,vendedor,fideos,pu="","",0.0,0.0
#imput
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
fideos=float(os.sys.argv[3])
pu= float(os.sys.argv[4])

#procesing
total=round(fideos*pu)
#verificador
comprador_compulsivo=(total>=50)
#ouput

print("  BOLETA ELECTRONICA      ")
print("   BODEGA LIBERTAD        ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("fideos:",fideos ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("   GRACIAS POR SU COMPRA    ")

#condicional simple
#si es comprador compulsivo otorgar un descuento del 10%
if (comprador_compulsivo==True):
    print("GANASTE 10% DE DESCUENTO ")
