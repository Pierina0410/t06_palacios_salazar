import os
#Declaración de variables
comprador,vendedor,manteles,pu="","",0,0.0
#imput
comprador=os.sys.argv[1]
vendedor=os.sys.argv[2]
manteles =int (os.sys.argv[3])
pu=float(os.sys.argv[4])


#procesing
total=(manteles*pu)
#verificador
comprador_del_año=(total>280)

#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##  CASA HOGAR        ##")
print("# cliente:",comprador)
print("#vendedor:",vendedor)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#manteles:",manteles,"unidades")
print("#p.u:",pu)
print("Total",total)
print("#### GRACIAS POR SU COMPRA ###")

#Condicional simple
#Si el cliente es el comprador del año se le otorgara compras gracis por un dia
if (comprador_del_año==True):
    print("FELICIDADES GANÓ UN DIA DE COMPRAS GRATIS")
