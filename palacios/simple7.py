import os
#Declarar variables
cliente,empleado,yogurt,precio="","",0.0,0.0
#imput
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
juguetes=float(os.sys.argv[3])
pu=float(os.sys.argv[4])

#procesing
total=(juguetes*pu)
#verificador
Cliente_preferido=(total>120)

#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##   JUGUETERIA DIVERSION      ##")
print("# cliente:",cliente)
print("#vendedor:",vendedor)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#juguetes:",juguetes ,"docenas")
print("#p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
if (Cliente_preferido==True):
    print("GANASTE UNA TARJETA VIP")
