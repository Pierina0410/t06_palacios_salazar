import os
#BOLETA DE VENTA
#Declaracion de variables
vendedor, cliente, celular, pu="", "", 0, 0.0

vendedor=os.sys.argv[1]
cliente=os.sys.argv[2]
celular=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total=(celular*pu)

#VERIFICACIONES
comprador_compulsivo=(celular>10)

#OUTPUT
print ("#################################")
print ("# VENTA DE ACCESORIOS PARA CARRO #")
print ("# CLIENTE:", cliente)
print ("# VENDEDOR:", vendedor)
print ("# CELULAR", celular)
print ("# P.U:", pu)
print ("# TOTAL:", total)
print ("##################################")

#CONDICIONAL DOBLE
#Si el comprador es compulsivo, mostrar la tarjeta dorada
if (comprador_compulsivo==True):
    print("GANASTE LA TARJETA DORADA")

else:
    print ("VUELVA PRONTO")

#FIN_IF
