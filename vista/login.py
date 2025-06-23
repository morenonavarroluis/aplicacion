import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import  Style  # Asegúrate de importar Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
#from controlador.funciones import verificar_credenciales
from controlador.funciones import verificar_credenciales
from vista.tabla import Gestion  # Asegúrate de que esta importación sea correcta

class LoginApp(ttk.Frame):  # Cambiado el nombre de la clase a PascalCase (convención)
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
    
        
        
                # Crear un marco con borde
        frame_borde = ttk.Frame(self, borderwidth=4, relief="groove", padding=20)
        frame_borde.pack(padx=20, pady=140)
        # Título
        label_titulo = ttk.Label(frame_borde, text="Acceso al Sistema", font=("Helvetica", 16, "bold"), bootstyle=PRIMARY)
        label_titulo.pack(pady=(0, 20), anchor='center')  # Centrar el título
        # Campo de Usuario
        label_usuario = ttk.Label(frame_borde, text="Usuario:")
        label_usuario.pack(pady=(0, 5), anchor='center')  # Centrar la etiqueta de usuario
        self.entry_usuario = ttk.Entry(frame_borde, bootstyle=PRIMARY)  # Guardar como self.entry_usuario
        self.entry_usuario.pack(pady=(0, 10), padx=20)  # Centrar el campo de entrada
        # Campo de Contraseña
        label_contrasena = ttk.Label(frame_borde, text="Contraseña:")
        label_contrasena.pack(pady=(0, 5), anchor='center')  # Centrar la etiqueta de contraseña
        self.entry_contrasena = ttk.Entry(frame_borde, show="*", bootstyle=PRIMARY)  # Guardar como self.entry_contrasena
        self.entry_contrasena.pack(pady=(0, 20), padx=20)  # Centrar el campo de entrada
        # Botón de Inicio de Sesión
        self.boton_login = ttk.Button(frame_borde, text="Iniciar Sesión", command=self.accion_login, bootstyle=PRIMARY)
        self.boton_login.pack()


    def accion_login(self):
        """Maneja el evento de clic del botón de inicio de sesión."""
        username_val = self.entry_usuario.get()  # Acceder a través de self
        password_val = self.entry_contrasena.get()  # Acceder a través de self
      
      

        if not username_val or not password_val:
            messagebox.showwarning("Campos Vacíos", "Por favor, ingresa tu usuario y contraseña.")
            return

        if verificar_credenciales(username_val, password_val):
            print('funcionando')
            # self.ventana.destroy()
            # gestion = Gestion() 
            # gestion.run()  # Si la clase Gestion tiene un método run, llámalo para iniciar la nueva ventana
            self.controller.show_frame('MenuApp')  # Cambia a la pantalla del menú principal
        else:
            messagebox.showerror("Error de Inicio de Sesión", "Usuario o contraseña incorrectos.")
            self.entry_contrasena.delete(0, tk.END)  # Acceder a través de self

    # def run(self):
    #     """Inicia el bucle principal de la aplicación."""
    #     self.ventana.mainloop()

