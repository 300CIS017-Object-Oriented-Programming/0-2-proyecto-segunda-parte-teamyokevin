import sys
import os

# Añadir rutas al sys.path. Nota: Esto no es una práctica recomendada en producción.
sys.path.append(r'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/utils')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/modelos')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/controlador')

import streamlit as st
from modelos.boleteria_b import comprador
from utils.pdf_generator import generar_pdf
from modelos.evento_b import EventoBar, EventoTeatro, EventoFilantropico

def calcular_ingresos(controller):
    """
    Calcula los ingresos por tipo de evento.

    Parameters:
    controller (GUIController): El controlador que maneja el estado de la aplicación.

    Returns:
    dict: Un diccionario con los ingresos por tipo de evento.
    """
    ingresos = {
        "Bar": 0,
        "Teatro": 0,
        "Filantropico": 0
    }

    # Recorre la lista de eventos para calcular los ingresos según el tipo de evento
    for evento in controller.eventos_lista:
        if isinstance(evento, EventoBar):
            ingresos["Bar"] = 0  # Restablecer los ingresos a 0 para este tipo de evento
            for comprador1 in controller.compradores_list:
                if comprador1.evento == evento.nombre:
                    total_ingreso = comprador1.total_compra
                    ingreso_bar = total_ingreso * 0.20
                    ingreso_artista = total_ingreso * 0.80
                    ingresos["Bar"] += ingreso_bar
        elif isinstance(evento, EventoTeatro):
            ingresos["Teatro"] = 0  # Restablecer los ingresos a 0 para este tipo de evento
            for comprador2 in controller.compradores_list:
                if comprador2.evento == evento.nombre:
                    total_ingreso = comprador2.total_compra
                    retencion_tiquetera = total_ingreso * 0.07
                    ingreso_evento = total_ingreso - retencion_tiquetera - evento.valor_alquiler
                    ingresos["Teatro"] += ingreso_evento
        elif isinstance(evento, EventoFilantropico):
            ingresos["Filantropico"] = 0  # Restablecer los ingresos a 0 para este tipo de evento
            ingresos["Filantropico"] += sum(evento.patrocinadores_valor_aportado)

    return ingresos

def mostrar_compraventa(controller):
    """
    Muestra el panel de compra y venta en la aplicación de Streamlit.

    Parameters:
    controller (GUIController): El controlador que maneja el estado de la aplicación.
    """
    st.title("Panel de Compra y Venta")

    if st.button("Volver a la página principal"):
        st.session_state['page'] = 'main'

    nombres_eventos = [evento.nombre for evento in controller.eventos_lista]

    boleta_comprada = None
    st.subheader("Ingrese sus datos por favor")
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")
    edad = st.number_input("Edad")
    correo = st.text_input("Correo")
    telefono = st.text_input("Telefono")
    direccion = st.text_input("Dirección")
    tipo_pago = st.selectbox("Tipo de pago", ["Efectivo", "Tarjeta de crédito", "Tarjeta débito", "Transferencia bancaria"])
    numero_boletas_compradas = st.number_input("Número de boletas", min_value=1)

    evento_seleccionado = st.selectbox("Seleccione un evento", [''] + nombres_eventos)

    # Muestra detalles del evento seleccionado y permite la selección de boletas
    for evento in controller.eventos_lista:
        if evento.nombre == evento_seleccionado:
            st.write(f"Nombre del evento: {evento.nombre}")
            st.write(f"Fecha del evento: {evento.fecha}")
            st.write(f"Hora de apertura: {evento.hora_apertura}")
            st.write(f"Hora del evento: {evento.hora_show}")
            st.write(f"Lugar del evento: {evento.lugar}")
            st.write(f"Dirección del evento: {evento.direccion}")
            st.write(f"Ciudad del evento: {evento.ciudad}")
            st.write(f"Aforo total: {evento.aforo_total}")
            st.write(f"Artistas: {', '.join(evento.artistas)}")
            st.write("Boletas disponibles:")
            categorias_boletas = [f'{boleta.categoria} - {boleta.fase_venta}' for boleta in evento.precio_boleta]

            boleta_seleccionada = st.selectbox("Seleccione una boleta", [''] + categorias_boletas)

            # Calcula el total de la compra según la boleta seleccionada
            for boleta in evento.precio_boleta:
                if f'{boleta.categoria} - {boleta.fase_venta}' == boleta_seleccionada:
                    total_compra = boleta.precio * numero_boletas_compradas
                    st.write(f"Total de la compra: {total_compra}")
                    boleta_comprada = boleta_seleccionada
            st.write("-------------------------------------------------")

    # Procesa la compra de boletas y genera el PDF del recibo
    if st.button("Comprar boletas"):
        comprador_actual = comprador(
            nombre, apellido, edad, correo, telefono, direccion, boleta_comprada,
            numero_boletas_compradas, total_compra, evento_seleccionado, tipo_pago
        )
        comprador_actual.evento = evento_seleccionado
        controller.compradores_list.append(comprador_actual)
        st.success("Boletas compradas exitosamente")
        controller.generar_pdf(comprador_actual)
        st.write(comprador_actual.tipo_pago)

    st.subheader("Ingresos por tipo de evento")
    ingresos = calcular_ingresos(controller)
    st.write(f"Ingresos por eventos en Bar: {ingresos['Bar']}")
    st.write(f"Ingresos por eventos en Teatro: {ingresos['Teatro']}")
    st.write(f"Ingresos por eventos Filantrópicos: {ingresos['Filantropico']}")

