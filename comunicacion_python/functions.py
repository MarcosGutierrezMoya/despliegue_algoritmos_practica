def personalData(name:str, age:int, country:str) -> dir:
    """"
    Recoje los datos personales del usuario y los devuelve en un directorio.
    """
    data = {
        'Name': name,
        'Age': age,
        'Country': country
    }
    return data

def addOperation(a: int, b: int) -> int:
    """
    Suma dos números enteros y devuelve el resultado.
    """
    return a + b