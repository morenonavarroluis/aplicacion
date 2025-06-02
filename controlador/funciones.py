from tkinter import messagebox
from modelo.modelo import conectar_db

import mysql.connector

def verificar_credenciales(username, password):
    """Verifica las credenciales del usuario en la base de datos."""
    conexion = conectar_db()
    if conexion is None:
        return False

    cursor = conexion.cursor()
    try:
        # Asumimos que tienes una tabla llamada 'usuarios' con columnas 'username' y 'password'
        # ¡IMPORTANTE! En un entorno de producción, NUNCA almacenes contraseñas en texto plano.
        # Deberías usar hashes de contraseñas (por ejemplo, bcrypt, scrypt, Argon2).
        # Esta consulta es solo para fines demostrativos.
        query = "SELECT password FROM usuario WHERE username = %s"
        cursor.execute(query, (username,))
        resultado = cursor.fetchone()

        if resultado:
            # Aquí deberías comparar el hash de la contraseña almacenada con el hash de la contraseña ingresada.
            # Por simplicidad, aquí comparamos directamente (NO SEGURO PARA PRODUCCIÓN).
            password_almacenada = resultado[0]
            if password == password_almacenada: # En producción: if bcrypt.checkpw(password.encode('utf-8'), password_almacenada.encode('utf-8')):
                return True
            else:
                return False
        else:
            return False # Usuario no encontrado
    except mysql.connector.Error as err:
        messagebox.showerror("Error de Base de Datos", f"Error al consultar la base de datos: {err}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()


