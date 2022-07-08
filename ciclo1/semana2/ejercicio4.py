# Diseñe un algoritmo que determina si un número es par o impar.
# Recuerde que un número es par si el resto de una división entera
# con el número 2 es cero.

def num_par_impar(val_num: int):

  if not isinstance(val_num, int):
    return ("numero debe ser entero")

  val_num = abs(val_num)
  val_modulo = val_num % 2

  if(val_modulo == 0):
    mensaje = (f"El número {val_num} es par")
  else:
    mensaje = (f"El número {val_num} es impar")
  return mensaje

val_num = int(input("Ingrese un numero: "))
print(num_par_impar(val_num))
