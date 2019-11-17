import os
#BOLETA DE VENTA
#Declaracion de variables
cliente, vendedor, mesas, p1="", "", 0, 0.0

cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
mesas=int(os.sys.argv[3])
p1=float(os.sys.argv[4])

#PROCESSING
total=(mesas*p1)

#VERIFICACIONES
comprador_compulsivo=(mesas>20)

#OUTPUT
print ("#################################")
print ("#####  BOLETA ELECTRONICA  #####")
print ("###### MADERERA MI ROSITA ######")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# MESAS:", mesas)
print ("# P.U:", p1)
print ("# TOTAL:", total)
print ("##################################")

#CONDICIONAL DOBLES
#Si el comprador es compulsivo, mostrarle un regalo
if (comprador_compulsivo==True):
    print ("GANASTE UN REGALO")

else:
    print ("NO DEJE DE SEGUIR COMPRANDO")
#FIN_IF
