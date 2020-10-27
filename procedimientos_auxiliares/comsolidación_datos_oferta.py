from typing import List

from aux_class import FullElementosOferta


def consolidar_datos(datos: List[FullElementosOferta]):
    """
    Este procedimiento recibe una lista compuesta de las diversas entradas del fichero de oferta. Consolida los
    elementos repetidos, entregando así una lista consolidada de menor longitud
    :param datos: Lista de entradas de la oferta
    :return: Lista consolidada de entradas
    """

    lista_consolidada = [datos[0]]  # Lista de elementos ya consolidados

    for i in range(1, len(datos)):
        item = datos[i]

        encontrado = False  # Parámetro auxiliar
        for item_consolidado in lista_consolidada:  # Comprobamos si la entrada ya estaba en lista_consolidada
            if ((item.manufacturer == item_consolidado.manufacturer) and (item.code == item_consolidado.code) and
                    (item.init_date == item_consolidado.init_date) and (item.end_date == item_consolidado.end_date) and
                    (item.uptime == item_consolidado.uptime)):
                item_consolidado.qty += item.qty
                item_consolidado.serial_no += (', ' + item.serial_no)
                encontrado = True
                break

        if not encontrado:  # Si no está, lo añadimos
            lista_consolidada.append(item)

    return lista_consolidada
