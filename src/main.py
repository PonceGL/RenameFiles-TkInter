import os
import platform
import tkinter as tk
import customtkinter
import threading
from tkinter import *
from handle_files import select_folder
from menubar import menu
from clock import clock


def run():
    # Modes: system (default), light, dark
    customtkinter.set_appearance_mode("System")
    # Themes: blue (default), dark-blue, green
    customtkinter.set_default_color_theme("blue")

    sistema = platform.system()
    # Crea la ventana principal de tkinter
    root = Tk()  # create CTk window like you do with the Tk window
    # Establece el título de la ventana
    root.title('Renombrar archivos')
    # Obtine la ruta del icono dependiendo del sistema
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
    root.iconphoto(False, icon)

    # Establece el ancho y alto mínimo y máximo de la ventana
    root.minsize(width=375, height=600)
    root.resizable(False, False)

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=6)
    root.grid_columnconfigure((0, 1), weight=1)

    # label = customtkinter.CTkLabel(
    #     master=root, text='Hola, tkinter!', font=("Helvetica", 18))
    # label.grid(row=0, column=0, columnspan=2,
    #            padx=20, sticky="ew")

    frame = tk.Frame(root, width=300)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=10)
    frame.grid_columnconfigure(1, weight=1)
    # frame.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    scrollbar = customtkinter.CTkScrollbar(frame, orientation='vertical')
    box = tk.Listbox(frame, width=40, yscrollcommand=scrollbar.set)
    box.grid(row=0, column=0, sticky="nsew")
    scrollbar.bind(command=box.yview)
    # scrollbar.grid(row=0, column=1, sticky="nse")

    progressbar = customtkinter.CTkProgressBar(
        master=root, orientation="horizontal", width=300, mode="determinate")

    button = customtkinter.CTkButton(master=root, text='Selecciona la carpeta \n donde están tus archivos', border_width=0, corner_radius=10, font=(
        "Helvetica", 18), command=lambda: select_folder(button, progressbar, frame, box, scrollbar))
    button.grid(row=1, column=0, columnspan=2,
                padx=20, sticky="ew")

    menu(root, progressbar)
    clock(root)
    # Inicia el bucle de eventos de tkinter
    root.mainloop()


if __name__ == "__main__":
    run()
