"""
Clase: SAPManager
Descripción:
    Permite manejar las APIs de SAP.
"""
import requests
import json
from packages.lfw_json.json_manager import JSONManager

class SAPManager:
    configuracion = None
    sessionId = ""

    def __init__(self):
        """ Constructor de clase """
        oConfig = JSONManager()
        oConfig.file_name = "config.json"
        oConfig.get_content()
        self.configuracion = oConfig.data

    def login (self):
        """ 
            Este método permite loguearse en SAP
        """
        url = self.configuracion["sap"]["urls"]["login"]
        body = self.configuracion["sap"]["body"]
        headers = {
            "Content-Type": "application/json"
            #"Prefer": "odata.maxpagesize=1"
        }
        respuesta = requests.post(url, headers=headers, data=json.dumps(body), verify=False).json()
        self.sessionId = respuesta["SessionId"]

    def login_if_source_is_sap(self, dbManager):
        """Verifica si la fuente es 'sap' y realiza el login si corresponde."""
        if dbManager.source == "sap" and not self.sessionId:
            self.login()

    def getData (self, xurlName, xfilter = None, xskip = 0, header = ''):
        """ 
            Este método devuelve un dato a partir del nombre de una URL definida en
            el archivo config.json.
            Devuelve un array JSON con los datos de la API
        """
        if xfilter == None:
            url = self.configuracion["sap"]["urls"][xurlName]
        else:
            url = self.configuracion["sap"]["urls"][xurlName] + "?$filter=" + xfilter

        if xskip != 0 :
            url = url + "?$skip=" + str(xskip)

        headers = {
            "Content-Type": "application/json",
            "Cookie": 'B1SESSION=' + self.sessionId + "; ROUTER.node1",
            "Prefer": "odata.maxpagesize=0"
        }
        if (header != ""):
            headers = header
            
        result = requests.get(url, headers=headers, verify=False).json()
        return result

    def logout (self):
        """ Permite desconectarse de SAP """
        url = self.configuracion["sap"]["urls"]["logout"]
        headers = {
            "Content-Type": "application/json",
            "Cookie": 'B1SESSION=' + str(self.sessionId) + "; ROUTER.node1"
        }
        result = requests.post(url, headers=headers, verify=False)
        self.sessionId = None

    def logout_if_source_is_sap(self, dbManager):
        """Verifica si la fuente es 'sap' y realiza el logout si corresponde."""
        if dbManager.source == "sap" and self.sessionId:
            self.logout()