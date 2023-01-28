import os
import platform
import tkinter as tk
from tkinter import ttk, END
from tkinter import filedialog
from handle_image import convert, get_text, get_name_file
from makedir import makedir, removedir
from alert import alert


def rename_files(directory, current_path, name):
    prev_name = get_name_file(current_path)
    sistema = platform.system()
    prev_name = prev_name.replace(".jpg", "")
    new_name = name
    if name == "NO SE ENCONTRO":
        new_name = f"❌ {prev_name}"

    prev_absolute_path = f'{directory}/{prev_name}.pdf'
    new_absolute_path = f'{directory}/{new_name}.pdf'

    if sistema == "Windows":
        prev_absolute_path = f'{directory}\{prev_name}.pdf'
        new_absolute_path = f'{directory}\{new_name}.pdf'

    try:
        os.rename(prev_absolute_path, new_absolute_path)
    except FileExistsError:
        print("El archivo ya existe.")

    return new_absolute_path


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


def show_names(box, path):
    file_name = get_name_file(path)
    # Inserta el nombre de el archivo en el contenedor
    box.insert(END, file_name)


def remove_progresbar(progressbar, frame):
    progressbar.grid_forget()
    frame.grid_forget()


def update_files(files, directory, progressbar, frame, box, scrollbar):
    path_dir = makedir()
    # Si la lectura de los archivos fue exitosa, filtra la lista de archivos para incluir solo los PDF
    pdf_files = [f for f in files if f.endswith('.pdf')]
    totalFiles = len(pdf_files)

    if totalFiles == 0:
        remove_progresbar(progressbar, frame)
        removedir(path_dir)
        alert('Error', 'La carpeta debe contener archivos PDF')
        return None
    numeros_lista = list(range(totalFiles))
    progressbar.grid(row=1, column=0, columnspan=2, padx=20, sticky="ew")
    frame.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
    for i, pdf_file in enumerate(numeros_lista):
        file_path = os.path.join(directory, pdf_files[i])
        progress = i / totalFiles
        path_image = convert(file_path, path_dir)
        if i > 24:
            scrollbar.grid(row=0, column=1, sticky="nse")
        if not path_image:
            alert('Error', 'No stá instalado poppler, no se puede continuar')
            remove_progresbar(progressbar, frame)
            return
        else:
            new_name = get_text(path_image)
            if not new_name:
                alert('Error', 'No stá instalado Tesserac, no se puede continuar')
                remove_progresbar(progressbar, frame)
                return
            new_absolute_path = rename_files(directory, path_image, new_name)
            show_names(box, new_absolute_path)
            # Actualiza el valor de la barra de progreso
            progressbar.set(progress)
            progressbar.update()  # Actualiza visualmente la barra de progreso

    progressbar.grid_forget()
    alert('Exito', 'Todos los archivos se han renombrado')
    return path_dir


def get_files(directory):
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

    return files


def select_folder(button, progressbar, frame, box, scrollbar):
    button.grid_forget()
    if box is not None:
        clear_frame(box)
    # Muestra un cuadro de diálogo de selección de carpeta al usuario
    directory = filedialog.askdirectory()

    files = get_files(directory)
    if not files:
        button.grid(row=1, column=0, columnspan=2,
                    padx=20, sticky="ew")
        return None
    else:
        images_dir = update_files(
            files, directory, progressbar, frame, box, scrollbar)
        if images_dir:
            removedir(images_dir)
    button.grid(row=1, column=0, columnspan=2,
                padx=20, sticky="ew")
