from datetime import datetime, timedelta
from .registro import Registro


class Poliza:
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float):
        self.num_poliza = num_poliza
        self.fecha_inicial = datetime.now()
        self.fecha_final = fecha_final
        self.costo = costo


class Vehicular(Poliza):
    
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float, marca : str, modelo: str, titular:str, registros: list[Registro]):
        super().__init__(num_poliza, fecha_final, datetime, costo)
        self.marca = marca
        self.modelo=modelo
        self.titular = titular
        self.registros = registros

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
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float, direccion:str , area:float, titular:str):
        super().__init__(num_poliza, fecha_final, datetime, costo)
        self.direccion = direccion
        self.area = area
        self.titular = titular
        
    def calcular_poliza_inmueble():
        return


class Adicional(Poliza):
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float , titulo : str , descripcion: str, titular : str):
        super().__init__(num_poliza, fecha_final, datetime, costo)
        self.titulo = titulo
        self.descripcion = descripcion
        self.titular = titular