import os
#declarar variables
cliente,vendedor,clavos,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
clavos=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(clavos*pu)
#verificador
por_compras=(total>50)
comprador_compulsivo= (total>100)
comprador_del_año=(total>345)

#ouput

print("  BOLETA ELECTRONICA     ")
print("  FERRETERIA       ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("clavos:",clavos ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional multiple
#si es comprador recurrente otorgar 30% de descuento
if (por_compras==True):
    print("GANASTE UN DESCUENTO DEL 30% ")
#si fuiste el que más compro en el año te ganas 100 soles en compras
if (comprador_compulsivo==True):
    print("FELICIDADES GANASTE 100 SOLES EN COMPRAS")
#si fuiste el comprador del año te ganas un viaje al cusco
if (comprador_del_año==True):
    print("Te ganaste un viaje al cuzco")
