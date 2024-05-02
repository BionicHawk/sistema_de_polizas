from source.models.polizas import Poliza, Vehicular, Inmueble, Adicional
from datetime import datetime, timedelta
import re

running = True
polizas: list[Poliza] = []


def mostrar_menu() -> int:
    is_input_right = False
    selected_value = -1
    while not is_input_right:
        print('[==== Seleccione alguna de las opciones ====]\n')
        print('\t1. Registrar una póliza\n\t2. Actualizar una póliza\n\t3. Eliminar una póliza\n\t4. Salir\n')
        response = input('> ')

        if response >= '1' and response <= '4':
            selected_value = int(response)
            is_input_right = True
            continue

        print("\n¡Lo siento, el valor dado es inválido!\n")

    return selected_value


def mostrar_menu_polizas() -> int:
    selected_value = -1
    is_input_right = False
    while not is_input_right:
        print('[==== Seleccione alguna de las opciones de pólizas ====]\n')
        print('\t1. Vehícular\n\t2. Inmueble\n\t3. Adicional\n\t4. Cancelar\n')
        response = input('> ')

        if response >= '1' and response <= '4':
            selected_value = int(response)
            is_input_right = True
            continue

        print('\n¡Lo siento, el valor dado es inválido!\n')

    return selected_value


def is_number(value: str) -> bool:
    is_float = re.compile(r'^[0-9]*.[0-9]*$').match(value)
    is_integer = re.compile(r'^[0-9]*$').match(value)
    return is_float or is_integer


def obtener_precio() -> float:
    price = 0.0
    is_valid_price = False
    while not is_valid_price:
        response = input('\tIngrese el costo: ')
        if is_number(response):
            price = float(response)
            is_valid_price = True
            continue

        print('¡Lo siento, el valor no es númerico, intentalo otra vez!\n')

    return price


def obtener_vencimiento() -> datetime:
    fecha_vencimiento = datetime.now()
    is_valid_date = False
    while not is_valid_date:
        response = input('\tIngrese la cantidad de meses de válidez: ')
        if str.isdigit(response):
            meses = int(response)
            if meses < 1:
                continue
            fecha_vencimiento += timedelta(days=meses * 30)
            is_valid_date = True
            continue

        print('¡Lo siento, el valor dado no es válido o es menor a un mes!\n')

    return fecha_vencimiento


def obtener_area() -> float:
    area = 0.0
    is_area_valid = False
    while not is_area_valid:
        response = input('\tIngresa el área: ')
        if is_number(response):
            area = float(response)
            is_area_valid = True
            continue

        print('¡Lo siento, el valor dado no es númerico!\n')

    return area


def agregar_poliza_vehicular():
    print('[==== Ingrese los detalles de la póliza vehícular ====\n]')
    titular = input('\tIngrese el nombre del titular: ')
    costo = obtener_precio()
    fecha_vencimiento = obtener_vencimiento()
    marca = input('\tIngrese la marca del vehículo: ')
    modelo = input('\tIngrese el modelo del vehículo: ')

    poliza = Vehicular(
        titular=titular,
        costo=costo,
        fecha_final=fecha_vencimiento,
        marca=marca,
        modelo=modelo,
        num_poliza=len(polizas) + 1)

    polizas.append(poliza)


def agregar_poliza_inmueble():
    print('[==== Ingrese los detalles del inmueble ====]\n')
    titular = input('\tIngrese el nombre del titular: ')
    costo = obtener_precio()
    area = obtener_area()
    fecha_vencimiento = obtener_vencimiento
    direccion = input('\tIngrese la dirección del inmbueble: ')

    poliza = Inmueble(
        titular=titular,
        costo=costo,
        area=area,
        fecha_final=fecha_vencimiento,
        num_poliza=len(polizas) + 1
    )

    polizas.append(poliza)


def agregar_poliza_adicional():
    print('[==== Ingrese los detalles de esta póliza ====]')
    titular = input('\tIngrese el nombre del titular: ')
    titulo = input('\tIngrese el título de esta póliza: ')
    descripcion = input('\tIngrese la descripción de está póliza: \n>')
    costo = obtener_precio()
    fecha_vencimiento = obtener_vencimiento()

    poliza = Adicional(
        titular=titular,
        titulo=titulo,
        descripcion=descripcion,
        costo=costo,
        fecha_final=fecha_vencimiento,
        num_poliza=len(polizas) + 1
    )

    polizas.append(poliza)


while running:
    option = mostrar_menu()
    if option == 1:
        opcion_poliza = mostrar_menu_polizas()

        match opcion_poliza:
            case 1:
                agregar_poliza_vehicular()
            case 2:
                agregar_poliza_inmueble()
            case 3:
                agregar_poliza_adicional()
            case 4:
                print('Cancelando...')

    elif option == 4:
        print('Saliendo...')
        running = False
