import os
#BOLETA DE VENTA
#Declaracion de variables
vendedor, cliente, sandia, pu="", "", 0, 0.0

vendedor=os.sys.argv[1]
cliente=os.sys.argv[2]
sandia=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total=(pu*sandia)

#VERIFICACION
comprador_compulsivo=(sandia>15)

#OUTPUT
print ("#################################")
print ("# VENTA DE SANDIAS #")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# SANDIA", sandia)
print ("# P.U:", pu)
print ("# TOTAL:", total)
print ("##################################")

#CONDICIONAL DOBLE
#Si el comprador es compulsivo, mostrarle la tarjeta platino
if (comprador_compulsivo==True):
    print ("GANASTE LA TARJETA PLATINO")

else:
    print ("NO DEJE DE COMPRAR")
