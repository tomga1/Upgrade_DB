import traceback
import pyodbc
from packages.lfw_json.json_manager import JSONManager


class SqlServerManager:
    dbConfig = None
    activeConnection = None

    def __init__(self):
        """
        Constructor de la clase.
        Al instaciar la clase establezco la conexion con SQL SERVER
        """

        oConfig = JSONManager()
        oConfig.file_name = "config.json"
        oConfig.get_content()
        self.dbConfig = oConfig.data

        self.source = self.dbConfig.get("source", "ecommerce")
        sql_config = self.dbConfig[self.source]["sqlserver"]

        conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={sql_config['host']};"
        f"DATABASE={sql_config['database']};"
        f"Trusted_Connection=yes;"
        f"TrustServerCertificate=yes;"
    )
        
        try:
            self.activeConnection = pyodbc.connect(conn_str)
        except Exception as e:
            print("Error al conectar con SQL Server: ")
            traceback.print_exc()
            raise e


    def closeDB(self):
        self.activeConnection.close()

    def execute(self, xsql, xargs=None):
        """
        Ejecuta un comando de inserción o actualización en SQL Server.
        """
        cursor = self.activeConnection.cursor()
        try:
            if xargs is None:
                cursor.execute(xsql)
            else:
                cursor.execute(xsql, xargs)
            self.activeConnection.commit()
        except:
            self.activeConnection.rollback()
            traceback.print_exc()
        finally:
            cursor.close()

    def getQuery(self, xsql, xuseFetchOne = False):
        
        cursor = self.activeConnection.cursor()
        cursor.execute(xsql)
        result = cursor.fetchone() if xuseFetchOne else cursor.fetchall()
        cursor.close()
        return result