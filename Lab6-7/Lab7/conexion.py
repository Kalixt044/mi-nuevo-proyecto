import sqlite3
import os

class Conexion:
    def __init__(self, name_db):
        # Asegurarse de que el directorio de la base de datos exista
        os.makedirs(os.path.dirname(name_db), exist_ok=True)
        
        self.name_db = name_db
        self.conn = None
        self.cursor = None

    def abrir_conexion(self):
        try:
            self.conn = sqlite3.connect(self.name_db)
            self.cursor = self.conn.cursor()
            print("Conexion exitosa.")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar_conexion(self):
        if self.conn:
            self.conn.close()
            print("Conexion cerrada.")
