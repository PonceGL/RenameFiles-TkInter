import os

class FileRenamer:
    def __init__(self):
        pass

    def rename_file(self, file_path, new_name):
        old_path = file_path
        new_path = os.path.join(os.path.dirname(file_path), new_name + ".pdf")

        try:
            os.rename(old_path, new_path)
            print("El archivo ha sido renombrado exitosamente.")
        except Exception as e:
            print("Ha ocurrido un error al intentar renombrar el archivo:", e)
