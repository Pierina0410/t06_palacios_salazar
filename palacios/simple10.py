import os
#declarar variables
cliente,vendedor,ceramica,pu="","",0.0,0.0
#imput
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
ceramica=float(os.sys.argv[3])
pu= float(os.sys.argv[4])

#procesing
total=round(ceramica*pu)
#verificador
comprador_estrella=(total>500)
comprador_del_año= (total>1200)
#ouput

print("  BOLETA ELECTRONICA      ")
print("  FERRETERIA        ")
print(" cliente:",cliente)
print("vendedor:",vendedor)
print("fecha=8/11/2019  Hora :8:50pm ")
print("ceramica:",ceramica ,"unidades")
print("p.u:",pu)
print("TOTAL:",total)
print("   GRACIAS POR SU COMPRA    ")

#condicional doble
#si es comprador compulsivo otorgar un descuento del 10%
if (comprador_estrella==True):
    print("GANASTE 10% DE DESCUENTO ")

