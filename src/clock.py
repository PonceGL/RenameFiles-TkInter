import time
import customtkinter


def create_widgets(root):
    label = customtkinter.CTkLabel(
        master=root, text='Hola!', font=("Helvetica", 40, "bold"))
    label.grid(row=0, column=0, columnspan=2,
               padx=20, sticky="ew")
    return label


def update_clock(label):
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%d/%m/%Y")
    label.configure(text=current_time+"\n"+current_date)
    label.after(1000, update_clock, label)


def clock(root):
    label = create_widgets(root)
    update_clock(label)
