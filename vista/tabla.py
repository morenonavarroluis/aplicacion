import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from modelo.modelo import obtener_datos_usuarios  # Asegúrate de que este módulo esté correctamente configurado

class Gestion(ttk.Frame):
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
       
        # Etiqueta de título
        titulo = ttk.Label(navbar, text="Gestión de Pagos", font=("Arial", 16))
        titulo.pack(anchor=tk.CENTER , padx=10, pady=20)
        # Configurar el fondo del titulo
        titulo.config(background="#4582EC",foreground="white")  # Cambia el color de fondo del título
        
 
 
 
    def _crear_widgets(self):
        """Crea y empaqueta todos los widgets de la interfaz."""
        

        
         # Variable para el Combobox
        self.dependencia_seleccionada = tk.StringVar()
        
        # Combobox
        self.dependencia_seleccionada.set("Seleccionar...")  # Establece el texto inicial del Combobox
        self.combobox_dependencia = ttk.Combobox(
            self,
            textvariable=self.dependencia_seleccionada,
            values=self.columnas_combobox,
            state="readonly",
            bootstyle=PRIMARY
        )
        # Use place with absolute positioning (x, y) and no pack() call
        self.combobox_dependencia.place(x=60, y=75, anchor="nw")
        self.combobox_dependencia.bind("<<ComboboxSelected>>", self._filtrar_tabla)

        # Botón para mostrar selección
        boton_imprimir = ttk.Button(
            self,
            text="Imprimir Selección",
            bootstyle=PRIMARY,
            command=self._mostrar_seleccion
        )
        boton_imprimir.pack(side="bottom", padx=10, pady=10)

        # Etiqueta de resultado
        self.etiqueta_resultado = tk.Label(self, text="")
        self.etiqueta_resultado.pack(pady=10)

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

        # Configurar ancho de columnas (opcional, para mejor visualización)
        self.tabla.column("id", width=50, anchor="center")
        self.tabla.column("nombre", width=120, anchor="center")
        self.tabla.column("apellido", width=120, anchor="center")
        self.tabla.column("dependencias", width=150, anchor="center")
        self.tabla.column("opcion", width=100, anchor="center")

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


