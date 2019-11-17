import os
#declarar variables
cliente,vendedor,cereales,pu="","",0.0,0.0

#imput
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
cereales=int (os.sys.argv[3])
pu=float(os.sys.argv[4])

#procesing
total=(cereales*pu)
#verificador
caserito=(total>=120)

#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##   BODEGA LIBERTAD        ##")
print("# cliente:",cliente)
print("#vendedor:",vendedor)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#cereales:",cereales ,"unidades")
print("#p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional simple
#si es comprador compulsivo otorgar un descuento del 10%
if (caserito==True):
    print("GANASTE UNA CANASTA NAVIDEÑA")

