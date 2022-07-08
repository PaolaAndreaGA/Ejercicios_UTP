# Diseñe un algoritmo que permita solicitar tanto el nombre como la edad de una persona
# y posteriormente indicar si es “Mayor de edad” o “Menor de edad”
# según la información ingresada. Una persona se considera mayor de edad si tiene 18 años o más.

edad = int(input("cuantos años tiene?: "))
if(edad >= 0):
  if(edad >= 18):
    print (f"su edad es: {edad} años, ¡Usted es mayor de edad!")
  else:
    print (f"su edad es: {edad} años, ¡Usted es menor de edad!")
