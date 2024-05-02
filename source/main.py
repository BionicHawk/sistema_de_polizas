from datetime import datetime
from models.polizas import Inmueble

inmueble = Inmueble(
    costo=5000,
    direccion='Calle del sexo',
    num_poliza=84848,
    fecha_final= datetime.now(),
    area=500,
    titular='Dante de Lordran'
)

print(inmueble.generar_informe_inspeccion())