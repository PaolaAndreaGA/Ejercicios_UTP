# Diseñe un algoritmo que determina si un número es par o impar.
# Recuerde que un número es par si el resto de una división entera
# con el número 2 es cero.

val_num = int(input("Ingrese un numero: "))
val_num = abs(val_num)
val_modulo = val_num % 2

if(val_modulo == 0):
    print(f"El número {val_num} es par")
else:
  print(f"El número {val_num} es impar")
