import tkinter as tk
from tkinter import ttk
# widgets
from widgets.clock import Clock
from widgets.main_button import MainButton
from widgets.name_files import MainFrame

class App:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(width, height))
        self.root.title("Renombrar archivos")
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