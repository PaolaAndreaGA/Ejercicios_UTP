def cliente(informacion:dict)->dict:

    nombre = informacion['nombre']
    edad = informacion['edad']
    primer_ing = informacion['primer_ingreso']

    if (edad > 18) :
        atraccion = "X-Treme"
        apto = True
        valor_boleta = 20000
        if primer_ing == True:
            total_boleta  = valor_boleta - (valor_boleta * 0.05)
        else:
            total_boleta = valor_boleta
    elif(edad >= 15 and edad <= 18):
        atraccion = "Carros chocones"
        apto = True
        valor_boleta = 5000
        if primer_ing== True:
            total_boleta  = valor_boleta - (valor_boleta * 0.07)
        else:
            total_boleta = valor_boleta
    elif(edad >= 7 and edad <= 15):
        atraccion = "Sillas voladoras"
        apto = True
        valor_boleta = 10000
        if primer_ing == True:
            total_boleta  = valor_boleta - (valor_boleta * 0.05)
        else:
            total_boleta = valor_boleta
    else:
        atraccion = "N/A"
        apto = False
        total_boleta = "N/A"

    mi_dict = {'nombre': nombre , 'edad': edad, 'atraccion': atraccion, 'apto': apto, 'primer_ingreso': primer_ing, 'total_boleta': total_boleta  }
    return mi_dict

informacion = {'id_cliente': 1,'nombre': 'Tatiana Suarez', 'edad': 7,'primer_ingreso': False}
print(cliente(informacion))
