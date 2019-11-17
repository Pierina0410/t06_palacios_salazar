import os
#BOLETA DE INVENTARIO
#DECLARAR VARIABLES
laboratorio, docente, computadoras, mouse, cpu="", "", 0, 0, 0

laboratorio=os.sys.argv[1]
docente=os.sys.argv[2]
computadoras=int(os.sys.argv[3])
mouse=int(os.sys.argv[4])
cpu=int(os.sys.argv[5])

#PROCESING
total=(computadoras+mouse+cpu)

#VERIFICADORES
inventario=(computadoras>10 and mouse>10 and cpu>10)

#OUTPUT
print ("###############################")
print ("## INVENTARIO DE LABORATORIO ##")
print ("# NOMBRE DEL LABORATORIO:", laboratorio)
print ("# DOCENTE:", docente)
print ("# FECHA: 12/11/2019    Hora: 9:27a.m")
print ("# COMPUTADORAS:", computadoras)
print ("# MOSUES:", mouse)
print ("# CPU:", cpu)
print ("#TOTAL DE ACCESORIOS:", total)
print ("################################")

#CONDICIONAL SIMPLE
#si el laboratorio presenta todos sus elementos, mostrarle un diploma
if (inventario==True):
    print ("OBTENGA SU DIPLOMA DE HONOR")
#FIN_IF
