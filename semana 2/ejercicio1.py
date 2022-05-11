#Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0.
#El algoritmo debe imprimir el valor ingresado, y de ser una nota mayor o igual a 4.0,
#deberá imprimir un mensaje de felicitaciones.

nota = float(input("ingrese su nota entre 0.0 y 5.0: "))
if(nota >= 0.0 and nota <= 5.0):
  if(nota >= 4.0):
    print (f"su nota es: {nota:.1f} ¡Felicitaciones!")
  else:
    print (f"su nota es: {nota:.1f}, esfuerzate un poco más, ¡tú puedes!")
else:
  print (f"la nota : {nota:.1f} está fuera del rango, por favor ingrese una nota entre 0.0 y 5.0")

