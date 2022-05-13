def desperdicio_de_gaseosa (amigo1,amigo2,amigo3,capcidad_boton):

    capacidad_final_amigo1 = amigo1["capacidad_vaso"]-amigo1["capacidad_actual"] + capcidad_boton
    capacidad_final_amigo2 = amigo2["capacidad_vaso"]-amigo2["capacidad_actual"] + capcidad_boton
    capacidad_final_amigo3 = amigo3["capacidad_vaso"]-amigo3["capacidad_actual"] + capcidad_boton

    capacidad_3_amigos = min(capacidad_final_amigo1, capacidad_final_amigo2, capacidad_final_amigo3)

    if ((capacidad_final_amigo1 <= amigo1["capacidad_vaso"]) and (capacidad_final_amigo2 <= amigo2["capacidad_vaso"]) 
        and (capacidad_final_amigo3 <= amigo3["capacidad_vaso"])):
        return None
    elif (capacidad_3_amigos == capacidad_final_amigo1):
        usuario = amigo1["nombre"]
        return f"Al amig@ {usuario} se le riega primero el vaso"
    elif(capacidad_3_amigos == capacidad_final_amigo2):
        usuario = amigo2["nombre"]
        return f"Al amig@ {usuario} se le riega primero el vaso"
    elif(capacidad_3_amigos == capacidad_final_amigo3):
        usuario = amigo3["nombre"]
        return f"Al amig@ {usuario} se le riega primero el vaso"

amigo1 = {"nombre": "harold stiven", "capacidad_vaso": 10.0, "capacidad_actual": 5.5},
amigo2 = {"nombre":"camilo hernadez", "capacidad_vaso": 15.5, "capacidad_actual": 10.5},
amigo3 = {"nombre":"maria adelaida", "capacidad_vaso": 5.5, "capacidad_actual": 2.5}

print(desperdicio_de_gaseosa(amigo1, amigo2, amigo3, 5.0))
