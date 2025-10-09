def saludar(nombre):
    return f"Hola {nombre}, este es un ejemplo de función en Python."

def sumar(a, b):
    """Suma dos números."""
    return a + b

def es_mayor_edad(edad):
    """Verifica si una persona es mayor de edad."""
    return edad >= 18

if __name__ == "__main__":
    print(saludar("Team"))
    print(f"La suma de 5 + 3 es: {sumar(5, 3)}")
    print(f"¿Una persona de 20 años es mayor de edad? {es_mayor_edad(20)}")