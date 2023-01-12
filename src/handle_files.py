import os
import platform
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from handle_image import convert, get_text, get_name_file
from makedir import makedir, removedir
from alert import alert

def rename_files(directory, current_name, name):
    prev_name = get_name_file(current_name)
    sistema = platform.system()
    prev_absolute_path = ""
    new_absolute_path = ""
    prev_name = prev_name.replace(".jpg", ".pdf")
    new_name = name
    if name == "NO-SE-ENCONTRO.pdf":
        new_name = f"{name}-{prev_name}"
        new_name = new_name.replace(".pdf", "")

    if sistema == "Windows":
        prev_absolute_path = f'{directory}\{prev_name}'
        new_absolute_path = f'{directory}\{new_name}.pdf'
    else:
        prev_absolute_path = f'{directory}/{prev_name}'
        new_absolute_path = f'{directory}/{new_name}.pdf'

    try:
        os.rename(prev_absolute_path, new_absolute_path)
    except FileExistsError:
        print("El archivo ya existe.")

    return new_absolute_path

def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()


def show_names_container(frame):
    frame.pack()
    text = tk.Text(frame, height=20)
    text.config(width=30, font=("Courier", 18))
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=10)

    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text['yscrollcommand'] = scrollbar.set
    return text

def show_names(position, text, path):
    file_name = get_name_file(path)
     # Crea un widget de etiqueta, con el nombre del archivo y lo coloca en la ventana
    position = f'{position}.0'
    text.insert(position, f"{file_name}\n")

def update_files(files, directory, progressbar, frame):
    progressbar.pack()
    path_dir = makedir()
    # Si la lectura de los archivos fue exitosa, filtra la lista de archivos para incluir solo los PDF
    pdf_files = [f for f in files if f.endswith('.pdf')]
    totalFiles = len(pdf_files)

    if totalFiles == 0:
        progressbar.pack_forget()
        alert('Error', 'La carpeta debe contener archivos PDF')
        return None
    text = show_names_container(frame)
    counter = 0
    file_paths = []
    for pdf_file in pdf_files:
        counter += 1  # Suma 1 al contador en cada iteración
        file_path = os.path.join(directory, pdf_file)
        file_paths.append(file_path)
        progress = (100 / totalFiles) * counter
        path_image  = convert(file_path, path_dir)
        if not path_image:
            alert('Error', 'No stá instalado poppler, no se puede continuar')
            progressbar.pack_forget()
            return
        else:
            new_name = get_text(path_image)
            if not new_name:
                alert('Error', 'No stá instalado Tesserac, no se puede continuar')
                progressbar.pack_forget()
                return
            new_absolute_path = rename_files(directory, path_image, new_name)
            show_names(int(counter), text, new_absolute_path)
            progressbar["value"] = progress  # Actualiza el valor de la barra de progreso
            progressbar.update()  #  Actualiza visualmente la barra de progreso

    progressbar.pack_forget()

    return path_dir

def select_folder(progressbar, frame):
    if frame is not None:
        clear_frame(frame)
    # Muestra un cuadro de diálogo de selección de carpeta al usuario
    directory = filedialog.askdirectory()

    # Si el usuario canceló el cuadro de diálogo, devuelve None
    if directory == '':
        return None

    # Lee los archivos en la carpeta seleccionada
    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        # Si la carpeta no existe, muestra un mensaje de error y devuelve None
        alert('Error' 'La carpeta seleccionada no existe')
        return None
    except NotADirectoryError:
        # Si el archivo seleccionado no es una carpeta, muestra un mensaje de error y devuelve None
        alert('Error', 'El archivo seleccionado no es una carpeta')
        return None
    else:
        images_dir = update_files(files, directory, progressbar, frame)
        if images_dir:
            removedir(images_dir)
            
