import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from search_text import get_new_name

def get_name_file(path):
    path_split = path.split("/")
    file_name = path_split[-1].replace(".pdf", "")
    return file_name

def get_text(path):
    image = Image.open(path)
    text = pytesseract.image_to_string(image)
    text = text.replace('-\n','')
    new_name = get_new_name(text)
    return new_name
    

def convert(path, dir):
    file_name = get_name_file(path)
    pages = convert_from_path(path)
    path_image = os.path.join(dir, file_name +'.jpg')
    print(path_image)
    pages[0].save(path_image)
    return path_image
