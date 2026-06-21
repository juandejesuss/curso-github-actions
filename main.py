import os

def main():
    nombre = os.getenv("USERNAME")
    printf(f"hola, {nombre} desde Github")

if __name__ == "__main__":
    main()