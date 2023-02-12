import os
import shutil

nameDir = "images"
project_root = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(project_root, nameDir)

def removedir(images_dir = path):
    shutil.rmtree(images_dir)

def makedir():
     # Elimina el directorio si ya existe
    if os.path.exists(path):
        removedir()
        print("La carpeta ha sido eliminada por que ya existia.")
    try:
    # Crea un nuevo directorio
        os.mkdir(path)
    except OSError:
        print("La carpeta no pudo ser creada.")
    else:
        print("La carpeta ha sido creada exitosamente.")
        return path
