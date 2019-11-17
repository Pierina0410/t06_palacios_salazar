import os
#BOLETA DE ENERGIA
#Declarar variables
masa, gravedad, altura=0.0, 0.0, 0.0

masa=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
altura=float(os.sys.argv[3])

#PROCESSING
energia_cinetica=(masa*gravedad*altura)

#VERIFICACIONES
energia=(energia_cinetica>100)
#OUTPUT
print ("###############################")
print ("## CALCULAR ENERGIS CINETICA ##")
print ("# MASA:", masa)
print ("# GRAVEDAD:", gravedad)
print ("# ALTURA:", altura)
print ("# ENERGIA CINETICA:", energia_cinetica)
print ("################################")

#CONDICIONAL SIMPLE
#Si la energia cinetica es alta, mostrar su bonificacion
if (energia==True):
    print ("USTED HA GANADO SU BONIFICACION")
#FIN_IF
