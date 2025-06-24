from packages.sap.SAPManager import SAPManager
from packages.lfw_json.json_manager import JSONManager
from packages.db.sql_server_manager import SqlServerManager

class Articulos: 
    def __init__(self):
        self._objSAP = SAPManager()
        self._aRubros = []

        self._objSAP.login()


    def insert_familias(self):
        sap = SAPManager()
        oConfig = JSONManager()
        oConfig.file_name = "config.json"
        oConfig.get_content()
        sqlserver = SqlServerManager()

        sap.login_if_source_is_sap(sqlserver)

        procesados = 0 

        if sqlserver.source == "sap":
            rubros = sap.getData("rubros", None)

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

    def insert_sub_familias(self):
        sap = SAPManager()
        oConfig = JSONManager()
        oConfig.file_name = "config.json"
        oConfig.get_content()
        sqlserver = SqlServerManager()

        sap.login_if_source_is_sap(sqlserver)

        procesados = 0 

        if sqlserver.source == "sap":
            subrubros = sap.getData("subrubros", None)

        try:
            for subrubro in subrubros["value"]:
                sql = f"EXEC sp_sap_subfamilias_insert '{subrubro['SubRubroName']}'"
                sqlserver.execute(sql)
                procesados += 1
                print(f"Sub_rubros procesados : {procesados}")
            sqlserver.closeDB()
            print(f"Sub_rubros Finalizado")
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")

        sap.logout_if_source_is_sap(sqlserver)

    def insert_marcas(self):
        sap = SAPManager()
        oConfig = JSONManager()
        oConfig.file_name = "config.json"
        oConfig.get_content()
        sqlserver = SqlServerManager()

        sap.login_if_source_is_sap(sqlserver)

        procesados = 0 

        if sqlserver.source == "sap":
            marcas = sap.getData("marcas", None)

        try:
            for marca in marcas["value"]:
                sql = f"EXEC sp_sap_marcas_insert '{marca['MarcaName']}'"
                sqlserver.execute(sql)
                procesados += 1
                print(f"Marcas procesadas : {procesados}")
            sqlserver.closeDB()
            print(f"Marcas Finalizado")
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")

        sap.logout_if_source_is_sap(sqlserver)







    def logout(self):
        """Cierra sesión en SAP"""
        self._objSAP.logout()