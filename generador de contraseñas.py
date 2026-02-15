import random
import string

# Función para generar la contraseña
def generar_password(longitud, mayusculas, minusculas, numeros, simbolos):
    caracteres = ""

    # Estructuras condicionales para construir el conjunto de caracteres
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    # Validación básica
    if not caracteres:
        return "Error: Debe seleccionar al menos un tipo de carácter."

    password = ""

    # Estructura repetitiva para construir la contraseña
    for _ in range(longitud):
        password += random.choice(caracteres)

    return password


# Función para evaluar el nivel de seguridad
def evaluar_seguridad(password):
    longitud = len(password)

    if longitud >= 12:
        return "Alta"
    elif longitud >= 8:
        return "Media"
    else:
        return "Baja"


# Programa principal
def main():
    continuar = True

    while continuar:  # Estructura repetitiva principal

        print("=== GENERADOR SEGURO DE CONTRASEÑAS ===")

        longitud = int(input("Ingrese la longitud de la contraseña: "))

        mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
        minus = input("¿Incluir minúsculas? (s/n): ").lower() == "s"
        nums = input("¿Incluir números? (s/n): ").lower() == "s"
        simb = input("¿Incluir símbolos? (s/n): ").lower() == "s"

        password = generar_password(longitud, mayus, minus, nums, simb)

        print("\nContraseña generada:", password)
        print("Nivel de seguridad:", evaluar_seguridad(password))

        respuesta = input("\n¿Desea generar otra contraseña? (s/n): ").lower()
        continuar = respuesta == "s"

        print()

    print("Programa finalizado.")


if __name__ == "__main__":
    main()
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
