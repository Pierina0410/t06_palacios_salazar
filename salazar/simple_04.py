import os
#BOLETA DE VENTA
#Declarar variavles
alumno, docente, nota1, nota2, nota3="", "", 0.0, 0.0, 0.0

alumno=os.sys.argv[1]
docente=os.sys.argv[2]
nota1=float(os.sys.argv[3])
nota2=float(os.sys.argv[4])
nota3=float(os.sys.argv[5])

#PROCCESING
promedio=(nota1+nota2+nota3)/3

#VERIFICADOR
promedio_final=(promedio>15)

#OUTPUT
print ("###########################")
print ("#    BOLETA DE NOTAS     ##")
print ("# ALUMNO:", alumno)
print ("# DOCENTE:", docente)
print ("# NOTA 1:    ", nota1)
print ("# NOTA 2:    ", nota2)
print ("# NOTA 3:    ", nota3)
print ("# PROMEDIO FINAL:", promedio)

#CONDICION SIMPLE
#si tiene buen promedio final, mostrarle diploma
if (promedio_final==True):
    print ("USTED HA GANADO SU DIPLOMA")
#FIN_IF
