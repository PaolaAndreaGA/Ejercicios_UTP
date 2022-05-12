#Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0.
#El algoritmo debe imprimir el valor ingresado, y de ser una nota mayor o igual a 4.0,
#deberá imprimir un mensaje de felicitaciones.

def nota_definitiva(nota: float):

    if not isinstance(nota, float) and not isinstance(nota, int):
        return ("la nota debe ser un decimal")


    if(nota < 0.0 or nota > 5.0):
        return (f"la nota : {nota:.1f} está fuera del rango, por favor ingrese una nota entre 0.0 y 5.0")

    if(nota >= 4.0):
        mensaje = (f"su nota es: {nota:.1f} ¡Felicitaciones!")
    else:
        mensaje  = (f"su nota es: {nota:.1f}, esfuerzate un poco más, ¡tú puedes!")
    return mensaje

nota = float(input("ingrese su nota entre 0.0 y 5.0: "))
mensaje_final = nota_definitiva
print(mensaje_final(nota))
