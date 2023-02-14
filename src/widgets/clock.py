import tkinter as tk
from tkinter import ttk
import time

class Clock():
    def __init__(self, root=None):
        self.root = root

        self.label = ttk.Label(self.root, width=400, font=("Helvetica", 40, "bold"))
        self.update()
        self.label.grid(row=0, column=0, columnspan=1, padx=20, sticky="ew")
        

    def update(self):
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%d/%m/%Y")
        self.label.config(text=current_time+"\n"+current_date)
        self.label.after(1000, self.update)
