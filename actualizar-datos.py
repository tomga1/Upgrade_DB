from packages.catalogo.datos import Datos
import time

start_time = time.perf_counter()


oArticulos = Datos()


oArticulos.update_datos(
    recurso="rubros",
    stored_procedure="sp_sap_familias_insert",
    build_sql_callback=lambda item, sp: f"EXEC {sp} '{item['RubroName']}'"
)
oArticulos.update_datos(
    recurso="subrubros",
    stored_procedure="sp_sap_subfamilias_insert",
    build_sql_callback=lambda item, sp: f"EXEC {sp} '{item['SubRubroName']}'"
)
oArticulos.update_datos(
    recurso="marcas",
    stored_procedure="sp_sap_marcas_insert",
    build_sql_callback=lambda item, sp: f"EXEC {sp} '{item['MarcaName']}'"
)






elapsed_time = time.perf_counter() - start_time
minute = int(elapsed_time / 60)
seconds = int(elapsed_time % 60)
print(f"Tiempo duracion tota: {minute}.{seconds} ")