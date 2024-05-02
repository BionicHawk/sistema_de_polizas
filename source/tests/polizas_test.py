import pytest
from datetime import datetime, timedelta
from ..models.polizas import Adicional, Inmueble

@pytest.fixture
def inmueble_de_prueba():
    return Inmueble(
        num_poliza=123456,
        fecha_final=datetime.now() + timedelta(days=365),
        costo=1000,
        direccion='Calle Principal 123',
        area=50,
        titular='Juan Perez'
    )

def test_calculo_costo_inmueble(inmueble_de_prueba):
    assert inmueble_de_prueba.calcular_costo_poliza_inmueble() == 1000 * 50 * 0.3

def test_generar_informe_inspeccion_inmueble(inmueble_de_prueba):
    informe = inmueble_de_prueba.generar_informe_inspeccion()
    assert f'El valor de la póliza 123456 para el inmueble Calle Principal 123 a nombre de Juan Perez tendrá un costo de ${inmueble_de_prueba.calcular_costo_poliza_inmueble()}' in informe

@pytest.fixture
def adicional_de_prueba():
    return Adicional(
        num_poliza=789012,
        fecha_final=datetime.now() + timedelta(days=365),
        costo=500,
        titulo='Cobertura adicional',
        descripcion='Cobertura extra para daños accidentales',
        titular='María López'
    )

def test_calculo_costo_adicional(adicional_de_prueba):
    # Asumiendo que la clase Adicional tiene un atributo `area`
    assert adicional_de_prueba.calcular_costo_poliza() == 500 * 0.3

def test_generar_informe_inspeccion_adicional(adicional_de_prueba):
    informe = adicional_de_prueba.generar_informe_inspeccion()
    assert f'El valor de la póliza 789012 para el inmueble {adicional_de_prueba.direccion} a nombre de {adicional_de_prueba.titular} tendrá el costo ${adicional_de_prueba.calcular_costo_poliza()}' in informe
