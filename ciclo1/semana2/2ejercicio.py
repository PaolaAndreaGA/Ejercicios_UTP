# A un trabajador le pagan según sus horas trabajadas por una tarifa
# de pago por hora. Si la cantidad de horas trabajadas es mayor 40 horas.
# La tarifa se incrementa en un 50% para las horas extras.
# Calcular el salario del trabajador dadas las horas trabajadas
# y la tarifa ingresadas por el usuario.

def salario(horas: int, valor_hora: int):
  if(horas <= 40):
    total_salarios = (horas * valor_hora)
    mensaje = (f"Sus horas laboradas fueron: {horas}, su salario es: ${total_salarios}")
  if(horas > 40):
    horas_ordinarias = 40
    val_horas_ordinarias = (horas_ordinarias * valor_hora)
    horas_extras = (horas - horas_ordinarias)
    valor_extra = (valor_hora + (valor_hora * 0.5))
    val_horas_extras = (horas_extras * valor_extra)
    total_salario = val_horas_ordinarias + val_horas_extras
    mensaje = (f"Sus horas laboradas fueron: {horas},  sus horas extras fueron: {horas_extras}, el valor total de sus horas ordinarias fue: ${val_horas_ordinarias} y el valor total de sus horas extras fue: ${val_horas_extras}, su salario total es de: ${total_salario}")

  return (mensaje)

horas = int(input("Ingrese número de horas trabajadas: "))
valor_hora = int(input("ingrese el valor de la hora ordinaria: "))

print(salario(horas, valor_hora))