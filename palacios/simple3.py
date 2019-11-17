import os
#Declarar variables
comprador,empleado,yogurt,precio="","",0,0.0
#imput
comprador=os.sys.argv[1]
empleado=os.sys.argv[2]
yogurt=int(os.sys.argv[3])
precio=float(os.sys.argv[4])

#procesing

total2=(yogurt*precio)

#verificador
Cliente_recurrente=(total2>120)
#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##   BODEGA LIBERTAD        ##")
print("# cliente:",cliente)
print("#vendedor:",empleado)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#yogurt:",yogurt,"unidades")
print("#precio:",precio)
print("TOTAL:",total2)

#condicional simple
#si es comprador compulsivo otorgar un descuento del 10%
if (Cliente_recurrente==True):
    print("GANASTE UNA TARJETA VIP")



