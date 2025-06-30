from packages.sap.SAPManager import SAPManager
from packages.lfw_json.json_manager import JSONManager
from packages.db.sql_server_manager import SqlServerManager

class Datos: 
    def __init__(self):
        self._objSAP = SAPManager()
        self._aRubros = []
        self._objSAP.login()




    def update_datos(self, recurso, stored_procedure, build_sql_callback):
        sap = SAPManager()
        oConfig = JSONManager()
        oConfig.file_name = "config.json"
        oConfig.get_content()
        sqlserver = SqlServerManager()

        sap.login_if_source_is_sap(sqlserver)

        procesados = 0 

        if sqlserver.source == "sap":
            datos = sap.getData(recurso, None)

        try:
            for item in datos["value"]:
                sql = build_sql_callback(item, stored_procedure)
                sqlserver.execute(sql)
                procesados += 1
                print(f"{recurso.capitalize()} procesados: {procesados}")
                
            sqlserver.closeDB()
            print(f"{recurso.capitalize()} Finalizado")
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")

        sap.logout_if_source_is_sap(sqlserver)


    def insert_proveedor_if_exist(self, raz_soc, cuit, habilitado=1):
        oConfig = JSONManager()
        oConfig.file_name = "config.json"
        oConfig.get_content()
        sqlserver = SqlServerManager()
        
        proveedores = sqlserver.getQuery("SELECT razSoc FROM proveedor WHERE habilitado = 1")

        proveedores = [prov[0].strip() for prov in proveedores]

        if raz_soc.strip() not in proveedores:
            sqlserver.execute(
                "insert into proveedor (razSoc, cuit, habilitado) values ('DER S.A.', '30-70700000-0', 1)"),
            ()
        else:
            print("Proveedor 'DER S.A' ya existe, no se insertará.")

        # try:
        #     for rubro in rubros["value"]:
        #         sql = f"EXEC sp_sap_familias_insert '{rubro['RubroName']}'"
        #         sqlserver.execute(sql)
        #         procesados += 1
        #         print(f"Rubros procesados : {procesados}")
        #     sqlserver.closeDB()
        #     print(f"Rubros Finalizado")
        # except BaseException as err:
        #     print(f"Unexpected {err=}, {type(err)=}")

        # sap.logout_if_source_is_sap(sqlserver)




    def logout(self):
        """Cierra sesión en SAP"""
        self._objSAP.logout()