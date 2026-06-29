import os


def main():
    nombre = os.getenv("USERNAME", "Usuario")
    lenguaje = os.getenv("LANGUAGE", "No especificado")

    print(f"Hola, {nombre}, desde GitHub. Tu lenguaje favorito es {lenguaje}.")


if __name__ == "__main__":
    main()