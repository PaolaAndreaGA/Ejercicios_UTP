from functools import reduce

def ordenes(rutinaContable):
    my_list = []
    for i in rutinaContable:
        my_list.append(i.pop(0))
    list_2 = []
    for j in rutinaContable:
        list_2.append(reduce(lambda x,y:x+y,(list(map(lambda x:x[1]*x[2], j)))))
    list_2 = [x + 25000 if x < 600000 else x for x in list_2]
    resultado = list(zip(my_list, list_2))

    salida = "------------------------ Inicio Registro diario ---------------------------------\n"
    for y in resultado:
        salida += f"La factura {y[0]} tiene un total en pesos de {y[1]:,.2f}\n"
    salida += "-------------------------- Fin Registro diario ----------------------------------"

    return print(salida)

rutinaContable = [
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]
ordenes(rutinaContable)