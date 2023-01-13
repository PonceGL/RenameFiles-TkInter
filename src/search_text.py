import re
import os

def search_title(text):
    RegExTitle = re.compile(r'([0-9]{1,4})/([0-9]{4})')
    amparo_lawsuit = re.compile(r'(J\s?U\s?I?\|?\s?C\s?I?\|?\s?O\s?\s?D\s?E\s?\s?A\s?M\s?P\s?A\s?R\s?O)')
    suspension_incident = re.compile(r'(I?\|?\s?N\s?C\s?I?\|?\s?D\s?E\s?N\s?T\s?E\s?\s?D\s?E\s?\s?S\s?U\s?S\s?P\s?E\s?N\s?I?\|?\s?S\s?Ó\s?N)')
    

    find_amparo_lawsuit = amparo_lawsuit.search(text)
    find_suspension_incident = suspension_incident.search(text)

    match = RegExTitle.search(text)
    document_number = ""
    
    if match is not None: 
        document_number = match.group().replace('/', '-') 
    else:
        document_number = "NO SE ENCONTRO"

    if find_amparo_lawsuit:
        return f"JA {document_number}"
    if find_suspension_incident:
        return f"IS {document_number}"

    return "NO SE ENCONTRO"

def search_office_number(text):
    RegExOfficeNumber = re.compile(r'(/\s?[0-9]{1,5})/([0-9]{4})')

    match = RegExOfficeNumber.search(text)

    if match:
        document_number = match.group(0).replace('/','').replace(' ','').split("/")[0]
        return f"OF {document_number}"
    else:
        return "NO SE ENCONTRO"

def rename_file(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        print("rename")
    except Exception as error:
        raise Exception("Error al renombrar archivo: " + str(error))
        
def search_file(route):
    try:
        with open(route, 'r') as f:
            return True
    except Exception as error:
        raise Exception("Error al buscar archivo: " + str(error))


def get_new_name(text):
    title = search_title(text)
    officeNumber = search_office_number(text)
    new_name = f'{title} {officeNumber}'
    return new_name.replace("NO SE ENCONTRO NO SE ENCONTRO", "NO SE ENCONTRO")
