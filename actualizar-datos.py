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

oDatos.insert_proveedor_if_exist(
    "DER S.A.", '30708698152'
)

oDatos.insert_unimed_if_exist()


# oDatos.update_articulos(
#     recurso="articulos",
#     stored_procedure="ProcesarArticuloSAP",
#     build_sql_callback = lambda item, sp: f"""EXEC {sp} 
#         '{item['ItemCode']}',
#         '{item['ItemName'].replace("'", "''")}',
#         {int(item['RubroCod']) if item.get('RubroCod') else 0},
#         {int(item['SubRubroCod']) if item.get('SubRubroCod') else 0},
#         {int(item['MarcaCod']) if item.get('MarcaCod') else 0},
#         {float(item['IvaRate']) if item.get('IvaRate') else 0},
#         {'\'S\'' if item.get('Habilitado', 'N').upper() == 'S' else '\'N\''},
#         '{item['CreateDate'].strftime("%Y-%m-%d") if hasattr(item['CreateDate'], 'strftime') else item['CreateDate']}',
#         '{item['UpdateDate'].strftime("%Y-%m-%d") if hasattr(item['UpdateDate'], 'strftime') else item['UpdateDate']}'
#     """
# )





# oDatos.update_datos(
#     recurso="art-cbios",
#     stored_procedure="sp_sap_art_cbios",
#     build_sql_callback=lambda item, sp: f"EXEC {sp} '{item['ItemCode']}','{item['Price']}'"
# )




elapsed_time = time.perf_counter() - start_time
minute = int(elapsed_time / 60)
seconds = int(elapsed_time % 60)
print(f"Tiempo duracion tota: {minute}.{seconds} ")