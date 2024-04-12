import math
def line():
    a= float(input("coeficiente a: "))
    b= float(input("coeficiente b: "))
    x1= float(input("coeficiente x1: "))
    x2= float(input("coeficiente x2: "))
    print("el coeficiente a de su ecuacion es:",a)
    print("el coeficiente b de su ecuacion es:",b)
    print("el coeficiente x1 de su ecuacion es:",x1)
    print("el coeficiente x2 de su ecuacion es:",x2)
    print("")
    print("para las siguientees ecuaciones:")
    print("y = ax + b")
    y1= a * x1 + b
    print("y1=", y1)
    y2= a * x2 + b
    print("y2=", y2)
    print("")
    print("dados los siguientes puntos:")
    distance=math.sqrt(math.pow(x2-x1,2)+ math.pow(y2-y1,2))
    print(f"la distancia entre ellos es: {distance}")
line()
