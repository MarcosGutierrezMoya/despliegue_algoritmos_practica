def main():
    print("Eejcutamos el main")

    # Datos personales
    name = input("Introduce tu nombre: ")
    age = int(input("Introduce tu edad: "))
    country = input("Introduce tu país: ")
    print(f"O sea que te llamas {name}, tienes {age} años y vives en {country}.")

    # Operación de suma
    a = int(input("Introduce el primer número para sumar: "))
    b = int(input("Introduce el segundo número para sumar: "))
    print(f"La suma de {a} y {b} es: {a + b}")

if __name__ == '__main__': 
  main()