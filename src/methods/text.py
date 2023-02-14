import re

class TextSearch:
    def __init__(self, text):
        self.text = text
        self.trial_number = re.compile(r'([0-9]{1,4})\/([0-9]{4})')
        self.amparo_lawsuit = re.compile(r'(J\s?U\s?(\||I)\s?C\s?(\||I)\s?O\s?\s?\s?D\s?E\s?\s?\s?A\s?M\s?P\s?A\s?R\s?O)', re.IGNORECASE)
        self.suspension_incident = re.compile(r'(((\||I)\s?N\s?C\s?(\||I)\s?\s?\s?D\s?E\s?N\s?T\s?E\s?\s?\s?D\s?E\s?\s?\s?S\s?U\s?S\s?P\s?E\s?N\s?S\s?(\||I)\s?(Ó|O)\s?N))', re.IGNORECASE)
        self.office_number = re.compile(r'([0-9]{1,5})(7|\/)([0-9]{4})')
        # self.office_number = re.compile(r'(((7|\/|I|L|i)\s?[0-9]{1,5})\/([0-9]{4}))')

    def get_trial_number(self):
        try:
            match = self.trial_number.search(self.text.replace(" ", ""))

            if match:
                document_number = re.sub("(\/\s?)", "", match.group(0))
                document_number = document_number[:-4]
                return document_number
            else:
                print("No se encontró el número de juicio.")
                return None
        except Exception as e:
            print("Error: {}".format(str(e)))
            return None

        except:
            print("Error en la búsqueda del numero de documento")
            return None
    
    def get_type_document(self):
        try:
            amparo_lawsuit_match = self.amparo_lawsuit.search(self.text)
            if amparo_lawsuit_match:
                return "JA"

            suspension_incident_match = self.suspension_incident.search(self.text)
            if suspension_incident_match:
                return "IS"

            print("No se encontró el número de juicio.")
            return None

        except Exception as e:
            print("Error: {}".format(str(e)))
            return None

        except:
            print("Error en la búsqueda del numero de documento")
            return None
    
    def get_office_number(self):
        # print("[ =============== ]")
        # print(self.text.replace(" ", ""))
        # print("[ =============== ]")
        try:
            # match = self.office_number.search(self.text.replace(" ", ""))
            matches = list(self.office_number.finditer(self.text.replace(" ", "")))

            if matches:
                office = None
                if len(matches) >= 2:
                    second_match = matches[1].group()
                    office = matches[1].group(0)
                    office = office[:-4].rstrip('7').rstrip('/')
                    # office = re.sub("(7|\/)$", "", matches[1].group(0))
                # else:
                    # office = matches[0].group(0)
                    # office = re.sub("(7|\/)", "", matches[0].group(0))
                return office
            else:
                print("No se encontró el número de juicio.")
                return None
        except Exception as e:
            print("Error: {}".format(str(e)))
            return None

        except:
            print("Error en la búsqueda del numero de documento")
            return None

    def search(self):
        self.convert_array_to_string()
        number = self.get_trial_number()
        document = self.get_type_document()
        office = self.get_office_number()
        final_name = ""
        if number is not None:
            final_name += f"OF {number} "
        if document is not None:
            final_name += f"{document} "
        if office is not None:
            final_name += f"{office}"

        if final_name != "":
            return final_name
        else:
            print("No se pudo formar la cadena final.")
            return ""
    
    def convert_array_to_string(self):
        self.text =  " ".join(self.text)

