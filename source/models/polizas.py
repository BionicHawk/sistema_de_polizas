from datetime import datetime, timedelta
from .registro import Registro


class Poliza:
    num_poliza: int
    fecha_inicial: datetime = datetime.now()
    fecha_final: datetime
    costo: float


class Vehicular(Poliza):
    marca: str
    modelo: str
    titular: str
    registros: list[Registro]

    def intentar_cubrir_daños_accidentes(self, razon: str, dias_de_vencimiento: int, monto_a_regresar: float = 0.0) -> bool:
        if dias_de_vencimiento < 1 or monto_a_regresar == 0.0 or len(razon) == 0:
            return False

        today = datetime.now()

        self.registros.append(Registro(
            razon=razon,
            expedicion=today,
            monto=monto_a_regresar,
            vencimiento=today + timedelta(days=dias_de_vencimiento)
        ))

        return True


class Inmueble(Poliza):
    direccion: str
    area: float
    titular: str


class Adicional(Poliza):
    titulo: str
    descripcion: str
    titular: str
