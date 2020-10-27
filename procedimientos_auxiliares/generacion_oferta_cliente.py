# Este fichero contiene sólo procedimientos para hacer la oferta de cliente. Nuevo en V4

import openpyxl
from typing import List
from aux_class import ElementosOferta, DatosGenerales, FullElementosOferta
import os
from os.path import dirname
from datetime import datetime


def generar_oferta_cliente(datos_clases: List[FullElementosOferta], datos_generales, instance):
    """
    Esta rutina nos genera un oferta Excel entregable al cliente. Para ello se parte de la listas de los
    de los ítems de la quote. Se consolidan aquellos artículos en los que se
    produce coincidencia de fabricante, código y fechas de principio y fin del servicio
    :param datos_clases: Lista de entradas consolidadas de la oferta
    :param datos_generales: Nombre de la oferta, del cliente, BID y AM
    :param instance:
    :return: Fichero oferta_cliente.xlsx de oferta
    """

    lista_articulos_oferta = []

    for element in datos_clases:
        pvp_total = element.qty * element.total_unit_price
        item = ElementosOferta(element.in_csv, element.manufacturer, element.code, element.qty, element.init_date,
                               element.end_date, element.uptime, pvp_total)
        lista_articulos_oferta.append(item)

    lista_articulos_oferta.sort(key=lambda x: x.manufacturer)
    book = hacer_libro_de_oferta_de_cliente(lista_articulos_oferta, datos_generales)
    book.close()
    return book


def hacer_libro_de_oferta_de_cliente(lista_elementos, datos_generales: DatosGenerales):
    # Comenzamos definiendo los parámetros de filas y columnas de la plantilla de oferta
    FIRST_ROW = 22
    fabricante = 'B'
    equipo = 'F'
    unid = 'N'
    servicio = 'P'
    fecha_inicio = 'AC'
    fecha_fin = 'AH'
    importe = 'AM'
    precio_total_oferta = 'AM51'

    quote_name = 'L6'
    cliente = 'L7'
    bid = 'L8'
    version = 'R9'
    am = 'T11'
    propuesta = 'B18'
    fecha = 'AM56'
    base_dir = dirname(os.path.abspath(os.path.dirname(__file__)))
    template_file = os.path.join(base_dir + '/template_oferta_cliente.xlsx')

    total = 0

    # Abrimos el libro y lo rellenamos con los datos de las lista recibidas
    try:
        book = openpyxl.load_workbook(template_file, data_only=False)
        sheet = book.get_sheet_by_name('OFERTA CLIENTE')

        for i in range(len(lista_elementos)):
            row = str(FIRST_ROW + i)
            sheet[fabricante + row] = lista_elementos[i].manufacturer  # Escribimos el fabricante
            sheet[equipo + row] = lista_elementos[i].code  # Código de equipo
            sheet[unid + row] = lista_elementos[i].qty  # Cantidad
            sheet[servicio + row] = lista_elementos[i].uptime  # Servicio Uptime
            sheet[fecha_inicio + row] = lista_elementos[i].init_date  # Fecha de inicio del servicio
            sheet[fecha_fin + row] = lista_elementos[i].end_date  # Fecha de final
            sheet[importe + row] = lista_elementos[i].total_price  # Precio total
            total += lista_elementos[i].total_price

        sheet[precio_total_oferta] = total

        # Ahora ponemos los datos generales de la oferta
        sheet[quote_name] = datos_generales.nombre_oferta
        sheet[cliente] = datos_generales.cliente
        sheet[bid] = datos_generales.bid
        sheet[version] = datos_generales.version
        sheet[am] = datos_generales.am.value
        sheet[propuesta] = datos_generales.nombre_oferta
        hoy = datetime.today()
        sheet[fecha] = hoy
        book.close()
        return book

    except Exception as e:
        print('Excepción:' + e.__repr__())
        return None


def obtener_datos_generales(hoja_resumen):
    quote_name = hoja_resumen['C6'].value
    customer = hoja_resumen['C7'].value
    bid = hoja_resumen['C8'].value
    version = hoja_resumen['E9'].value
    am = hoja_resumen['E11']

    datos = DatosGenerales(nombre_oferta=quote_name, cliente=customer, bid=bid, version=version, am=am)
    return datos
