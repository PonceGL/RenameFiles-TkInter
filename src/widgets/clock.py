import tkinter as tk
from tkinter import ttk
import time

class Clock(ttk.Label):
    def __init__(self, master=None):
        ttk.Label.__init__(self, master, width=400, font=("Helvetica", 40, "bold"))
        self.update()
        self.grid(row=0, column=0, columnspan=1, padx=20, sticky="ew")

    def update(self):
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%d/%m/%Y")
        self.config(text=current_time+"\n"+current_date)
        self.after(1000, self.update)
