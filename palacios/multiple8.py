import os
#declarar variables
cliente,vendedor,tortas,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
tortas=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(tortas*pu)
#verificador
por_compras=(total>20)
comprador_compulsivo= (total>100)
comprador_del_año=(total>320)
#ouput

print("  BOLETA ELECTRONICA     ")
print(" SERAFINA     ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("tortas:",tortas ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional multiple
#si es comprador recurrente otorgar 30% de descuento
if (por_compras==True):
    print("GANASTE UN DESCUENTO DEL 50% ")
#si fuiste el que más compro en el año te ganas 100 soles en compras
if (comprador_compulsivo==True):
    print("FELICIDADES GANASTE UNA CAJA DE CHOCOTEJAS")
#el comprador del año se gana 200 soles
if (comprador_del_año==True):
    print("TE GANASTE 200 SOLES")
