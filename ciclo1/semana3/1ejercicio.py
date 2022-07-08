#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

def cifra_par(n: int):
  if n < 10:
    return "ingrese un numero mayor a 9"
  else:
    a = n / 10
    a =  round(a)
    b = a % 2
    c = n % 10
    d = c % 2
    if b == 0 and c == 0:
      mensaje = f"los digitos de {n} son {a} {b} y {c} y son pares"
    else:
      mensaje = f" {a} {b} {c} {d}"
    return mensaje

n = int(input("ingrese un numero de dos cifras: "))
print (cifra_par(n))