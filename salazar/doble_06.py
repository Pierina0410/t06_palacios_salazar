import os
#BOLETA DE VENTA
#Declarar variables
recepcionista, cliente, cuarto1, pu="", "", 0.0, 0.0

recepcionista=os.sys.argv[1]
cliente=os.sys.argv[2]
cuarto1=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total=(cuarto1*pu)

#VERIFICACIONES
comprador_compulsivo=(total>50)

#OUTPUT
print ("#################################")
print ("#####  BOLETA ELECTRONICA  #####")
print ("###### HOTEL LA CASACADA #######")
print ("# CLIENTE:", cliente)
print ("# RECEPCIONISTA:", recepcionista)
print ("# HORAS DE CUARTO", cuarto1)
print ("# P.U:", pu)
print ("# TOTAL:", total)
print ("##################################")

#CONDICIONAL DOBLE
#Si el comprador es compulsivo, darle el 30% de descuento
if (comprador_compulsivo==True):
    print ("GANASTE EL 30% DE DESCUENTO")

else:
    print ("VUELVA PRONTO")
