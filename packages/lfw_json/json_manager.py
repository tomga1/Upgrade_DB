import json

class JSONManager :
    """
    Esta clase permite obtener el contenido de un archivo JSON
    """
    file_name = ""
    data = ""

    def __init__(self, file_name = "config.json") :
        self.file_name = file_name
        self.data = None
        

    def get_content (self) :
        """
        Obtiene el contenido de un archivo JSOsas
        """
        with open(self.file_name) as file:
            self.data = json.load(file)