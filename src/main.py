import tkinter as tk
import os
import platform
# widgets
from widgets.clock import Clock
from widgets.main_button import MainButton
from widgets.name_files import MainFrame

class App:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(width, height))
        self.root.title("Renombrar archivos")
        # Obtine la ruta del icono dependiendo del sistema
        sistema = platform.system()
        icon = ""
        if sistema == "Windows":
            # icon = r'assets\transfer-color\icons8-transfer-48.png'
            icon = r'D:\Usuarios\vmullor\Documents\projects\RenameFiles-TkInter\assets\transfer-color\icons8-transfer-48.png'
        else:
            icon = r"assets/transfer-color/icons8-transfer-48.png"

        file_path = os.path.dirname(os.path.abspath(__file__))
        BASE_DIR = os.path.dirname(file_path)
        path = os.path.join(BASE_DIR, icon)

        # Añade imagen
        icon = tk.PhotoImage(file=path)
        # Icono de la ventana del programa
        self.root.iconphoto(False, icon)
        self.root.resizable(False, False)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=8)
        self.root.grid_columnconfigure(0, weight=1)

        self.frame = MainFrame(self.root)
        # self.frame.render()

        # Main Clock
        self.clock = Clock(self.root)

        # Init Button
        self.main_button = MainButton(self.root, self.frame)
        self.main_button.render()


    def run(self):
        self.root.mainloop()

app = App(400, 600)
app.run()