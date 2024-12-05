import sqlite3
from app_crud import CRUD

def main():
    try:
        # Crear la carpeta de base de datos si no existe
        import os
        os.makedirs('./db', exist_ok=True)
        
        # Iniciar la aplicación CRUD
        db_conex = CRUD('./db/estudiantes.db')
        db_conex.abrir_conexion()
        db_conex.opciones()
    except sqlite3.Error as e:
        print(f"Error al iniciar la aplicación: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
