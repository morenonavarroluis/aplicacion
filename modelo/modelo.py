import mysql.connector
from tkinter import messagebox
from config.conexion import obtener_conexion
# --- Configuración de la Base de Datos ---
# Asegúrate de que estos detalles coincidan con tu configuración de MySQL
DB_CONFIG = {
    'host': 'localhost',
    'user': 'lnavarro', # Reemplaza con tu usuario
    'password': '123456', # Reemplaza con tu contraseña
    'database': 'gestion' # Reemplaza con tu base de datos
}

# --- Funciones ---

def conectar_db():
    """Establece conexión con la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error de Conexión", f"No se pudo conectar a la base de datos: {err}")
        return None
    

def obtener_datos_usuarios():
    """
    Ejecuta la consulta SQL y devuelve los datos de los usuarios.
    Maneja la conexión a la base de datos de forma segura.
    """
    conn = None # Inicializa conn a None
    cursor = None # Inicializa cursor a None
    try:
        # CORRECTO: Llama a la función 'obtener_conexion()'
        conn = obtener_conexion()
        if conn is None: # Si la conexión falla, obtener_conexion() devuelve None
            print("Error: No se pudo establecer la conexión a la base de datos.")
            return []

        cursor = conn.cursor()
        cursor.execute("""
            SELECT em.id, em.nombre, em.apellido, dep.dependencias, em.cantidad
            FROM empleado AS em
            INNER JOIN dependencias AS dep ON em.dependencia = dep.id_d;
        """)
        datos = cursor.fetchall()
        return datos
    except Exception as e:
        print(f"Error al obtener datos de la base de datos: {e}")
        return [] # Retorna una lista vacía en caso de error
    finally:
        # Asegúrate de cerrar el cursor y la conexión si se crearon
        if cursor:
            cursor.close()
        if conn:
            conn.close()
