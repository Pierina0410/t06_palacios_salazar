import os
#BOLETA DE VENTA
#Declaracion de variables
mesero, cliente, cabrito, p1="", "", 0, 0.0

mesero=os.sys.argv[1]
cliente=os.sys.argv[2]
cabrito=int(os.sys.argv[3])
p1=float(os.sys.argv[4])

#PROCESSING
total=(cabrito*p1)

#VERIFICACIONES
comprador_compulsivo=(cabrito>10)

#OUTPUT
print ("#################################")
print ("##### RESTAURANT EL CHOLITO #####")
print ("# CLIENTE:", cliente)
print ("# MESERO:", mesero)
print ("# CABRITO", cabrito)
print ("# P.U:", p1)
print ("# TOTAL:", total)
print ("##################################")

#CONDICIONAL DOBLE
#Si el comprador es compulsivo, mostrarle su descuento
if (comprador_compulsivo==True):
    print ("GANASTE UN DESCUENTO EN TU PROXIMA COMPRA")

else:
    print ("REGRESE LO MAS PRONTO")

#FIN_IF
