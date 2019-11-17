import os
# BOLETA DE VENTA
#DECLARAR VARIABLES
cliente, kg, pu="", 0.0, 0.0

cliente=os.sys.argv[1]
kg=float(os.sys.argv[2])
pu=float(os.sys.argv[3])

# PROCESSING
total=(pu*kg)

# VERIFICADOR
comprador_compulsivo=(kg>20)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("# Cliente:  ", cliente)
print("# Item   :  ",kg,"  kg mandarina")
print("# P.U.   :  S/.", pu)
print("# Total  :  S/.", total)
print("#######################")

# CONDICIONAL SIMPLE
# si el comprador es compulsivo, mostrarle la medalla de oro
if (comprador_compulsivo==True):
    print ("GANASTE LA MEDALLA DE ORO")
#FIN_IF
