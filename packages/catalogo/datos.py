from packages.sap.SAPManager import SAPManager
from packages.lfw_json.json_manager import JSONManager
from packages.db.sql_server_manager import SqlServerManager

class Datos: 
    def __init__(self):
        self._objSAP = SAPManager()
        self._aRubros = []
        self._objSAP.login()


    # Atualiza : Rubros, Subrubros y Marcas
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


    
    def insert_proveedor_if_exist(self, raz_soc, cuit=None):
        oConfig = JSONManager()
        oConfig.file_name = "config.json"
        oConfig.get_content()
        sqlserver = SqlServerManager()
        
        proveedores = sqlserver.getQuery("SELECT razSoc, nroCUIT FROM proveedor WHERE habilitado = 1")
    
        proveedores = [(raz.strip().lower(), c.strip() if c else None) for raz, c in proveedores]


        existe = any(
        raz_soc.strip().lower() == prov[0] or
        (cuit and cuit.strip() == prov[1])
        for prov in proveedores
        )

        if not existe:
            sqlserver.execute("""
                INSERT INTO Proveedor (
                    idProv, razSoc, nomFant, direccion, idLocalid, idCondPago, idSitIVA,
                    nroCUIT, telefono, fax, eMail, pagWeb, observ, contacto, habilitado,
                    tMon, cotizac, idTransp, usuAlta, fecAlta, idHostAlta, usuModi, fecModi,
                    idHostModi, usuBaja, fecBaja, idHostBaja, idTipoDoc
                )
                VALUES (
                    1, 'DER S.A.', 'DER DISTRIBUCIONES', 'COLECTORA ESTE 27887', 195, 1, 1,
                    '30708698152', '4846-7500', NULL, 'INFO@DERDISTRIBUCIONES.COM.AR', 'WWW.DERDISTRIBUCIONES.COM.AR',
                    NULL, NULL, 1, 'PSO', 0, 1, 'SUPER', '2014-03-08 08:14:04.600', 'SIS-65',
                    NULL, NULL, NULL, NULL, NULL, NULL, 1
                )
            """)
            print(f"Proveedor '{raz_soc}' insertado.")
        else:
            print(f"Proveedor '{raz_soc}' o CUIT '{cuit}' ya existe, no se insertará.")



    def insert_unimed_if_exist(self):
        sqlserver = SqlServerManager()
        
        unidades_actuales = sqlserver.getQuery("SELECT codUM FROM unidmed")
        codigos_existentes = [codigo.strip().upper() for (codigo,) in unidades_actuales]

        unidades_a_verificar = [
            ("UNI", "UNIDADES"),
            ("MET", "METROS")
        ]

        for codUM, descripcion in unidades_a_verificar:
            if codUM not in codigos_existentes:
                resultado = sqlserver.getQuery("SELECT ISNULL(MAX(idUniMed), 0) + 1 FROM unidmed")
                proximo_id = resultado[0][0]

                query = """
                INSERT INTO unidmed (idUniMed, codUM, descripcio, usuAlta, fecAlta, idHostAlta)
                VALUES (?, ?, ?, ?, GETDATE(), ?)
                """
                params = (proximo_id, codUM, descripcion, "PYTH", "PYTH-SCRIPT")
                sqlserver.execute(query, params)
                print(f"[INFO] Unidad de medida '{codUM}' insertada con ID {proximo_id}.")
            else:
                print(f"[OK] Unidad de medida '{codUM}' ya existe.")



    def update_articulos(self, recurso, stored_procedure, build_sql_callback):
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


    def logout(self):
        """Cierra sesión en SAP"""
        self._objSAP.logout()