from datetime import datetime, timedelta
from .registro import Registro


class Poliza:
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float):
        self.num_poliza = num_poliza
        self.fecha_inicial = datetime.now()
        self.fecha_final = fecha_final
        self.costo = costo


class Vehicular(Poliza):

    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float, marca: str, modelo: str, titular: str):
        super().__init__(num_poliza, fecha_final, costo)
        self.marca = marca
        self.modelo = modelo
        self.titular = titular
        self.registros: list[Registro] = []

    def intentar_cubrir_daños_accidentes(self, razon: str, dias_de_vencimiento: int, monto_a_regresar: float = 0.0) -> bool:
        if dias_de_vencimiento < 1 or monto_a_regresar <= 0.0 or len(razon) == 0:
            return False

        today = datetime.now()

        self.registros.append(Registro(
            razon=razon,
            expedicion=today,
            monto=monto_a_regresar,
            vencimiento=today + timedelta(days=dias_de_vencimiento)
        ))

        return True

    def esta_la_poliza_expirada(self) -> bool:
        remaining_days = self.fecha_final - datetime.now()
        return remaining_days.seconds <= 0.0


class Inmueble(Poliza):
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float, direccion: str, area: float, titular: str):
        super().__init__(num_poliza, fecha_final, costo)
        self.direccion = direccion
        self.area = area
        self.titular = titular

    def calcular_costo_poliza_inmueble(self) -> float:
        return (self.costo * self.area) * 0.3

    def generar_informe_inspeccion(self) -> str:
        return f'El valor de la poliza {self.num_poliza} para el inmueble {self.direccion} a nombre de {self.titular} tendra un costo de ${self.calcular_costo_poliza_inmueble()}'


class Adicional(Poliza):
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float, titulo: str, descripcion: str, titular: str):
        super().__init__(num_poliza, fecha_final, costo)
        self.titulo = titulo
        self.descripcion = descripcion
        self.titular = titular

    def calcular_costo_poliza(self) -> float:
        return (self.costo * self.area) * 0.3

    def generar_informe_inspeccion(self) -> str:
        return f'El valor de la poliza {self.num_poliza} para el inmueble {self.direccion} a nombre de {self.titular} tendra el costo ${self.calcular_costo_poliza()}'
