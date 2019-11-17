
import os
#declarar variables
cliente,vendedor,chocotejas,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
chocotejas=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(chocotejas*pu)
#verificador
por_compras=(total>20)
comprador_compulsivo= (total>100)
cliente_del_año=(total>200)

#ouput

print("  BOLETA ELECTRONICA     ")
print(" SERAFINA     ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("chocotejas:",chocotejas ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional multiple
#si es comprador recurrente otorgar 2 cajas gratis
if (por_compras==True):
    print("FELICIDADES GANASTE 2 CAJA DE CHOCOTEJAS")
#si fuiste el que más compro en el año te ganas 3 cajas gratis
if (comprador_compulsivo==True):
    print("FELICIDADES GANASTE 3 CAJA DE CHOCOTEJAS")
#si fuiste el cliente del año te ganas una torta matrimonial
if (cliente_del_año==True):
    print("TE GANAS UNA TORTA MATRIMONIAL")
