import tkinter as tk
import tkinter.ttk as ttk


class MainFrame:
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.listbox = tk.Listbox(self.frame, height=6, font=('Helvetica', 16), selectmode=tk.EXTENDED)
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.listbox.yview)
        self.listbox.configure(width=40, height=10, yscrollcommand=self.scrollbar.set)
        self.listbox.grid(row=0, column=0, columnspan=1, padx=20, pady=20, sticky="nsew")

        self.scrollbar.grid(row=2, column=0, sticky="ns")
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

    def render(self):
        self.frame.grid(row=2, column=0, columnspan=1, sticky="nsew")

    def hide(self):
        self.frame.grid_forget()

    def add_text(self, text):
        self.listbox.insert(tk.END, text)
