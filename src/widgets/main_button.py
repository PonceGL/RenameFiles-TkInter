import tkinter as tk
import platform
from methods.main_process import MainProcess

class MainButton():
    def __init__(self, root=None, main_frame=None):
        self.root = root
        self.main_process = MainProcess()
        # self.main_frame = main_frame
        
        self.button = tk.Button(self.root, text="Selecciona la carpeta donde están tus archivos", font=('Helvetica', 16), height=5, width=10, bg='#FC7300', fg='#00425A', command=lambda: self.action())
        self.button = tk.Button(self.root, text="Selecciona la carpeta donde están tus archivos", height=2, width=10, font=("Helvetica", 16), command=lambda: self.action())
        if platform.system() == "Windows":
            self.button.config(background="#0A66C2", foreground="#ffffff",
                    borderwidth=0, relief="flat",
                    activebackground="#0A66C2", activeforeground="#ffffff", bd=0, highlightthickness=0,)

    def action(self):
        # main_process = MainProcess()
        # self.main_frame.render()
        self.main_process.init_proccess()
        
    def render(self):
        self.button.grid(row=1, column=0, columnspan=1, padx=20, sticky="ew")



# import tkinter as tk
# from tkinter import ttk
# from utils.alert import alert

# class MainButton():
#     def __init__(self, root=None, main_frame=None):
#         self.root = root
#         self.main_frame = main_frame
        
#         self.style = ttk.Style()
#         self.style.configure('my.TFrame', padding=(10, 20), font=('Helvetica', 16), background="white")
#         self.button = ttk.Frame(self.root, style='my.TFrame')
#         self.button.bind("<Button-1>", self.action)
#         self.label = tk.Label(self.button, text="Selecciona la carpeta donde están tus archivos", font=('Helvetica', 16), anchor="center", justify="center")
#         self.label.pack(expand=True, fill="both")



#     def action(self, event):
#         self.style.configure('my.TButton', background="blue")
#         self.button.update()
#         self.main_frame.render()
#         self.main_frame.add_text("Button was clicked!")
        
#     def render(self):
#         self.button.grid(row=1, column=0, columnspan=1, padx=20, sticky="nsew")
#         self.label.grid(sticky="nsew")




# import tkinter as tk
# from tkinter import ttk
# from utils.alert import alert

# class MainButton():
#     def __init__(self, root=None, main_frame=None):
#         self.root = root
#         self.main_frame = main_frame
        
#         self.style = ttk.Style()
#         self.style.configure('my.TFrame', padding=(10, 20), font=('Helvetica', 16))
#         self.button = ttk.Frame(self.root, style='my.TFrame')
#         self.button.bind("<Button-1>", self.action)
#         self.label = tk.Label(self.button, text="Selecciona la carpeta donde están tus archivos", font=('Helvetica', 16))
#         self.label.pack(expand=True, fill="both")



#     def action(self, event):
#         self.main_frame.render()
#         self.main_frame.add_text("Button was clicked!")
        
#     def render(self):
#         self.button.grid(row=1, column=0, columnspan=1, padx=20, sticky="nsew")
#         self.label.grid(sticky="nsew")
