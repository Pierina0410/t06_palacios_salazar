import os
#declarar variables
cliente,vendedor,jabones,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
jabones=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(jabones*pu)
#verificador
por_compras=(total>600)
comprador_compulsivo= (total>800)
comprador_del_año=(total>1000)
#ouput

print("  BOLETA ELECTRONICA     ")
print("   RIPLEY        ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("jabones:",jabones ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional multiple
#si es comprador recurrente otorgar 20% de descuento
if (por_compras==True):
    print("GANASTE UN DESCUENTO DEL 20% ")
#si fuiste el que más compro en el año te 1 caja de jabones
if (comprador_compulsivo==True):
    print("FELICIDADES GANASTE 1 CAJA DE JABONES")
#si fuiste el comprador del año te ganas una cajas de 245 jabones
if (comprador_del_año==True):
    print("TE GANASTE 1 CAJA DE JABONES")
