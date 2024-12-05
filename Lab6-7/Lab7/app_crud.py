import sqlite3
from conexion import Conexion

class CRUD(Conexion):
    def crear_tabla(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS estudiantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(50),
                    edad INTEGER,
                    ciudad VARCHAR(50)
                )
            ''')
            self.conn.commit()
            print("Tabla de estudiantes creada exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def insertar_estudiante(self, nombre, edad, ciudad):
        try:
            self.cursor.execute('''
                INSERT INTO estudiantes (nombre, edad, ciudad) 
                VALUES (?, ?, ?)
            ''', (nombre, edad, ciudad))
            self.conn.commit()
            print("Estudiante insertado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar estudiante: {e}")

    def consultar_estudiantes(self):
        try:
            self.cursor.execute('SELECT * FROM estudiantes')
            estudiantes = self.cursor.fetchall()
            
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                print("\nLista de Estudiantes:")
                print("-" * 50)
                print("ID | Nombre | Edad | Ciudad")
                print("-" * 50)
                for estudiante in estudiantes:
                    print(f"{estudiante[0]} | {estudiante[1]} | {estudiante[2]} | {estudiante[3]}")
        except sqlite3.Error as e:
            print(f"Error al consultar estudiantes: {e}")

    def actualizar_estudiante(self, id_estudiante, nombre=None, edad=None, ciudad=None):
        try:
            update_fields = []
            params = []
            
            if nombre:
                update_fields.append("nombre = ?")
                params.append(nombre)
            if edad is not None:
                update_fields.append("edad = ?")
                params.append(edad)
            if ciudad:
                update_fields.append("ciudad = ?")
                params.append(ciudad)
            
            params.append(id_estudiante)
            
            if update_fields:
                query = f"UPDATE estudiantes SET {', '.join(update_fields)} WHERE id = ?"
                self.cursor.execute(query, params)
                self.conn.commit()
                
                if self.cursor.rowcount > 0:
                    print("Estudiante actualizado correctamente.")
                else:
                    print("No se encontró un estudiante con ese ID.")
            else:
                print("No se proporcionaron campos para actualizar.")
                
        except sqlite3.Error as e:
            print(f"Error al actualizar estudiante: {e}")

    def eliminar_estudiante(self, id_estudiante):
        try:
            self.cursor.execute('DELETE FROM estudiantes WHERE id = ?', (id_estudiante,))
            self.conn.commit()
            
            if self.cursor.rowcount > 0:
                print("Estudiante eliminado correctamente.")
            else:
                print("No se encontró un estudiante con ese ID.")
        except sqlite3.Error as e:
            print(f"Error al eliminar estudiante: {e}")

    def opciones(self):
        while True:
            print("\n--- Menú de Gestión de Estudiantes ---")
            print("1. Crear Tabla de Estudiantes")
            print("2. Insertar Estudiante")
            print("3. Consultar Estudiantes")
            print("4. Actualizar Estudiante")
            print("5. Eliminar Estudiante")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.crear_tabla()
            elif opcion == '2':
                nombre = input("Ingrese el nombre del estudiante: ")
                edad = int(input("Ingrese la edad del estudiante: "))
                ciudad = input("Ingrese la ciudad del estudiante: ")
                self.insertar_estudiante(nombre, edad, ciudad)
            elif opcion == '3':
                self.consultar_estudiantes()
            elif opcion == '4':
                id_estudiante = int(input("Ingrese el ID del estudiante a actualizar: "))
                nombre = input("Ingrese el nuevo nombre (deje en blanco para no modificar): ")
                edad_str = input("Ingrese la nueva edad (deje en blanco para no modificar): ")
                ciudad = input("Ingrese la nueva ciudad (deje en blanco para no modificar): ")
                
                edad = int(edad_str) if edad_str else None
                
                self.actualizar_estudiante(id_estudiante, nombre or None, edad, ciudad or None)
            elif opcion == '5':
                id_estudiante = int(input("Ingrese el ID del estudiante a eliminar: "))
                self.eliminar_estudiante(id_estudiante)
            elif opcion == '6':
                self.cerrar_conexion()
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")
