import os
#declarar variables
cliente,vendedor,jeans,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
jeans=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(jeans*pu)
#verificador
por_compras=(total>200)
comprador_compulsivo= (total>200)
comprador_anual=(total>600)

#ouput

print("  BOLETA ELECTRONICA     ")
print("  Boutique       ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("jeans:",jeans ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional multiple
#si es comprador recurrente puedes participar del sorteo de un carro
if (por_compras==True):
    print("AHORA PUEDES PARTICIPAR DEL SORTEO DE UN TOYOTA ")
#si fuiste el que más compro en el año te ganas una docena de jeans
if (comprador_compulsivo==True):
    print("FELICIDADES GANASTE 12 JEANS")
#si compraste más que todos te ganas un pase para el concierto de tini
if (comprador_anual==True):
    print("TE GANASTE UN PASE PARA EL CONCIERTO DE TINI")
