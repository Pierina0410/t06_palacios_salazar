import os
# BOLETA DE VENTA
# Declara variables
cliente, arroz, p1, postre, p2="", 0, 0.0, 0, 0.0

cliente=os.sys.argv[1]
arroz=int(os.sys.argv[2])
p1=float(os.sys.argv[3])
postre=int(os.sys.argv[4])
p2=float(os.sys.argv[5])

# PROCESSING
total = (arroz*p1)+(postre*p2)

#VERIFICADOR
comprador_compulsivo=(arroz>10 and postre>10)

# OUTPUT
print ("#######################")
print ("# BOLETA DE VENTA")
print ("#######################")
print ("#")
print ("# Cliente:  ", cliente)
print ("#                    Nro")
print ("# Arroz con Pato:    ", arroz)
print ("# P.U:", p1)
print ("# Gelatina:          ", postre)
print ("# P.U:", p2)
print ("# Total  :  S/.", total)
print ("#######################")

# CONDICIONAL MULTIPLE
# si el comprador es compulsivo, mostrarle la tarjeta dorada
if (comprador_compulsivo==True):
    print ("GANASTE LA TARJETA PLATINO")

if (total>90):
    print ("GANO PREMIO SORPRESA")

if (total<90):
    print ("VUELVA PRONTO")
#fin_if
