from datetime import datetime


class Poliza:
    num_poliza: int
    fecha_inicial: datetime = datetime.now()
    fecha_final: datetime
    costo: float


class Vehicular(Poliza):
    marca: str
    modelo: str


class Inmueble(Poliza):
    direccion: str
    area: float


class Adicional(Poliza):
    titulo: str
    descripcion: str
