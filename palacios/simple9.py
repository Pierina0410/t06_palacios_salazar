import os
#declaración de variables
cliente,vendedor,alcancias,pu="","",0.0,0.0
#imput
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
alcancias =float(os.sys.argv[3])
pu=float(os.sys.argv[4])

#procesing
total=(alcancias*pu)
#veriricador
Comprador_compulsivo=(total>430)


#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##  MUEBLERIA COMODIDAD        ##")
print("# cliente:",cliente)
print("#vendedor:",vendedor)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#alcancias:",alcancias,"unidades")
print("#p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional simple
#si es comprador compulsivo otorgar cupones
if (Comprador_compulsivo==True):
    print("FELICIDADES GANÓ 100 soles en productos")

