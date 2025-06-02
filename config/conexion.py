import mysql.connector
from mysql.connector import Error


def obtener_conexion(): # Esta es la función que te devuelve la conexión
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="lnavarro",
            password="123456",
            database="gestion"
        )
        if conn.is_connected():
            # print("Conexión a la base de datos MySQL exitosa.") # Puedes quitar este print si es muy repetitivo
            return conn
        else:
            print("No se pudo conectar a la base de datos.")
            return None
    except Error as e:
        print(f"Error al intentar conectar a MySQL: {e}")
        return None
