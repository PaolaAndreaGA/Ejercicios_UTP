def cobro_fact(estrato: int, m3: float):
  if(estrato < 0 or estrato > 6):
    return "Estrato no valido, ingrese un estrato entre 1 y 6"
  if (m3 < 0):
    return "Consumo no valido, ingrese un consumo mayor o igual 0"

  tarifa = {
        1 :{"cargo_fijo" : 2500, 'mts_consumo' : 2200, "basuras" : 5500},
        2 :{"cargo_fijo" : 2800, 'mts_consumo' : 2350, "basuras" : 6200},
        3 :{"cargo_fijo" : 3000, 'mts_consumo' : 2600, "basuras" : 7400},
        4 :{"cargo_fijo" : 3300, 'mts_consumo' : 3400, "basuras" : 8600},
        5 :{"cargo_fijo" : 3700, 'mts_consumo' : 3900, "basuras" : 9700},
        6 :{"cargo_fijo" : 4400, 'mts_consumo' : 4800, "basuras" : 11000}
  }

  valor_recibo = tarifa[estrato]["cargo_fijo"]
  valor_recibo +=  m3 * tarifa[estrato]["mts_consumo"]
  valor_recibo += tarifa[estrato]["basuras"]
  return valor_recibo

estrato = int(input("Ingrese el estrato: "))
m3 = float(input("Ingrese su consumo en Metros cubicos (m3): "))
print(cobro_fact(estrato, m3))