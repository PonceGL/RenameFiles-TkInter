import fitz
import os
import sys
import shutil

dir_name = "images"
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
path = os.path.join(project_root, dir_name)

class PDFConverter:

    def __init__(self):
        self.path_files = []
        self.output_dir = path

    def convert_to_image(self, path_files):
        self.path_files = path_files
        # Crear el directorio de salida si no existe
        dir = self.makedir(self.output_dir)
        path_files_update = []

        try:
            for pdf in self.path_files:
                pdf_path = pdf['path']
                pdf_name = pdf['current_name']
                current_name = pdf_name.replace(".pdf", "")

                # Crear el directorio de salida para cada archivo PDF
                pdf_dir = os.path.join(dir, current_name)
                self.makedir(pdf_dir)

                # Abrir el archivo PDF
                pdf_document = fitz.open(pdf_path)

                # Convertir la primer página del PDF en una imagen
                # page = pdf_document[0]
                # pix = page.get_pixmap()
                # output_path = os.path.join(dir, pdf_name.replace(".pdf", ".png"))
                # pix.save(output_path)
                
                # Convertir cada página del PDF en una imagen
                for page_number in range(pdf_document.page_count):
                    page = pdf_document[page_number]
                    pix = page.get_pixmap()
                    output_path = os.path.join(pdf_dir, "page_{}.png".format(page_number))
                    pix.save(output_path)
                pdf["path_image"] = pdf_dir
                path_files_update.append(pdf)
            print("PDFs convertidos a imágenes exitosamente.")
            return path_files_update
        except:
            error_message = sys.exc_info()[0]
            print("Error al convertir PDFs a imágenes: {}".format(error_message))

    def removedir(self, dir):
        shutil.rmtree(dir)

    def makedir(self, dir):
        # Elimina el directorio si ya existe
        if os.path.exists(dir):
            self.removedir(dir)
            # print("La carpeta ha sido eliminada por que ya existia.")
        try:
        # Crea un nuevo directorio
            os.mkdir(dir)
        except OSError:
            print("La carpeta no pudo ser creada.")
        else:
            # print("La carpeta ha sido creada exitosamente.")
            return dir