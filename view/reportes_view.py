import sys
import os

# Añadir rutas al sys.path. Nota: Esto no es una práctica recomendada en producción.
sys.path.append(r'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/controlador')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/modelos')

import streamlit as st
import pandas as pd
import plotly.express as px
from compraventa_view import calcular_ingresos
import io
from modelos.evento_b import EventoBar, EventoTeatro, EventoFilantropico
from modelos.boleteria_b import comprador
import admin_view
import compraventa_view
import asistencia_view

def mostrar_pagina_reportes(controller):
    """
    Muestra la página de generación de reportes en la aplicación de Streamlit.

    Parameters:
    controller (GUIController): El controlador que maneja el estado de la aplicación.
    """
    st.title("Generar Reportes")

    if st.button("Volver a la página principal"):
        st.session_state['page'] = 'main'

    st.subheader("Reporte de Ventas de Boletas")
    reportes_ventas_boletas(controller)

    st.subheader("Reporte Financiero")
    st.write(comprador.tipo_pago)
    reportes_financieros(controller)
    st.write(comprador.tipo_pago)

    st.subheader("Reporte de Datos de los Compradores")
    reportes_datos_compradores(controller)

    st.subheader("Reporte de Datos por Artista")
    reportes_datos_por_artista(controller)

def reportes_ventas_boletas(controller):
    """
    Genera y muestra el reporte de ventas de boletas.

    Parameters:
    controller (GUIController): El controlador que maneja el estado de la aplicación.
    """
    boletas_vendidas = []
    for evento in controller.eventos_lista:
        for comprador in controller.compradores_list:
            if comprador.evento == evento.nombre:
                for boleta in evento.precio_boleta:
                    boletas_vendidas.append({
                        'Evento': evento.nombre,
                        'Categoría': boleta.categoria,
                        'Fase de venta': boleta.fase_venta,
                        'Precio': boleta.precio,
                        'Total Compra': comprador.total_compra
                    })

    df_boletas_vendidas = pd.DataFrame(boletas_vendidas)
    st.write(df_boletas_vendidas)

def reportes_financieros(controller):
    """
    Genera y muestra el reporte financiero desglosado por tipo de pago y tipo de boleta.

    Parameters:
    controller (GUIController): El controlador que maneja el estado de la aplicación.
    """
    ingresos_por_tipo_pago = {'Efectivo': 0, 'Tarjeta de crédito': 0, 'Tarjeta débito': 0, 'Transferencia bancaria': 0}
    ingresos_por_tipo_boleta = {}

    for comprador in controller.compradores_list:
        # Sumar al total de ingresos por tipo de pago
        ingresos_por_tipo_pago[comprador.tipo_pago] += comprador.total_compra

        # Sumar al total de ingresos por tipo de boleta
        if comprador.boletas not in ingresos_por_tipo_boleta:
            ingresos_por_tipo_boleta[comprador.boletas] = 0
        ingresos_por_tipo_boleta[comprador.boletas] += comprador.total_compra

    # Mostrar los ingresos por tipo de pago
    for tipo_pago, ingresos in ingresos_por_tipo_pago.items():
        st.write(f"Ingresos por {tipo_pago}: {ingresos}")

    # Mostrar los ingresos por tipo de boleta
    for tipo_boleta, ingresos in ingresos_por_tipo_boleta.items():
        st.write(f"Ingresos por boletas {tipo_boleta}: {ingresos}")

def reportes_datos_compradores(controller):
    """
    Genera y muestra el reporte detallado de los compradores.

    Parameters:
    controller (GUIController): El controlador que maneja el estado de la aplicación.
    """
    compradores_data = []
    for comprador in controller.compradores_list:
        compradores_data.append({
            'Nombre': comprador.nombre,
            'Apellido': comprador.apellido,
            'Edad': comprador.edad,
            'Correo': comprador.correo,
            'Teléfono': comprador.telefono,
            'Dirección': comprador.direccion,
            'Tipo de Pago': comprador.tipo_pago,
            'Evento': comprador.evento,
            'Boleta': comprador.boletas,
            'Número de boletas compradas': comprador.numero_boletas_compradas,
            'Total Compra': comprador.total_compra
        })

    df_compradores = pd.DataFrame(compradores_data)
    st.write(df_compradores)

    # Análisis demográfico y comportamiento
    st.plotly_chart(px.histogram(df_compradores, x="Edad", title="Distribución de Edad de Compradores"))
    st.plotly_chart(px.histogram(df_compradores, x="Evento", title="Número de Compradores por Evento"))

    # Convertir DataFrame a BytesIO para la descarga
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df_compradores.to_excel(writer, index=False)

    output.seek(0)  # Ir al inicio del stream

    st.download_button(
        label="Descargar datos de compradores en Excel",
        data=output,
        file_name='datos_compradores.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

def reportes_datos_por_artista(controller):
    """
    Genera y muestra el reporte de datos por artista.

    Parameters:
    controller (GUIController): El controlador que maneja el estado de la aplicación.
    """
    # Obtener la lista de todos los artistas
    artistas = [artista for evento in controller.eventos_lista for artista in evento.artistas]
    artista_seleccionado = st.selectbox("Seleccione un artista", list(set(artistas)))

    # Filtrar eventos del artista seleccionado
    eventos_artista = []
    for evento in controller.eventos_lista:
        if artista_seleccionado in evento.artistas:
            eventos_artista.append({
                'Nombre del evento': evento.nombre,
                'Fecha': evento.fecha,
                'Lugar': evento.lugar,
                'Cantidad de boletas vendidas': sum([comprador.numero_boletas_compradas for comprador in controller.compradores_list if comprador.evento == evento.nombre]),
                'Porcentaje de aforo cubierto': (sum([comprador.numero_boletas_compradas for comprador in controller.compradores_list if comprador.evento == evento.nombre]) / int(evento.aforo_total)) * 100
            })

    df_eventos_artista = pd.DataFrame(eventos_artista)
    st.write(df_eventos_artista)
