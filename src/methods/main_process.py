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

            if result != "":
                text_file['new_name'] = result
            else:
                text_file['new_name'] = text_file['current_name'].replace(".pdf", "")


            files_with_name.append(text_file)
            self.get_value_to_progressbar(i)
        self.paths = files_with_name
        self.change_name()

    def get_value_to_progressbar(self, i):
        total_files = len(self.paths)
        progress = progress = (i + 1) / total_files * 100
        self.progressbar.update(progress)

    def change_name(self):
        self.progressbar.updadte_label("Renombrando archivos...")
        self.progressbar.update(0)
        for i, file in enumerate(self.paths):
            self.files.rename_file(file["path"], file["new_name"])
            self.main_frame.add_text(file["new_name"])
            self.get_value_to_progressbar(i)

            