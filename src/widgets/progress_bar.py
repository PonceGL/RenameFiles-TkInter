from tkinter import ttk

class MainProgressbar():
    def __init__(self, root=None):
        self.root = root

        self.frame = ttk.Frame(self.root)
        self.label = ttk.Label(self.frame, text="Procesando tus archivos...", width=400, font=("Helvetica", 16, "bold"))

        self.progressbar = ttk.Progressbar(self.frame, orient="horizontal", mode="determinate")
        self.progressbar["maximum"] = 100

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        
        self.label.grid(row=0, column=0, columnspan=1, sticky="ew")
        self.progressbar.grid(row=1, column=0, columnspan=1, sticky="ew")
            
    def render(self):
        self.frame.grid(row=1, column=0, columnspan=1, padx=20, sticky="ew")
    
    def hide(self):
        self.frame.grid_forget()
    
    def update(self, value):
        self.progressbar["value"] = value
        self.progressbar.update()
    
    def updadte_label(self, text):
        print("updadte_label")
        print(text)
        self.label.config(text=text)