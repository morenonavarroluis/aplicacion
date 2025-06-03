import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from modelo.modelo import obtener_datos_usuarios  # Asegúrate de que este módulo esté correctamente configurado

class MenuApp(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        
        self.datos_originales = obtener_datos_usuarios()
        self.columnas_combobox = sorted(list(set([row[3] for row in self.datos_originales])))  # Eliminar duplicados y ordenar

        self.navbar()  # Llamar al método para crear la barra de navegación
        self._crear_widgets()
        self._configurar_tabla()
        self._cargar_datos_en_tabla(self.datos_originales)

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?"):
            self.master.destroy()  # Cambiado a master.destroy() para cerrar la ventana principal
            

    def navbar(self):

        # Cargar imágenes (ajusta las rutas a tus imágenes)
        img_left = Image.open("./img/images.png").resize((50, 50))
        img_right = Image.open("./img/salidas.png").resize((50, 50))
        self.photo_left = ImageTk.PhotoImage(img_left)  # Guardar referencia
        self.photo_right = ImageTk.PhotoImage(img_right)  # Guardar referencia

        # Navbar frame
        navbar = ttk.Frame(self, bootstyle=PRIMARY)  # Cambia el estilo a PRIMARY para color azul
        navbar.pack(side="top", fill="x")
         

         # Imagen izquierda
        label_left = tk.Label(navbar, image=self.photo_left, bg="#4582EC")
        label_left.pack(side=tk.LEFT, padx=10, pady=5)
        #color de fondo del label
        label_left.config(background="#4582EC")  # Cambia el color de fondo del label

        # Imagen derecha
        label_right = tk.Label(navbar, image=self.photo_right, bg="#4582EC")
        label_right.pack(side=tk.RIGHT, padx=10, pady=5)
        #color de fondo del label
        label_right.config(background="#4582EC")  # Cambia el color de fondo del label
        label_right.bind("<Button-1>", lambda e: self.salir())  # Asignar evento de clic para salir
       
        # label de href 
        label_href = tk.Label(navbar, text="Menu", bg="#4582EC", fg="white", font=("Arial", 12))
        label_href.pack(side=tk.LEFT, padx=10, pady=5)
        label_href.config(background="#4582EC")  # Cambia el color de fondo del label
        label_href.bind("<Button-1>", lambda e: self.controller.show_frame("MenuApp"))  # Asignar evento de clic para volver al menú principal

         # label de href 
        label_href = tk.Label(navbar, text="pagos", bg="#4582EC", fg="white", font=("Arial", 12))
        label_href.pack(side=tk.LEFT, padx=10, pady=5)
        label_href.config(background="#4582EC")  # Cambia el color de fondo del label
        label_href.bind("<Button-1>", lambda e: self.controller.show_frame("Gestion"))  # Asignar evento de clic para ir a la gestión de pagos
 
 
 
    def _crear_widgets(self):
        #crear boton para un modal
       self.boton_modal = ttk.Button(self, text="Abrir Modal", command=self._abrir_modal)
       self.boton_modal.pack(side="bottom", padx=10 , pady= 75)  # Coloca el botón en la esquina superior izquierda

       

    def _configurar_tabla(self):
        """Configura la estructura de la tabla Treeview."""
        self.tabla = ttk.Treeview(
            self,
            columns=("id", "nombre", "apellido", "dependencias", "opcion"),
            show="headings",
            bootstyle=PRIMARY # Cambia el estilo a INFO para color azul suave
        )
       
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("apellido", text="Apellido")
        self.tabla.heading("dependencias", text="Dependencia")
        self.tabla.heading("opcion", text="Opción")

       

        self.tabla.pack(expand=True, fill="both", padx=10, pady=10)  # Ajusta el tamaño al espacio disponible

    def _filtrar_tabla(self, event=None):
        """Filtra la tabla según la dependencia seleccionada en el Combobox."""
        seleccion = self.dependencia_seleccionada.get()
        if seleccion:
            datos_filtrados = [row for row in self.datos_originales if row[3] == seleccion]
        else:
            datos_filtrados = self.datos_originales
        self._cargar_datos_en_tabla(datos_filtrados)

    def _cargar_datos_en_tabla(self, datos):
        """Limpia la tabla y carga los datos proporcionados."""
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for fila in datos:
            self.tabla.insert("", tk.END, values=fila)

    def _mostrar_seleccion(self):
        """Muestra la dependencia seleccionada en la etiqueta de resultado."""
        seleccion = self.dependencia_seleccionada.get()
        if seleccion:
            self.etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}")
        else:
            self.etiqueta_resultado.config(text="No se ha seleccionado ninguna dependencia.")
    def _abrir_modal(self):
        """Abre un modal con un Combobox para seleccionar una dependencia."""
        modal = ttk.Toplevel(self)
        modal.title("Registro de menu")

        modal.geometry("600x500")

        # Etiqueta para el Combobox
        label = ttk.Label(modal, text="Registro de menu", font=("Arial", 16)) 
        label.pack(pady=10)

        label_usuario = ttk.Label(modal, text="Sopa:")
        label_usuario.pack(pady=(0, 5), anchor='w')
        self.entry_usuario = ttk.Entry(modal, bootstyle=PRIMARY)  # Guardar como self.entry_usuario
        self.entry_usuario.pack(fill=tk.X, pady=(0, 10))

        label_usuario = ttk.Label(modal, text="Proteina:")
        label_usuario.pack(pady=(0, 5), anchor='w')
        self.entry_usuario = ttk.Entry(modal, bootstyle=PRIMARY)  # Guardar como self.entry_usuario
        self.entry_usuario.pack(fill=tk.X, pady=(0, 10))


        label_usuario = ttk.Label(modal, text="Contorno:")
        label_usuario.pack(pady=(0, 5), anchor='w')
        self.entry_usuario = ttk.Entry(modal, bootstyle=PRIMARY)  # Guardar como self.entry_usuario
        self.entry_usuario.pack(fill=tk.X, pady=(0, 10))



        label_usuario = ttk.Label(modal, text="Ensalada:")
        label_usuario.pack(pady=(0, 5), anchor='w')
        self.entry_usuario = ttk.Entry(modal, bootstyle=PRIMARY)  # Guardar como self.entry_usuario
        self.entry_usuario.pack(fill=tk.X, pady=(0, 10))


        label_usuario = ttk.Label(modal, text="Jugo:")
        label_usuario.pack(pady=(0, 5), anchor='w')
        self.entry_usuario = ttk.Entry(modal, bootstyle=PRIMARY)  # Guardar como self.entry_usuario
        self.entry_usuario.pack(fill=tk.X, pady=(0, 10))


        label_usuario = ttk.Label(modal, text="Postre:")
        label_usuario.pack(pady=(0, 5), anchor='w')
        self.entry_usuario = ttk.Entry(modal, bootstyle=PRIMARY)  # Guardar como self.entry_usuario
        self.entry_usuario.pack(fill=tk.X, pady=(0, 10))

        # Botón para cerrar el modal
        boton_cerrar = ttk.Button(modal, text="Cerrar", command=modal.destroy)
        boton_cerrar.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(parent=root, controller=None)  # Cambia 'None' por tu controlador si es necesario
    app.pack(expand=True, fill="both")
    root.mainloop()