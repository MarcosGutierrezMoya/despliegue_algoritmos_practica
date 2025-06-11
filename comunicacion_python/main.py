from functions import addOperation, personalData

def main():
    print("Eejcutamos el main")

    # Datos personales
    name = input("Introduce tu nombre: ")
    age = int(input("Introduce tu edad: "))
    country = input("Introduce tu país: ")
    data = personalData(name, age, country)
    print(f"O sea que te llamas {data['Name']}, tienes {data['Age']} años y vives en {data['Country']}.")

    # Operación de suma
    a = int(input("Introduce el primer número para sumar: "))
    b = int(input("Introduce el segundo número para sumar: "))
    result = addOperation(a, b)
    print(f"La suma de {a} y {b} es: {result}")

if __name__ == '__main__': 
  main()