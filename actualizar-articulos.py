from packages.catalogo.articulos import Articulos
import time

start_time = time.perf_counter()


oArticulos = Articulos()
oArticulos.insert_familias()
oArticulos.insert_sub_familias()
oArticulos.insert_marcas()


elapsed_time = time.perf_counter() - start_time
minute = int(elapsed_time / 60)
seconds = int(elapsed_time % 60)
print(f"Tiempo duracion tota: {minute}.{seconds} ")