import os
#BOLETA
#DECLARAR VARIABLES
vendedor, cliente, pastel1, p1, pastel2, p2="", "", 0, 0.0, 0, 0.0

vendedor=os.sys.argv[1]
cliente=os.sys.argv[2]
pastel1=int(os.sys.argv[3])
p1=float(os.sys.argv[4])
pastel2=int(os.sys.argv[5])
p2=float(os.sys.argv[6])

#PROCESSING
total=(pastel1*p1)+(pastel2*p2)

#VERIFICADORES
comprador_compulsivo=(pastel1>8 and pastel2>8)

#OUTPUT
print ("#################################")
print ("####   BOLETA ELECTRONICA   ####")
print ("####  PASTELERIA RICO SABOR  ####")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# TORTA TRES LECHES:", pastel1)
print ("# P.U:", p1)
print ("# TORTA DE CHOCOLATE:", pastel2)
print ("# P.U:", p2)
print ("# TOTAL:", total)
print ("##### GRACIAS POR SU COMPRA #####")
print ("#################################")

#CONDICIONAL MULTIPLE
#si el comprador es compulsivo, mostrarle el 30% de descuento
if (comprador_compulsivo==True):
    print ("GANASTE EL 30% DE DESCUENTO")

if (total>100):
    print ("GANASTE TARJETA DORADA")

if (total<100):
    print ("GANASTE MEDALLA")
#FIN_IF
