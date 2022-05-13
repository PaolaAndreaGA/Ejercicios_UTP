#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
def num_par_impar(val_num: int):
  
  if not isinstance(val_num, int):
    return ("numero debe ser entero")
  if (val_num < 10 or val_num > 100):
    val_num = abs(val_num)
    val_modulo = val_num % 2
  if(val_modulo == 0):
    mensaje = (f"El número {val_num} es par")
  else:
    mensaje = (f"El número {val_num} es impar")
  return mensaje

val_num = int(input("Ingrese un numero: "))
print(num_par_impar(val_num))
