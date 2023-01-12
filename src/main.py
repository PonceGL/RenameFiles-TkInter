import os
import platform
import tkinter as tk
from tkinter import ttk
from handle_files import select_folder
from menubar import menu


def run():
    sistema = platform.system()
    # Crea la ventana principal de tkinter
    root = tk.Tk()
    # Establece el título de la ventana
    root.title('Renombrar archivos')
    # Obtine la ruta del icono dependiendo del sistema
    icon = ""
    if sistema == "Windows":
        icon = r'assets\transfer-color\icons8-transfer-48.png'
        # icon = r'D:\Usuarios\vmullor\Documents\projects\RenameFiles-TkInter\assets\transfer-color\icons8-transfer-48.png'
    else:
        icon = r"assets/transfer-color/icons8-transfer-48.png"

    file_path = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(file_path)
    path = os.path.join(BASE_DIR, icon)

    # Añade imagen
    icon = tk.PhotoImage(file=path)
    # Icono de la ventana del programa
    root.iconphoto(False, icon)  

    # Establece el ancho y alto mínimo y máximo de la ventana
    root.minsize(width=375, height=600)
    root.resizable(False, False)
    # root.maxsize(width=1000, height=600)

    # Crea un widget de etiqueta y lo coloca en la ventana
    label = tk.Label(root, text='Hola, tkinter!')
    label.pack()
    # Crea una barra de progreso y la coloca en la ventana
    progressbar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    # progressbar.pack()

    frame = tk.Frame(root, width=300, height=200) 
    # frame.pack()

    # Crea un widget de botón y lo coloca en la ventana
    button = tk.Button(root, text='Selecciona la carpeta \n donde están tus archivos', font=("Verdana", 18), command=lambda: select_folder(progressbar, frame))
    button.pack()


    

    menu(root, progressbar)
    # Inicia el bucle de eventos de tkinter
    root.mainloop()


if __name__ == "__main__":
    run()