import os
#BOLETA DE VENTA
#Declarar variables
cliente, vendedor, tortas, pu="", "", 0, 0.0

cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
tortas=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESING
total=(tortas*pu)

#VERIFICADORES
comprador_compulsivo=(tortas>15)

#OUTPUT
print ("###############################")
print ("##     BOLETA ELECTRONICA    ##")
print ("#        PASTELERIA           #")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# FECHA: 09/11/2019    Hora: 17:27p.m")
print ("# TORTAS:", tortas,)
print ("# P.U:",    pu)
print ("# TOTAL:",   total)
print ("####  GRACIAS POR SU COMPRA  ###")
print ("################################")

#CONDICIONAL MULTIPLE
#si el comprador es compulsivo, mostrarle la tarjeta dorada
if (comprador_compulsivo==True):
    print ("GANASTE LA TARJETA DORADA")

if (total>60):
    print("GANASTE LA TARJETA PLATINO")

if (total<60):
    print ("VUELVA PRONTO")
#FIN_IF
