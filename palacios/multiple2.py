import os
#declarar variables
cliente,vendedor,pollos,pu="","",0.0,0.0
#imput
cliente= os.sys.argv[1]
vendedor=os.sys.argv[2]
pollos=float(os.sys.argv[3])
pu=float (os.sys.argv[4])

#procesing
total=(pollos*pu)
#verificador
cliente_estrella=(total>120)
comprador_anual= (total>1200)
comprador_compulsivo=(total>456)
#ouput

print("  BOLETA ELECTRONICA     ")
print("   RIPLEY        ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("pollos:",pollos ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional multiple
#si es comprador recurrente otorgar una tarjeta
if (cliente_estrella==True):
    print("GANASTE TARJETA DE BRONCE")
#si fuiste el que más compro en el año te otorgaran una tarjeta de oro
if (comprador_anual==True):
    print("FELICIDADES GANASTE UNA TARJETA ORO")
#si eres comprador compulsivo te ganas 2 pollos
if (comprador_compulsivo==True):
    print("TE GANASTE 2 POLLOS")
