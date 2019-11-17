import os
#BOLETA DE MASA
#Declaracion de variables
alumno, peso, talla="", 0.0, 0.0

alumno:os.sys.argv[1]
peso=float(os.sys.argv[2])
talla=float(os.sys.argv[3])

#PROCESSING
indice=(peso+talla)/2

#VERIFICACIONES
indice_compulsivo=(indice>50)

#OUTPUT
print ("#####################################")
print ("#CALCULAR EL INDICE DE MASA CORPORAL#")
print ("# PESO", peso)
print ("# TALLA:", talla)
print ("# INDICE DE MASA CORPORAL:", indice)
print ("#################################")

#CONDICIONAL DOBLE
#Si el indice es compulsivo, mostrarle un premio
if (indice_compulsivo==True):
    print ("GANASTE UN PREMIO SORPRESA")

else:
    print ("SIGA BAJANDO DE PESO")
#FIN_IF
