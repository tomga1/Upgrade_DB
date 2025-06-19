from packages.sap.SAPManager import SAPManager

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



    def logout(self):
        """Cierra sesión en SAP"""
        self._objSAP.logout()