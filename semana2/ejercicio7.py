def sistema_op(opcion: str):
  opcion = opcion.lower()
  if(opcion == "a"):
    mensaje = "El sistema operativo es Android"
  elif(opcion == "i"):
      mensaje = "El sistema operativo es IOS"
  else:
    mensaje = "Opcion inválida"
  return mensaje

opcion = input("Escoja un sistema (a = Android) (i= IOS): ")
print(sistema_op(opcion))
