import os
#Declarar variables
adquiriente,vendedor,televisor,pu="","",0,0.0
#imput
adquiriente=os.sys.argv[1]
vendedor=os.sys.argv[2]
televisor=int (os.sys.argv[3])
pu=float(os.sys.argv[4])

#procesing
total=(televisor*pu)
#Verificador
Cliente_fiel=(total>1800)

#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##  ELECTRA       ##")
print("# cliente:",adquiriente)
print("#vendedor:",vendedor)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#televisor:",televisor ,"unidades")
print("#p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
#Condicional simple
#si es un cliente fiel se ganara una olla arrocera
if (Cliente_fiel==True):
    print("FELICIDADES GANASTE UNA OLLA ARROCERA")
