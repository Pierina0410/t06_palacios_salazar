import os
#BOLETA DE VENTA
#Declarar variables
vendedor, cliente, llantas, p1, faros, p2="", "", 0, 0.0, 0, 0.0

vendedor=os.sys.argv[1]
cliente=os.sys.argv[2]
llantas=int(os.sys.argv[3])
p1=float(os.sys.argv[4])
faros=int(os.sys.argv[5])
p2=float(os.sys.argv[6])

#PROCESSING
total=(llantas*p1)+(faros*p2)

#VERIFICADOR
comprador_compulsivo=(total>120)
#OUTPUT
print ("#################################")
print ("# VENTA DE ACCESORIOS PARA CARRO #")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# Llantas", llantas)
print ("# P.U:", p1)
print ("# FAROS:", faros)
print ("# P.U:", p2)
print ("# TOTAL:", total)
print ("##################################")

#CONDICIONAL MULTIPLE
#Si es comprador compulsivo, mostrar la tarjeta de regalo
if (comprador_compulsivo==True):
    print ("GANASTE LA TARJETA DE REGALO")

if (total>200):
    print("HA GANADO UN DESCUENTO ESPECIAL")

if (total<200):
    print ("REALIZE MAS PUNTOS")
#fin_IF
