def AutoPartes(ventas: list):
    result = {}
    for i in range(len(ventas)):
        result[i] = [ventas[i]]
    return result

def consultaRegistro(ventas, idProducto):
    result2 = {}
    for x in ventas:
        if idProducto == ventas[x][0][0]:
            result2[x] = ventas[x]
    result3 = ''
    if len(result2) == 0:
        result3 = 'No hay registro de venta de ese producto'
    else:
        for x in result2:
            result3 += f"Producto consultado:  {ventas[x][0][0]} Descripción  {ventas[x][0][1]} #Parte  {ventas[x][0][2]} Cantidad vendida  {ventas[x][0][3]} Stock {ventas[x][0][4]} Comprador  {ventas[x][0][5]} Documento  {ventas[x][0][6]} Fecha Venta  {ventas[x][0][7]} \n"
    return print(result3)


consultaRegistro(AutoPartes([(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
