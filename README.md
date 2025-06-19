# DBSISCOM_upgrade

# SAP → DBSISCOM Sync

Este proyecto permite sincronizar datos desde SAP hacia una base de datos local (`DBSISCOM`) utilizada en el sistema de mostrador.

## Funcionalidad

- Conexión a SAP Business One mediante APIs (Service Layer).
- Obtención de entidades como rubros, artículos, marcas, precios, etc.
- Inserción o actualización de los datos en una base de datos SQL Server (`DBSISCOM`).

## Estructura

- `SAPManager`: Maneja login, logout y consumo de endpoints de SAP.
- `SqlServerManager`: Administra la conexión y operaciones sobre SQL Server.
- `Articulos`: Clase de ejemplo que muestra cómo consultar y procesar datos de SAP (por ejemplo, rubros).
- `config.json`: Archivo de configuración con las credenciales y endpoints.

## Requisitos

- Python 3.8+
- `pyodbc`
- `requests`
- Driver ODBC para SQL Server (ej.: ODBC Driver 17 for SQL Server)

## Uso

```bash
python main.py
