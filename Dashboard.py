import os
import subprocess
import sys
import time
from colorama import init, Fore, Style

init(autoreset=True)

# =======================
# ANIMACIÓN DE BIENVENIDA
# =======================
def animacion_bienvenida():
    texto = Fore.CYAN + "Universidad Estatal Amazónica - Programación Orientada a Objetos"
    for i in range(3):
        sys.stdout.write("\r" + texto + "." * (i + 1))
        sys.stdout.flush()
        time.sleep(0.7)
    print("\n")

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(Fore.YELLOW + f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(Fore.RED + "El archivo no se encontró.")
        return None
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print(Fore.GREEN + "\n==============================")
        print(Fore.GREEN + "   MENÚ PRINCIPAL - DASHBOARD ")
        print(Fore.GREEN + "==============================")
        # Imprime las opciones del menú principal
        for key in unidades:
            print(Fore.BLUE + f"{key} - {unidades[key]}")
        print(Fore.MAGENTA + "0 - Salir")

        eleccion_unidad = input(Fore.CYAN + "Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print(Fore.MAGENTA + "Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print(Fore.RED + "Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print(Fore.GREEN + "\n------------------------------")
        print(Fore.GREEN + "   SUBMENÚ - SELECCIONA UNA CARPETA")
        print(Fore.GREEN + "------------------------------")
        # Imprime las subcarpetas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(Fore.BLUE + f"{i} - {carpeta}")
        print(Fore.MAGENTA + "0 - Regresar al menú principal")

        eleccion_carpeta = input(Fore.CYAN + "Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print(Fore.RED + "Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print(Fore.RED + "Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(Fore.GREEN + "\n******************************")
        print(Fore.GREEN + "   SCRIPTS DISPONIBLES")
        print(Fore.GREEN + "******************************")
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):
            print(Fore.BLUE + f"{i} - {script}")
        print(Fore.MAGENTA + "0 - Regresar al submenú anterior")
        print(Fore.MAGENTA + "9 - Regresar al menú principal")

        eleccion_script = input(Fore.CYAN + "Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input(Fore.CYAN + "¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print(Fore.YELLOW + "No se ejecutó el script.")
                        else:
                            print(Fore.RED + "Opción no válida. Regresando al menú de scripts.")
                        input(Fore.CYAN + "\nPresiona Enter para volver al menú de scripts.")
                else:
                    print(Fore.RED + "Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print(Fore.RED + "Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    animacion_bienvenida()
    mostrar_menu()
