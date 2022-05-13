def desperdicio_de_gaseosa(amigo1, amigo2, amigo3, capcidad_boton):

    capacidad_rest1 = amigo1["capacidad_vaso"]-amigo1["capacidad_actual"] + capcidad_boton
    capacidad_rest2 = amigo2["capacidad_vaso"]-amigo2["capacidad_actual"] + capcidad_boton
    capacidad_rest3 = amigo3["capacidad_vaso"]-amigo3["capacidad_actual"] + capcidad_boton

    if(capcidad_boton > capacidad_rest1):
        mensaje =  amigo1["nombre"], "se le regó la gaseosa"
    elif(capcidad_boton > capacidad_rest2):
        mensaje =  amigo2["nombre"], "se le regó la gaseosa"
    elif(capcidad_boton > capacidad_rest3):
        mensaje =  amigo3["nombre"], "se le regó la gaseosa"
    return mensaje

amigo1 = {"nombre": "harold stiven", "capacidad_vaso": 10.0, "capacidad_actual": 5.5},
amigo2 = {"nombre":"camilo hernadez", "capacidad_vaso": 15.5, "capacidad_actual": 10.5},
amigo3 = {"nombre":"maria adelaida", "capacidad_vaso": 5.5, "capacidad_actual": 2.5}

print(desperdicio_de_gaseosa(amigo1, amigo2, amigo3, 5.0))

