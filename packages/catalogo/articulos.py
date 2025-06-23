from packages.sap.SAPManager import SAPManager
from packages.lfw_json.json_manager import JSONManager
from packages.db.sql_server_manager import SqlServerManager

class Articulos: 
    def __init__(self):
        self._objSAP = SAPManager()
        self._aRubros = []

        self._objSAP.login()


    def recibir_rubros(self):
        try:
            print("Obteniendo rubros desde SAP...")
            datos_rubros = self._objSAP.getData("rubros")

            self._aRubros = datos_rubros.get("value", [])

            print(f"Cantidad de rubros recibidos: {len(self._aRubros)}")
            for rubro in self._aRubros[:10]: 
                print(f"Código: {rubro.get('RubroCode')}, Nombre: {rubro.get('RubroName')}")
        except Exception as e:
            print("Ocurrió un error al obtener los rubros:")
            print(e)


    def insertFamilias(self):
        sap = SAPManager()
        oConfig = JSONManager()
        oConfig.file_name = "config.json"
        oConfig.get_content()
        sqlserver = SqlServerManager()

        sap.login_if_source_is_sap(sqlserver)

        procesados = 0 

        if sqlserver.source == "sap":
            rubros = sap.getData("rubros", None)

        sap.logout_if_source_is_sap(sqlserver)

        try:
            for rubro in rubros["value"]:
                sql = f"EXEC sp_sap_familias_insert '{rubro['RubroName']}'"
                sqlserver.execute(sql)
                procesados += 1
                print(f"Rubros procesados : {procesados}")
            sqlserver.closeDB()
            print(f"Rubros Finalizado")
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")

        sap.logout_if_source_is_sap(sqlserver)







    def logout(self):
        """Cierra sesión en SAP"""
        self._objSAP.logout()