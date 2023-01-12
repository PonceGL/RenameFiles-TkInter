import os
import platform
import sys
from PIL import Image
import pytesseract
from pytesseract import TesseractError, TesseractNotFoundError
from pdf2image import convert_from_path
from search_text import get_new_name

def get_name_file(path):
    path_split = []
    sistema = platform.system()
    if sistema == "Windows":
        path_split = path.split("\\")
    else:
        path_split = path.split("/")
    file_name = path_split.pop().replace(".pdf", "")
    return file_name

def get_image(path):
    image = Image.open(open(path, "rb"))
    return image


def get_text(path):
    image = get_image(path)
    try:
        # print("getattr(sys, 'frozen', False)")
        # print(getattr(sys, 'frozen', False))
        # print("_path = os.path.join(sys._MEIPASS, 'tesseract.exe')")
        # print(os.path.join(sys._MEIPASS, r'Tesseract-OCR\tesseract'))
        if getattr(sys, 'frozen', False):
            _path = os.path.join(sys._MEIPASS, r'Tesseract-OCR\tesseract')
            print(_path)
            pytesseract.pytesseract.tesseract_cmd =_path
        else:
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

        text = pytesseract.image_to_string(image)
        text = text.replace('-\n','')
        new_name = get_new_name(text)
        return new_name
    except TesseractNotFoundError:
        print("TesseractNotFoundError")
        return ""
    except TesseractError:
        print("TesseractError")
        return ""
    

def convert(path, dir):
    try:
        file_name = get_name_file(path)
        pages = None
        sistema = platform.system()
        if sistema == "Windows":
            pages = convert_from_path(path, poppler_path = r"D:\Usuarios\vmullor\Desktop\Release-22.12.0-0\poppler-22.12.0\Library\bin")
        else:
            pages = convert_from_path(path)
        path_image = os.path.join(dir, file_name +'.jpg')
        pages[0].save(path_image)
        return path_image
    except:
        return ""
        
