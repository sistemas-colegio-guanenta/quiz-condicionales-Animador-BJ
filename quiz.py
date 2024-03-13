# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")


# Input
a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

# Processing
es_triangulo = a + b > c and a + c > b and b + c > a

# Output
if es_triangulo:
    print(f"Estas longitudes ({a}, {b}, {c}) pueden formar un triángulo.")
else:
    print(f"Estas longitudes ({a}, {b}, {c}) no pueden formar un triángulo.")
