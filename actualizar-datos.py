from packages.catalogo.datos import Datos
import time

start_time = time.perf_counter()


oDatos = Datos()


oDatos.update_datos(
    recurso="rubros",
    stored_procedure="sp_sap_familias_insert",
    build_sql_callback=lambda item, sp: f"EXEC {sp} '{item['RubroName']}'"
)
oDatos.update_datos(
    recurso="subrubros",
    stored_procedure="sp_sap_subfamilias_insert",
    build_sql_callback=lambda item, sp: f"EXEC {sp} '{item['SubRubroName']}'"
)
oDatos.update_datos(
    recurso="marcas",
    stored_procedure="sp_sap_marcas_insert",
    build_sql_callback=lambda item, sp: f"EXEC {sp} '{item['MarcaName']}'"
)
oDatos.update_datos(
    recurso="art-cbios",
    stored_procedure="sp_sap_art_cbios",
    build_sql_callback=lambda item, sp: f"EXEC {sp} '{item['ItemCode']}','{item['Price']}'"
)





elapsed_time = time.perf_counter() - start_time
minute = int(elapsed_time / 60)
seconds = int(elapsed_time % 60)
print(f"Tiempo duracion tota: {minute}.{seconds} ")