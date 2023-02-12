import tkinter as tk
from handle_files import select_folder
from alert import alert

def menu(root, progressbar):
    menubar = tk.Menu(root)
    root.config(menu = menubar)
    file = tk.Menu(menubar)
    help_ = tk.Menu(menubar)

    menubar.add_cascade(menu = file, label = "File")
    file.add_command(label = 'Seleccionar archivos', command=lambda: select_folder(progressbar, root))
    menubar.add_cascade(menu = help_, label = "Ayuda")
    help_.add_command(label = 'About', command=lambda: alert('About', 'Este es un proyecto de demostración Tkinter por PonceGL'))