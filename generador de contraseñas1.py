import random
import string


# programa principal 
def main():
    seguir = True

    while seguir:

        print("=== GENERADOR DE CONTRASEÑAS ===")

        longitud = int(input("ingrese la longitud de la contraseña: "))

        incluir_mayus = input("¿incluir mayúsculas? (s/n): ").lower() == "s"
        incluir_minus = (
                input("¿Incluir minúsculas? (s/n): ").lower() == "s")
        incluir_nums = input("Incluir números? (s/n): ").lower() == "s"
        incluir_simb = input("¿Incluir símbolos? (s/n): ").lower() == "s"

        contraseña = generar_password(longitud, incluir_mayus, incluir_minus, incluir_nums, incluir_simb)



        print("\nContraseña genrada:", contraseña)
        print("nivel de seguridad:", evaluar_seguridad(contraseña))

        otra = input("\nDesea generar otra contraseña? (s/n): ").lower()

        if otra != "s":
            seguir = False

        print()

    print("Programa finalizado.")


# funcion que genera la contraseña
def generar_password(longitud, mayus, minus, nums, simb):

    caracteres = ""

    if mayus:
        caracteres += (
            string.ascii_uppercase)
    if minus:
        caracteres += string.ascii_lowercase
    if nums:
        caracteres += (
            string.digits)
    if simb:
        caracteres += string.punctuation

    if caracteres == "":
        return "Error: Debe seleccionar al menos un tipo de carácter"

    password = ""

    for i in range(longitud):
        password += random.choice(caracteres)

    return password


# funcion para evaluar qué tan segura es
def evaluar_seguridad(password):

    if len(password) >= 12:
        return "Alta"
    elif len(password) >= 8:
        return "Media"

    else:
        return "Baja"


main()
