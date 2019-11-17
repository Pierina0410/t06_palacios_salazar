import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente, vendedor, clavos, pu="", "", 0.0, 0.0

cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
clavos=float(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESING
total=(clavos*pu)

#VERIFICADOR
comprador_compulsivo=(clavos>10)

#OUTPUT
print ("###############################")
print ("##     BOLETA ELECTRONICA    ##")
print ("#      FERRETERIA OFERTON     #")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# FECHA: 0""8/11/2019    Hora: 9:27a.m")
print ("# CLAVOS:", clavos, "docenas")
print ("# P.U:",    pu)
print ("# TOTAL:",   total)
print ("####  GRACIAS POR SU COMPRA  ###")
print ("################################")

#CONDICIONAL SIMPLE
#si el comprador es compulsivo, mostrarle su regalo sorpresa
if (comprador_compulsivo==True):
    print ("GANASTE EL REGALO SORPRESA")

else:
    print ("Lo esperamos pronto")
#fin_if
