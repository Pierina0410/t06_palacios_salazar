import os
#declaración de variables
cliente,vendedor,muebles,pu="","",0.0,0.0
#imput
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
muebles =float(os.sys.argv[3])
pu=float(os.sys.argv[4])

#procesing
total=(muebles*pu)
#veriricador
Comprador_compulsivo=(total>240)


#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##  MUEBLERIA COMODIDAD        ##")
print("# cliente:",cliente)
print("#vendedor:",vendedor)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#muebles:",muebles,"unidades")
print("#p.u:",pu)
print("#sillas:",sillas,"unidades")
print("#precio:",precio)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#condicional simple
#si es comprador compulsivo otorgar cupones
if (Comprador_compulsivo==True):
    print("FELICIDADES GANÓ 10 CUPONES")
