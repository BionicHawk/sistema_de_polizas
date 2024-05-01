from datetime import datetime

class Poliza:
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float):
        self.num_poliza = num_poliza
        self.fecha_inicial = datetime.now()
        self.fecha_final = fecha_final
        self.costo = costo


class Vehicular(Poliza):
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float, marca: str, modelo: str):
        super().__init__(num_poliza, fecha_final, costo)
        self.marca = marca
        self.modelo = modelo


class Inmueble(Poliza):
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float, direccion: str, area: float):
        super().__init__(num_poliza, fecha_final, costo)
        self.direccion = direccion
        self.area = area
    

class Adicional(Poliza):
    def __init__(self, num_poliza: int, fecha_final: datetime, costo: float, titulo: str, descripcion: str):
        super().__init__(num_poliza, fecha_final, costo)
        self.titulo = titulo
        self.descripcion = descripcion
