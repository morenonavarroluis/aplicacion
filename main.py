# /home/desarrollo-02/Escritorio/tkinter_apli/main.py
import tkinter
#from vista.tabla import Gestion # Importa la clase refactorizada

from vista.login import LoginApp # Importa la clase de inicio de sesión
from vista.tabla import Gestion # Importa la clase para la tabla de ventas


#clase base para la construccion de la ventana
class BaseApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        #self.ventana = tk.Tk()
        self.title("Gestión de Pagos")
        self.geometry("600x400")

        # Configurar grid para que el frame ocupe todo el espacio
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.current_frame = None
        self._frames = {} # Diccionario para almacenar las clases de las pantallas

        self._frames[LoginApp.__name__] = LoginApp
        self._frames[Gestion.__name__] = Gestion
        #self._frames[DashboardScreen.__name__] = DashboardScreen

        self.show_frame(LoginApp.__name__)

    def show_frame(self, page_name):
        """
        Muestra un frame específico.
        Destruye el frame actual y crea una nueva instancia del solicitado.
        """
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None # Limpia la referencia al frame destruido

        # Obtiene la clase del frame del diccionario
        frame_class = self._frames.get(page_name)
        if frame_class:
            # Crea una nueva instancia de la clase del frame, pasándole 'self' (la app)
            # para que el frame pueda acceder a métodos de la app (como show_frame)
            new_frame = frame_class(parent=self, controller=self)
            new_frame.grid(row=1, column=1, sticky="nsew") # Empaca el frame en la ventana
            new_frame.tkraise() # Asegura que esté al frente
            self.current_frame = new_frame
        else:
            print(f"Error: No se encontró la pantalla '{page_name}'")


# Para ejecutar la aplicación
if __name__ == "__main__":
    app = BaseApp()
    app.mainloop()

