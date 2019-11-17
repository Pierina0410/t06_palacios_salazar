import os
#BOLETA DE AREA
#DECLARACION DE VARIABLES
pi, radio1, radio2=0.0, 0.0, 0.0

pi=float(os.sys.argv[1])
radio1=float(os.sys.argv[2])
radio2=float(os.sys.argv[3])

#PROCESSING
area=(pi*radio1*radio2)

#VERIFICADOR
area_compulsiva=(area>100)

#OUTPUT
print ("################################")
print ("# CALCULAR EL AREA DEL CIRCULO #")
print ("# PI:", pi)
print ("# RADIO 1:", radio1)
print ("# RADIO 2:", radio2)
print ("# EL AREA DEL CIRCULO ES:", area)
print ("#################################")

#CONDICIONAL MULTIPLE
#si el area es compulsiva, mostrarle su castigo
if (area_compulsiva==True):
    print ("HAZ GANADO UN CASTIGO")

if (area>80):
    print ("HA GANADO UNA MEDALLA DE ORO")

if (area<80):
    print("HA GANADO UNA MEDALLA DE PLATA")
#FIN_IF
