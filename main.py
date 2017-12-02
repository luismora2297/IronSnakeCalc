"""
	Luis Mora @ fobos
	Gianfranco Quiodetti @ laptop1
	Manuel Serna @ latop2
	Developed by BlackBohr Vyperion Team
	Apache License 2.0
	IronSnake is a numerical methods calculator with various functions able to do most of
	the many methods explained in the book 'Applied Numerical Methods in C by Shoichiro Nakamura'
"""

# Begin Imports 
import sys 
import numpy 

# Begin App 
IronCalcLagrangeInterpolate = True 
print("Bienvenido al programa de Interpolación de Lagrange") 
while IronCalcLagrangeInterpolate: 
    validate = True
    while validate: 
        # Petición de cantidad de números a interpolar 
        xyz = input("Introduzca la cantidad de números a interpolar: ")
        try: 
            i = int(xyz) 
            # Confirmando nuestra cantidad de números a interpolar 
            # print(i) 
            # Condición que tiene nuestro metodo 
            if i > 4: 
                print("Advertencia, utilizar el metodo de interpolación de Lagrange para más de 4 datos, esta data puede quedar obsoleta o incorrecta en su precisión.") 
            break 
        except ValueError: 
            print("Número no valido... ") 
 
    while validate: 
        # Valor que le pedimos al usuario para hacer el calculo de interpolación con Lagrange 
        xenter = input("Introduzca valor de interpolación X: ") 
        try: 
            xvalue = float(xenter) 
            # Confirmando nuestra cantidad de números a interpolar 
            # print(xvalue) 
            break 
        except ValueError: 
            print("Número no valido... ") 
 
    # Inicializando arrays en Python 3 
    lg = [] 
    fx = [] 
 
    # Pedimos los números independientes 
    x = 1 
    for x in range(i): 
        while x < i: 
            xyu = input("Introduzca el número independiente: ") 
            try: 
                x = float(xyu) 
                lg.append(x) 
                x += 1 
            except ValueError: 
                print("Número incorrecto, introduzca denuevo el número") 
    # Impresión para verificación 
    # print(len(lg)) 
    # print(*lg) 
 
    # Pedimos los números dependientes 
    y = 1 
    for y in range(i): 
        while y < i: 
            try: 
                y = float(input("Introduzca el número dependiente: ")) 
                fx.append(y) 
                y += 1 
            except ValueError: 
                print("Número incorrecto, introduzca denuevo número") 
    # Impresión para verificación 
    # print(len(fx)) 
    # print(*fx) 
    # Imprimir tabla 
    print("i    x   f(x)") 
    z = 0 
    for number1, number2 in zip(lg, fx): 
        rowprint = str(z) + "   "+str(number1)+"  "+str(number2) 
        z += 1 
        print ( rowprint ) 
 
    # Aplicando la formula de Lagrange
    U = fx
    T = lg
    equation = 0
    for j in range(len(lg)):
        # print(U[j])
        equation_t = U[j]
        for k in range(len(lg)):
            if k == j:
                continue
            fac = T[j] - T[k]
            # print(fac)
            polynomium = numpy.poly1d([1.0, -T[k]])
            # print(polynomium)
            equation_t *= polynomium / fac
            # print(equation_t)
        equation += equation_t
        # print(equation)
    print(equation)

    ironSnakeLagrangeEval = numpy.polyval(equation,  eval(xenter))

    print(ironSnakeLagrangeEval)
    # Fin del programa
    IronCalcLagrangeInterpolate = False
# Sale del programa
sys.exit(0)

