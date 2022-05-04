
def CDT(usuario:str, capital: int, tiempo: int):
    """
        Función que reciba como parámetros:
        

    """

    if tiempo > 2:
        porc_int = 0.03
        valor_int = int(capital * porc_int * tiempo)/12
        valor_total = int(capital + valor_int)
    else:
        penalizacion = 0.02
        valor_perd = capital * penalizacion
        valor_total = capital - valor_perd


    return valor_total

usuario = input("Digite su nombre de usuario: ")
capital = int(input("Digite el valor de su capital: "))
tiempo = int(input("Digite tiempo: "))
info_cdt = CDT(usuario, capital, tiempo)

print('Para el usuario {}', usuario, 'La cantidad de dinero a recibir, según el monto inicial {} ', capital, 'para un tiempo de ', tiempo, 'meses es: {}', info_cdt)