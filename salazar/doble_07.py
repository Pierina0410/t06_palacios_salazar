import os
#BOLETA DE VENTA
#Declarar variables
supervisor, cliente, vendedor, televisor, p1="", "", "", 0, 0.0

supervisor=os.sys.argv[1]
cliente=os.sys.argv[2]
vendedor=os.sys.argv[3]
televisor=int(os.sys.argv[4])
p1=float(os.sys.argv[5])

#PROCESSING
total=(televisor*p1)

#VERIFICACIONES
comprador_compulsivo=(televisor>10)

#OUTPUT
print ("#################################")
print ("#####  BOLETA ELECTRONICA  #####")
print ("######VENTA DE ARTEFACTOS#######")
print ("# SUPERVISOR:", supervisor)
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# TELEVISOR:", televisor)
print ("# P.U:", p1)
print ("# TOTAL:", total)
print ("##################################")

#CONDICIONAL DOBLE
#Si el comprador es compulsivo, mostrarle un premio
if (comprador_compulsivo==True):
    print ("GANASTE UN PREMIO")

else:
    print("GRACIAS POR LA PREFERENCIA")
#FIN_IF
