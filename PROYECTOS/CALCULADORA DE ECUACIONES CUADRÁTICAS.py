import sys, math
#variables de los valores de la ecuación cuadrática (ax^2 + bx + c)
a=None
b=None
c=None
#solicitar el valor de las variablaes
print("Para carcular el discriminante de una ecuación cuadrática inserte los siguientes datos:")
a=int(input("valor de a: "))
b=int(input("valor de b: "))
c=int(input("valor de c: "))
#calcular el discriminante de una ecuación cuadrática
discriminante=(b*b)-4*a*c
print(f"El discriminante de tu ecuación es: {discriminante}")
#Determinar si hay respuesta
if discriminante >= 0:
    continuacion = int(input("¿Desea la/s soluciones de su ecuación? Inserte 1 para proseguir o 2 para finalizar el programa: "))
    if continuacion == 1:
        if discriminante > 0:
            x1 = (-b+math.sqrt(discriminante))/(2*a)
            x2 = (-b-math.sqrt(discriminante))/(2*a)
            print(f"las soluciones de su ecuación son: x1 = {x1}, x2 = {x2}")
        elif discriminante == 0:
            x = (-b)/(2*a)
            print(f"la solución de su ecuación es: {x}")
    elif continuacion == 2:
        sys.exit()
else:
    print("Su ecuación no tiene solución")
    sys.exit()


