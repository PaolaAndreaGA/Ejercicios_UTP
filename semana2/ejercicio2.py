#Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0.
# El algoritmo debe imprimir el valor ingresado, y un mensaje que indique si el estudiante “Ganó el curso”
# o “Perdió el curso”. Se gana el curso solo si la nota definitiva es mayor o igual a 3.0..

nota = float(input("ingrese su nota entre 0.0 y 5.0: "))
if(nota >= 0.0 and nota <= 5.0):
  if(nota >= 3.0):
    print (f"su nota es: {nota} ¡Felicitaciones usted ganó el curso!")
  else:
    print (f"su nota es: {nota}, lo sentimos, usted ha perdido el curso")
else:
  print (f"la nota : {nota} está fuera del rango, por favor ingrese una nota entre 0.0 y 5.0") 