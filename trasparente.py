import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

def enviar():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    print(f"Nombre: {nombre}, Correo: {correo}")

# Crear la ventana principal
root = tb.Window(themename="cosmo")

# Título de la ventana
root.title("Formulario Bonito")

# Crear un marco para el formulario
frame = ttk.Frame(root, padding="20")
frame.pack(padx=10, pady=10)

# Etiqueta y campo para el nombre
label_nombre = ttk.Label(frame, text="Nombre:")
label_nombre.grid(row=0, column=0, sticky="w", pady=5)
entry_nombre = ttk.Entry(frame)
entry_nombre.grid(row=0, column=1, pady=5)

# Etiqueta y campo para el correo electrónico
label_correo = ttk.Label(frame, text="Correo Electrónico:")
label_correo.grid(row=1, column=0, sticky="w", pady=5)
entry_correo = ttk.Entry(frame)
entry_correo.grid(row=1, column=1, pady=5)

# Botón de envío
boton_enviar = ttk.Button(frame, text="Enviar", command=enviar)
boton_enviar.grid(row=2, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
