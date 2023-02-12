import sys
import os
import platform
import pytesseract

from methods.directory_chooser import DirectoryChooser

class ImageTextExtractor:
    def __init__(self):
        self.chooser = DirectoryChooser()

    def extract_text(self, path_files):
        extracted_texts = []
        sistema = platform.system()
        if sistema == "Windows":
            self.execute_tesseract()
        try:
            for path_file in path_files:
                files = self.chooser.list_directory_files(path_file['path_image'], ".png")
                for file in files:
                    image_path = path_file['path_image'] + "/" + file
                    text = pytesseract.image_to_string(image_path)
                    extracted_texts.append(text)
            print("Texto extraído exitosamente.")
        except:
            error_message = sys.exc_info()[0]
            print("Error al extraer texto de las imágenes: {}".format(error_message))
        return extracted_texts
    
    def execute_tesseract(self):
        try:
            if getattr(sys, 'frozen', False):
                _path = os.path.join(sys._MEIPASS, r'Tesseract-OCR\tesseract')
                print(_path)
                pytesseract.pytesseract.tesseract_cmd = _path
            else:
                pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        except:
            error_message = sys.exc_info()[0]
        print("Error al especificar la ruta de tesseract: {}".format(error_message))
        