import tkinter as tk
import platform
from methods.main_process import MainProcess

class MainButton():
    def __init__(self, root=None, main_frame=None):
        self.root = root
        self.main_frame = main_frame
        self.main_process = MainProcess(self.main_frame)
        
        self.button = tk.Button(self.root, text="Selecciona la carpeta donde están tus archivos", font=('Helvetica', 16), height=5, width=10, bg='#FC7300', fg='#00425A', command=lambda: self.action())
        self.button = tk.Button(self.root, text="Selecciona la carpeta donde están tus archivos", height=2, width=10, font=("Helvetica", 16), command=lambda: self.action())
        if platform.system() == "Windows":
            self.button.config(background="#0A66C2", foreground="#ffffff",
                    borderwidth=0, relief="flat",
                    activebackground="#0A66C2", activeforeground="#ffffff", bd=0, highlightthickness=0,)

    def action(self):
        self.hide()
        if self.main_frame is not None:
            self.main_frame.clear()

        self.main_process.init_proccess(self.render)
        
    def render(self):
        self.button.grid(row=1, column=0, columnspan=1, padx=20, sticky="ew")
    
    def hide(self):
        self.button.grid_forget()

