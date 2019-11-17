import os
#BOLETA
#Declaracion de variables
masa, velocidadluz, velocidadsol=0.0, 0.0, 0.0

masa=float(os.sys.argv[1])
velocidadluz=float(os.sys.argv[2])
velocidadsol=float(os.sys.argv[3])

#PROCESSING
area=(masa*velocidadluz*velocidadsol)

#VERIFICACIONES
area_compulsiva=(area>20)

#OUTPUT
print ("################################")
print ("# CALCULAR LA ENERGIA #")
print ("# MASA", masa)
print ("# VELCCIDAD DE LA LUZ:", velocidadluz)
print ("# VELOCIDAD DEL SOL:", velocidadsol)
print ("# EL AREA DEL CIRCULO ES:", area)
print ("#################################")

#CONDICIONAL DOBLE
#Si el area es compulsiva, mostrarle su bonificacion
if (area_compulsiva==True):
    print ("GANASTE TU BONIFICACION")

else:
    print ("SIGA AUMENTANDO SU AREA")
