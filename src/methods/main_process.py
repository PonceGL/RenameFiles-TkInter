from methods.directory_chooser import DirectoryChooser
from methods.pdf_converter import PDFConverter
from methods.get_text import ImageTextExtractor

class MainProcess():
    def __init__(self, main_frame=None):
        self.chooser = DirectoryChooser()
        self.text = ImageTextExtractor()
        self.directory = None
        self.main_frame = main_frame
        self.paths = []
        self.pdf = PDFConverter()

    def init_proccess(self):
        selected_directory = self.chooser.choose_directory()
        self.directory = selected_directory
        length_files = self.chooser.check_pdf_files()
        if length_files is not None and length_files > 0:
            self.main_frame.render()
            self.chooser.list_directory_files()
            self.paths = self.chooser.get_path_files()
            self.paths = self.pdf.convert_to_image(self.paths)
            if len(self.paths) > 0:
                self.text.extract_text(self.paths)


            