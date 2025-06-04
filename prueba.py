import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def crear_login_con_fondo():
    # --- 1. Configuración de la ventana principal ---
    ventana = tk.Tk()
    ventana.title("Login con Imagen de Fondo")
    ventana.geometry("800x500") # Tamaño fijo para la ventana
    ventana.resizable(False, False) # Evita que se cambie el tamaño de la ventana

    # --- 2. Cargar y preparar la imagen de fondo ---
    try:
        # Asegúrate de que 'fondo.jpg' exista en el mismo directorio que tu script
        # o proporciona la ruta completa a la imagen.
        ruta_imagen = "img/himalaya.png"  # Reemplaza con la ruta a tu imagen
        imagen_original = Image.open(ruta_imagen)

        # Escalar la imagen para que se ajuste al tamaño de la ventana
        ancho_ventana = 800
        alto_ventana = 500
        imagen_redimensionada = imagen_original.resize((ancho_ventana, alto_ventana), Image.LANCZOS)
        fondo_tk = ImageTk.PhotoImage(imagen_redimensionada)

    except FileNotFoundError:
        messagebox.showerror("Error de Imagen", f"No se encontró la imagen: {ruta_imagen}")
        ventana.destroy()
        return
    except Exception as e:
        messagebox.showerror("Error de Imagen", f"Error al cargar la imagen: {e}")
        ventana.destroy()
        return

    # --- 3. Crear un Canvas para el fondo y los widgets ---
    # Un Canvas permite superponer widgets fácilmente sobre una imagen.
    canvas = tk.Canvas(ventana, width=ancho_ventana, height=alto_ventana)
    canvas.pack(fill="both", expand=True)

    # Colocar la imagen en el canvas
    canvas.create_image(0, 0, image=fondo_tk, anchor="nw")

    # --- 4. Crear los widgets del login ---

    # Frame para agrupar los elementos del login y centrarlos visualmente
    # Este frame tendrá un color de fondo semitransparente si lo deseas,
    # o simplemente para organizar.
    frame_login = tk.Frame(canvas, bd=2, relief="groove") # Puedes cambiar 'white' por un color con transparencia
    frame_login.configure(background="#FFFFFF00")  # Color de fondo del frame
    frame_login.place(relx=0.5, rely=0.5, anchor="center", width=300, height=250)
 
    # Etiquetas (Labels)
    lbl_usuario = tk.Label(frame_login, text="Usuario:", bg="white", font=("Arial", 12))
    lbl_usuario.pack(pady=10) # pady para espacio vertical

    # Entradas de texto (Entry)
    entrada_usuario = tk.Entry(frame_login, width=30, font=("Arial", 12))
    entrada_usuario.pack(pady=5)

    lbl_contrasena = tk.Label(frame_login, text="Contraseña:", bg="white", font=("Arial", 12))
    lbl_contrasena.pack(pady=10)

    entrada_contrasena = tk.Entry(frame_login, show="*", width=30, font=("Arial", 12)) # 'show' para ocultar contraseña
    entrada_contrasena.pack(pady=5)

    # Función para el botón de login
    def verificar_login():
        usuario = entrada_usuario.get()
        contrasena = entrada_contrasena.get()

        if usuario == "admin" and contrasena == "1234": # Credenciales de ejemplo
            messagebox.showinfo("Login Exitoso", "¡Bienvenido!")
            # Aquí podrías cerrar la ventana de login y abrir otra ventana principal
            ventana.destroy()
        else:
            messagebox.showerror("Error de Login", "Usuario o contraseña incorrectos.")

    # Botón de Login
    btn_login = tk.Button(frame_login, text="Iniciar Sesión", command=verificar_login,
                          bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="raised")
    btn_login.pack(pady=20)

    # --- 5. Ejecutar la aplicación ---
    ventana.mainloop()

# Llamar a la función para crear el login
crear_login_con_fondo()