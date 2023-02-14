from methods.directory_chooser import DirectoryChooser
from methods.pdf_converter import PDFConverter, path
from methods.get_text import ImageTextExtractor
from methods.name import FileRenamer
from methods.text import TextSearch
from widgets.progress_bar import MainProgressbar
from utils.alert import alert

class MainProcess():
    def __init__(self, main_frame=None):
        self.chooser = DirectoryChooser()
        self.text = ImageTextExtractor()
        self.progressbar = MainProgressbar()
        self.files = FileRenamer()
        self.directory = None
        self.main_frame = main_frame
        self.paths = []
        self.pdf = PDFConverter()
        self.extracted_texts = []

    def init_proccess(self, show_main_button):
        self.directory = self.chooser.choose_directory()
        if self.directory == "":
            self.progressbar.hide()
            self.main_frame.hide()
            show_main_button()
            return
        length_files = self.chooser.check_pdf_files()
        if length_files is not None and length_files > 0:
            self.main_frame.render()
            self.progressbar.render()
            self.progressbar.updadte_label("Procesando tus archivos...")
            self.chooser.list_directory_files()
            self.paths = self.chooser.get_path_files()
            self.paths = self.pdf.convert_to_image(self.paths, self.progressbar)
            if len(self.paths) > 0:
                self.progressbar.update(0)
                self.progressbar.updadte_label("Extrayendo el texto...")
                self.extracted_texts = self.text.extract_text(self.paths, self.progressbar)
                if len(self.extracted_texts) > 0:
                    self.progressbar.updadte_label("Buscando los del archivo...")
                    self.progressbar.update(0)
                    self.handle_text()
            else:
                alert('Error', 'La carpeta debe contener archivos PDF')
            self.progressbar.hide()
            alert('Exito', 'Todos los archivos se han renombrado')
            self.pdf.removedir(path)
        show_main_button()

    
    def handle_text(self):
        files_with_name = []
        for i, text_file in enumerate(self.extracted_texts):
            text = TextSearch(text_file['text'])
            result = text.search()

            text_file['new_name'] = result

            files_with_name.append(text_file)
            self.get_value_to_progressbar(i)
        self.paths = files_with_name
        self.change_name()

    def get_value_to_progressbar(self, i):
        total_files = len(self.paths)
        progress = progress = (i + 1) / total_files * 100
        self.progressbar.update(progress)

    def change_name(self):
        print("[ =============== ]")
        print("self.paths")
        print(self.paths)
        print("[ =============== ]")
        self.progressbar.updadte_label("Renombrando archivos...")
        self.progressbar.update(0)
        for i, file in enumerate(self.paths):
            self.files.rename_file(file["path"], file["new_name"])
            self.main_frame.add_text(file["new_name"])
            self.get_value_to_progressbar(i)

        x = [
            {
                'path': '/Users/poncegl/Downloads/RV_ Oficios/MX-B476W_20221214_094858_0002.pdf', 
                'current_name': 'MX-B476W_20221214_094858_0002.pdf', 
                'new_name': 'OF 1245 JA 29075', 
                'path_image': '/Users/poncegl/Downloads/proyects/Tests/Python/tkinter/read-files-app/images/MX-B476W_20221214_094858_0002', 
                'text': 'ng\n\nPODER JUDICIAL DE LA FEDERACION ~\nJUZGADO DECIMOQUINTO DE DISTRITO EN EL ESTADO DE VERACRUZ\n\n“2022, Afo de Ricardo Flores Mogén”\n\nJUICIO DE AMPARO\nTRAMITE 1245/2022-1-A\n\nMESA FA\n\n- And SONSTANCIA DE NOTIFICACION QUE SE HACE A LA\nF ‘AUTORIDAD QUE SE INDICA, EN TERMINOS DEL\ng ARTICULO 28, FRACCION I, DE LA LEY DE AMPARO, DEL\n\nPROVEIDO DICTADO EL 08 DE DICIEMBRE DE 2022\n\noFicio:\n\n2907572022 AGENTE DEL MINISTERIO PUBLICO DE LA FEDERACION -\n\nAOSTA (MINISTERIO PUBLICO)\n\n2907672022 JUEZ DECIMO SEGUNDO _DE__PRIMERA _INSTANCIA\nESPECIALIZADO. EN. MATERIA. DE FAMILIA. CIUDAD\n(AUTORIDAD RESPONSABLE)\n\n'
            }, 
            {
                'path': '/Users/poncegl/Downloads/RV_ Oficios/MX-B476W_20221214_094858_0001.pdf', 
                'current_name': 'MX-B476W_20221214_094858_0001.pdf', 
                'new_name': 'OF 1246 ', 
                'path_image': '/Users/poncegl/Downloads/proyects/Tests/Python/tkinter/read-files-app/images/MX-B476W_20221214_094858_0001', 
                'text': 'PODER JUDICIAL DE LA FEDERACION = te\n-U2GADO DECMOQUNTO DE OSSTRTO EN EL ESTADO OE VERACRUZ\n\n"2022, Af de Ricardo Fores Magéa”\n\nSaronic INCIDENTE DE SUSPENISON\n1246/2022/11-B\n\nCONSTANCIA DE NOTIFICACION QUE SE HACE A LA\n(00.50 N° AUTORIDAD QUE SE INDICA, EN TERMINOS DEL\nARTICULO 28, FRACCION |, DE LA LEY DE AMPARO, DEL\nPROVEIDO DICTADO EL 09 DE DICIEMBRE DE 2022\n\nLZ pziaeee 122 02 como. ei suzos00 ve proceso vy\nFROCEDIMEENTO PENAL Y ORAL DEL DEGIMO PRIMER DISTRITo USGA\nOE XALAPA, CON SEDE EN EL CENTRO ESTATAL DE Jusrisn pane\n\nMUJERES EN XALAPA, VERACRUZ (AUTORIDAD RESPONSABLE)\n‘SE ANEXA DEMANDA DE AMPARO\n\n'
            }
        ]

            