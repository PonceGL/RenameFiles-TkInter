import sys
import os
import platform
import pytesseract
import cv2
import numpy as np
# from PIL import Image

# https://res.cloudinary.com/duibtuerj/image/upload/v1676324925/Projects/read_files/fi646vas4078s8a22ucw.png
# https://res.cloudinary.com/duibtuerj/image/upload/v1676324918/Projects/read_files/xfbgezebf2htty4cmspo.png

from methods.directory_chooser import DirectoryChooser

class ImageTextExtractor:
    def __init__(self):
        self.chooser = DirectoryChooser()
        self.sistema = platform.system()

    def separator(self):
        if self.sistema == "Windows":
            return "\\"
        else:
            return "/"

    def extract_text(self, path_files):
        extracted_texts = []
        if self.sistema == "Windows":
            self.execute_tesseract()
        try:
            for path_file in path_files:
                files = self.chooser.list_directory_files(path_file['path_image'], ".png")
                file_string = ""
                for file in files:
                    image_path = path_file['path_image'] + self.separator() + file
                    img_rgb =self.get_image(image_path)
                    text = pytesseract.image_to_string(img_rgb)
                    file_string = file_string + text
                extracted_texts.append(file_string)
            print("Texto extraído exitosamente.")
        except:
            error_message = sys.exc_info()[0]
            print("Error al extraer texto de las imágenes: {}".format(error_message))
        return extracted_texts
    
    def get_image(self, path):
        img_cv = cv2.imread(path)
        # img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        img_convolved = self.convolucion(cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY))
        text_by_img_clean = pytesseract.image_to_string(img_convolved)
        return img_convolved
    
    def convolucion(self, image):
        kernel = np.ones((1,2), np.float32)/1.7
        img_convolved = cv2.filter2D(image, -1, kernel)
        # cv2.imwrite('img_convolved.png', img_convolved)
        return img_convolved
    
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
        