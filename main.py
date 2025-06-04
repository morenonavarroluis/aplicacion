# /home/desarrollo-02/Escritorio/tkinter_apli/main.py
import tkinter
from vista.login import LoginApp  # Importa la clase de inicio de sesión
from vista.principal import MenuApp  # Importa la clase del menú principal
from vista.tabla import Gestion  # Importa la clase para la tabla de ventas

# Clase base para la construcción de la ventana
class BaseApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Pagos")
        self.geometry("900x600")

        # Configurar grid para que el frame ocupe todo el espacio
        self.grid_rowconfigure(0, weight=1)  # Cambiado a 0 para que el frame principal ocupe la fila 0
        self.grid_columnconfigure(0, weight=1)  # Cambiado a 0 para que el frame principal ocupe la columna 0

        self.current_frame = None
        self._frames = {}  # Diccionario para almacenar las clases de las pantallas

        self._frames[LoginApp.__name__] = LoginApp
        self._frames[MenuApp.__name__] = MenuApp
        self._frames[Gestion.__name__] = Gestion  # Asegúrate de que Gestion esté correctamente importada

        self.show_frame(LoginApp.__name__)

    def show_frame(self, page_name):
        """
        Muestra un frame específico.
        Destruye el frame actual y crea una nueva instancia del solicitado.
        """
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None  # Limpia la referencia al frame destruido

        # Obtiene la clase del frame del diccionario
        frame_class = self._frames.get(page_name)
        if frame_class:
            # Crea una nueva instancia de la clase del frame, pasándole 'self' (la app)
            # para que el frame pueda acceder a métodos de la app (como show_frame)
            new_frame = frame_class(parent=self, controller=self)
            new_frame.grid(row=0, column=0, sticky="nsew")  # Cambiado a (0, 0) para ocupar toda la ventana
            new_frame.tkraise()  # Asegura que esté al frente
            self.current_frame = new_frame
        else:
            print(f"Error: No se encontró la pantalla '{page_name}'")

# Para ejecutar la aplicación
if __name__ == "__main__":
    app = BaseApp()
    app.mainloop()
