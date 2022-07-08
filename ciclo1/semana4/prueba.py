def ordenes(rutinaContable):
  
    pass




rutinaContable = [
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]
print('----------------- Inicio Registro diario --------------------------')
i = 0
while i < len(rutinaContable):
    numero = rutinaContable[i][0]
    cantidad = rutinaContable[i][1][2]+rutinaContable[i][2][2]+rutinaContable[i][3][2]
    print( f"La factura {numero} tiene un total en pesos de {cantidad:,.2f}")
    i += 1
print('----------------- Fin Registro diario -----------------------------')