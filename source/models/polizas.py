from datetime import datetime


class Poliza:
    num_poliza: int
    fecha_inicial: datetime = datetime.now()
    fecha_final: datetime
    costo: float


class Vehicular(Poliza):
    pass


class Inmueble(Poliza):
    pass


class Adicional(Poliza):
    pass
