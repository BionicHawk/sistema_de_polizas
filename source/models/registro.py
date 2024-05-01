from datetime import datetime


class Registro:

    def __init__(self, razon: str, expedicion: datetime, monto: float, vencimiento: datetime):
        self.razon = razon
        self.expedicion = expedicion
        self.monto = monto
        self.vencimiento = vencimiento
