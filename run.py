from archivos.archivo import MiArchivo
from modelado.busquedabinaria import *
# crear objeto de miarchivo
obj = MiArchivo()
list = obj.obtener_informacion()
list = [x.split(",") for x in list]
# se cre a una lista vacia 
list2 = []
for x in list:
    for obj in x:
        # separamos las listas 
        list2.append(int (obj))
# realiozamos el ordenamiento 
list2.sort()
print(list2)
llamar = busquedabinaria(list2)
numero= int(input("ingrese el  valor :"))
print(llamar.BusquedaBinaria(numero))
