from cgi import print_form
import math


print("Risolvo l'equazione a x^2 + b x + c = 0")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if not math.isclose(a, 0.0):
    # a != 0 => secondo grado
    delta = b**2 - 4*a*c
    if math.isclose(delta, 0.0):
        # una soluzione
        x = -b / (2*a) 
        print(f"Una soluzione: {x:.3f}")
    elif delta > 0.0:
        # due soluzioni
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print(f"Due soluzioni: {x1:.3f} e {x2:.3f}")
    else:
        # nessuna soluzione
        print("Nessuna soluzione reale")
else:
    # a == 0 => primo grado
    if not math.isclose(b, 0.0):
        # b != 0
        x = - c / b
        print(f"Una soluzione: {x:.3f}")
    else:
        # b == 0
        if math.isclose(c, 0.0):
            print("Equazione indeterminata")
        else:
            # c != 0
            print("Equazione impossibile")