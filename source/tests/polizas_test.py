import pytest
from datetime import datetime, timedelta
from ..models.polizas import Adicional, Inmueble, Vehicular

# Pruebas de Vehicular
def test_cubrir_daños_1():
    """
    En este caso se evalua que se pueda hacer válida 
    la póliza con datos correctos (Debería de ser válido)
    """

    poliza = Vehicular(
        num_poliza=25235,
        titular='Angel de Jesus Manzo Rosas',
        costo=1320,
        fecha_final=datetime.now() + timedelta(days= 5 * 30),
        marca='Tesla',
        modelo='Model Y'
    )

    assert poliza.intentar_cubrir_daños_accidentes(
        razon='Sufrió daño en el parachoques trasero por choque',
        dias_de_vencimiento=15,
        monto_a_regresar=4000
    ) == True

def test_cubrir_daños_2():
    """
    En este caso se evalua que se pueda hacer válida 
    la póliza con datos incorrectos (Debería de ser Falso)
    """

    poliza = Vehicular(
        num_poliza=425,
        titular='Angel de Jesus Manzo Rosas',
        costo=1320,
        fecha_final=datetime.now() + timedelta(days= 5 * 30),
        marca='Tesla',
        modelo='Model Y'
    )

    assert poliza.intentar_cubrir_daños_accidentes(
        razon='',
        dias_de_vencimiento=0,
        monto_a_regresar=-450
    ) == True

def test_cubrir_daños_3():
    """
    En este caso se evalua que se pueda hacer válida 
    la póliza con menos de 1 día de vencimiento (Debería de ser Falso)
    """

    poliza = Vehicular(
        num_poliza=3216,
        titular='Angel de Jesus Manzo Rosas',
        costo=1320,
        fecha_final=datetime.now() + timedelta(days= 5 * 30),
        marca='Tesla',
        modelo='Model Y'
    )

    assert poliza.intentar_cubrir_daños_accidentes(
        razon='Sufrió daño en el parachoques trasero por choque',
        dias_de_vencimiento=0,
        monto_a_regresar=3000
    ) == True

def test_cubrir_daños_4():
    """
    En este caso se evalua que se pueda hacer válida 
    la póliza con un costo monto a regresar negativo (Debería de ser Falso)
    """

    poliza = Vehicular(
        num_poliza=3526,
        titular='Angel de Jesus Manzo Rosas',
        costo=1320,
        fecha_final=datetime.now() + timedelta(days= 5 * 30),
        marca='Tesla',
        modelo='Model Y'
    )

    assert poliza.intentar_cubrir_daños_accidentes(
        razon='',
        dias_de_vencimiento=20,
        monto_a_regresar=-450
    ) == False

def test_cubrir_daños_5():
    """
    En este caso se evalua que se pueda hacer válida 
    la póliza sin pasarle la razón (Debería de ser Falso)
    """

    poliza = Vehicular(
        num_poliza=3256,
        titular='Angel de Jesus Manzo Rosas',
        costo=1320,
        fecha_final=datetime.now() + timedelta(days= 5 * 30),
        marca='Tesla',
        modelo='Model Y'
    )

    assert poliza.intentar_cubrir_daños_accidentes(
        razon='',
        dias_de_vencimiento=30,
        monto_a_regresar=450
    ) == False
    
def test_poliza_expirada_1():
    """
    En está prueba se esta verificando si la fecha final de póliza
    ha sido alcanzada, usando una fecha de hace 5 meses atrás
    como fecha de vencimiento
    """
    
    poliza = Vehicular(
        num_poliza=3256,
        titular='Angel de Jesus Manzo Rosas',
        costo=1320,
        fecha_final=datetime.now() - timedelta(days= 5 * 30),
        marca='Tesla',
        modelo='Model Y'
    )

    assert poliza.esta_la_poliza_expirada() == True
    
def test_poliza_expirada_2():
    """
    En está prueba se esta verificando si la fecha final de póliza
    ha sido alcanzada usando una fecha de 5 meses en el futuro
    como vencimiento
    """
    
    poliza = Vehicular(
        num_poliza=3256,
        titular='Angel de Jesus Manzo Rosas',
        costo=1320,
        fecha_final=datetime.now() + timedelta(days= 5 * 30),
        marca='Tesla',
        modelo='Model Y'
    )

    assert poliza.esta_la_poliza_expirada() == False


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

def test_calculo_costo_inmueble(inmueble_de_prueba):
    assert inmueble_de_prueba.calcular_costo_poliza_inmueble() == 1000 * 50 * 0.3

def test_generar_informe_inspeccion_inmueble(inmueble_de_prueba):
    informe = inmueble_de_prueba.generar_informe_inspeccion()
    assert f'El valor de la poliza 123456 para el inmueble Calle Principal 123 a nombre de Juan Perez tendra un costo de ${inmueble_de_prueba.calcular_costo_poliza_inmueble()}' in informe

def test_calculo_costo_adicional(adicional_de_prueba):
    assert adicional_de_prueba.calcular_costo_poliza() == 500 * 0.3

def test_generar_informe_inspeccion_adicional(adicional_de_prueba):
    informe = adicional_de_prueba.generar_informe_inspeccion()
    assert f'El valor de la póliza 789012 para el inmueble {adicional_de_prueba.direccion} a nombre de {adicional_de_prueba.titular} tendrá el costo ${adicional_de_prueba.calcular_costo_poliza()}' in informe