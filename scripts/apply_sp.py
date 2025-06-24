import pyodbc
import os
from packages.db.sql_server_manager import SqlServerManager


def ejecutar_scripts_sp(ruta_carpeta = "sp"):
    gestor_sql = SqlServerManager()

    for archivo in os.listdir(ruta_carpeta):
        if archivo.endswith(".sql"):
            ruta_carpeta = os.path.join(ruta_carpeta, archivo)
            with open(ruta_carpeta, 'r', encoding='utf-8') as file:
                script = file.read()
                try:
                    gestor_sql.execute(script)
                    print(f"Script {archivo} ejecutado correctamente.")
                except pyodbc.Error as e:
                    print(f"Error al ejecutar el script {archivo}: {e}")
                except Exception as e:
                    print(f"Error inesperado al ejecutar el script {archivo}: {e}")

    gestor_sql.closeDB()

if __name__ == "__main__":
    ejecutar_scripts_sp()