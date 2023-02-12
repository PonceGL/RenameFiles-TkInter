import os
import sys
from tkinter import filedialog

class DirectoryChooser:
    def __init__(self, root=None, selected_directory=None):
        pass
        self.root = root
        self.selected_directory = selected_directory
        self.files_in_directory = []
        self.path_files = []

    def choose_directory(self):
        try:
            self.selected_directory = filedialog.askdirectory(parent=self.root, title="Selecciona una carpeta")
        except:
            self.selected_directory = None
            error_message = sys.exc_info()[0]
            print("Error: {}".format(error_message))
        return self.selected_directory
    
    def check_pdf_files(self):
        try:
            import os
            if self.selected_directory is None:
                print("No se ha seleccionado ninguna carpeta")
                return

            files = os.listdir(self.selected_directory)
            pdf_files = [file for file in files if file.endswith(".pdf")]
            length = len(pdf_files)

            if length == 0:
                print("No se encontraron archivos PDF en la carpeta seleccionada")
            else:
                print("Se encontraron {} archivos PDF en la carpeta seleccionada".format(length))
            return length
        except:
            error_message = sys.exc_info()[0]
            print("check_pdf_files Error: {}".format(error_message))
    
    def list_directory_files(self, dir = None, ext = ".pdf"):
        try:
            if self.selected_directory or dir:
                directory = self.selected_directory or dir
                self.files_in_directory = [f for f in os.listdir(directory) if f.endswith(ext) and os.path.isfile(os.path.join(directory, f))]
                return self.files_in_directory
            else:
                print("No se ha seleccionado un directorio aún.")
                return None
        except:
            error_message = sys.exc_info()[0]
            print("list_directory_files Error: {}".format(error_message))
            return None
    
    
    def get_path_files(self):
        paths = []
        try:
            for file in self.files_in_directory:
                paths.append({"path": os.path.join(self.selected_directory, file), "current_name": file, "new_name": "", "path_image": ""})
        except:
            error_message = sys.exc_info()[0]
            print("get_path_files Error: {}".format(error_message))
        self.path_files = paths
        return paths