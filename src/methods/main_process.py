from methods.directory_chooser import DirectoryChooser

class MainProcess():
    def __init__(self):
        self.chooser = DirectoryChooser()
        self.directory = None

    def init_proccess(self):
        selected_directory = self.chooser.choose_directory()
        self.directory = selected_directory
        print(self.directory)
        length_files = self.chooser.check_pdf_files()
        if length_files is not None and length_files > 0:
            print(length_files)
            files = self.chooser.list_directory_files()
            print("files =======>")
            print(files)
            