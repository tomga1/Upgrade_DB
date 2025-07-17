# DBSISCOM_upgrade

## SAP → DBSISCOM Sync

Este proyecto permite sincronizar datos desde SAP hacia una base de datos local (`DBSISCOM`) utilizada en el sistema de mostrador.

---

## Funcionalidad

- Conexión a SAP Business One mediante APIs (Service Layer).
- Obtención de entidades como rubros, artículos, marcas, precios, etc.
- Inserción o actualización de los datos en una base de datos SQL Server (`DBSISCOM`).
- Ejecución automatizada de procedimientos almacenados para creación o modificación de estructuras.

---

## Estructura

- `SAPManager`: Maneja login, logout y consumo de endpoints de SAP.
- `SqlServerManager`: Administra la conexión y operaciones sobre SQL Server.
- `Datos`: Clase de ejemplo que muestra cómo consultar y procesar datos de SAP (por ejemplo, rubros).
- `config.json`: Archivo de configuración con las credenciales y endpoints.
- `apply_sp.py`: Script para aplicar procedimientos almacenados de forma automática desde archivos `.sql`.

---

## Requisitos

- Python 3.8+
- `pyodbc`
- `requests`
- Driver ODBC para SQL Server (ej.: ODBC Driver 17 for SQL Server, se instala con SQL Server)

---

## Uso

<!-- ### Sincronización principal: -->

<!-- ```bash -->
<!-- # python main.py


### Para aplicar cambios en la base de datos (crear o modificar procedimientos almacenados):
# Este script debe ejecutarse desde la raíz del proyecto y permite mantener los procedimientos almacenados actualizados automáticamente a partir de archivos .sql.

# python apply_sp.py -->
