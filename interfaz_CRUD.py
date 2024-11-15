import tkinter as tk
from tkinter import messagebox
import logica_CRUD

# Función para crear un nuevo registro a través de la GUI
def create():
    name = entry_name.get()
    age = entry_age.get()
    if logica_CRUD.create(name, age):
        listbox.insert(tk.END, f"{name} - {age} años")
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        messagebox.showinfo("Información", "Registro creado exitosamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

# Función para leer o mostrar un registro a través de la GUI
def read():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        record = logica_CRUD.read(index)
        if record:
            entry_name.delete(0, tk.END)
            entry_name.insert(0, record["name"])
            entry_age.delete(0, tk.END)
            entry_age.insert(0, record["age"])
    else:
        messagebox.showwarning("Advertencia", "Selecciona un registro para ver.")

# Función para actualizar un registro a través de la GUI
def update():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        name = entry_name.get()
        age = entry_age.get()
        if logica_CRUD.update(index, name, age):
            listbox.delete(index)
            listbox.insert(index, f"{name} - {age} años")
            messagebox.showinfo("Información", "Registro actualizado exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
    else:
        messagebox.showwarning("Advertencia", "Selecciona un registro para actualizar.")

# Función para eliminar un registro a través de la GUI
def delete():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        if logica_CRUD.delete(index):
            listbox.delete(index)
            messagebox.showinfo("Información", "Registro eliminado exitosamente.")
    else:
        messagebox.showwarning("Advertencia", "Selecciona un registro para eliminar.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("CRUD con Tkinter")

# Etiquetas y campos de entrada
label_name = tk.Label(root, text="Nombre")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_age = tk.Label(root, text="Edad")
label_age.grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

# Listbox para mostrar los registros
listbox = tk.Listbox(root, width=40)
listbox.grid(row=2, column=0, columnspan=2)

# Botones de operación CRUD
btn_create = tk.Button(root, text="Crear", command=create)
btn_create.grid(row=3, column=0)
btn_read = tk.Button(root, text="Leer", command=read)
btn_read.grid(row=3, column=1)
btn_update = tk.Button(root, text="Actualizar", command=update)
btn_update.grid(row=4, column=0)
btn_delete = tk.Button(root, text="Eliminar", command=delete)
btn_delete.grid(row=4, column=1)

# Iniciar la aplicación
root.mainloop()
