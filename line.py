import math
def line():
    a= float(input("Ingrese el coeficiente A: "))
    b= float(input("Ingrese el coeficiente B: "))
    x1= float(input("Ingrese el coeficiente X1: "))
    x2= float(input("Ingrese el coeficiente X2: "))
    print("El coeficiente A de su ecuación de la recta es:",a)
    print("El coeficiente B de su ecuación de la recta es:",b)
    print("El coeficiente X1 de su ecuación de la recta es:",x1)
    print("El coeficiente X2 de su ecuación de la recta es:",x2)
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {a}X + {b}")
    y1= a * x1 + b
    y2= a * x2 + b
    print("")
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})")
    print("")
    distance=math.sqrt(math.pow(x2-x1,2)+ math.pow(y2-y1,2))
    print(f"La distancia entre ellos es: {distance}")
