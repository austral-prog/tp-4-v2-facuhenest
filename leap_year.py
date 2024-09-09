def leap_year():
    año = input("Ingrese un año:")

    ye = int(año)  # Convierte el año a entero
    if (ye % 400 == 0) or (ye % 4 == 0 and ye % 100 != 0):
        print(f"El año {ye} es bisiesto")
    else:
        print(f"El año {ye} no es bisiesto")
