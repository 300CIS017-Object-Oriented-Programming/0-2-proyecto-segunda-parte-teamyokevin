import sys
import os

# Añadir rutas al sys.path. Nota: Esto no es una práctica recomendada en producción.
sys.path.append(r'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/modelos')

import streamlit as st

def asistencia(controller):
    """
    Muestra el panel de asistencia en la aplicación de Streamlit.

    Parameters:
    controller (GUIController): El controlador que maneja el estado de la aplicación.
    """
    st.title("Panel de Asistencia")

    if st.button("Volver a la página principal"):
        st.session_state['page'] = 'main'

    nombres_eventos = [evento.nombre for evento in controller.eventos_lista]
    if not nombres_eventos:
        st.error("No hay eventos disponibles.")
        return

    st.write("Seleccione el evento al que va a asistir")
    evento_seleccionado = st.selectbox("Seleccione un evento", [''] + nombres_eventos)

    # Filtrar la lista de compradores para que solo se muestren los compradores que aún no han confirmado su asistencia y que tienen boletos para el evento seleccionado
    nombres_compradores = [
        current_comprador.nombre for current_comprador in controller.compradores_list
        if current_comprador not in controller.lista_confirmadas and current_comprador.evento == evento_seleccionado
    ]

    if nombres_compradores:
        st.write("Seleccione el comprador")
        comprador_seleccionado = st.selectbox("Seleccione un comprador", [''] + nombres_compradores)

        if st.button("Confirmar asistencia"):
            for current_comprador in controller.compradores_list:
                if current_comprador.nombre == comprador_seleccionado:
                    controller.lista_confirmadas.append(current_comprador)
                    st.success(f"Asistencia confirmada para {current_comprador.nombre}")
                    break
            else:
                st.error("El comprador seleccionado no existe o ya ha confirmado su asistencia.")

    st.subheader(f"Lista de asistencia confirmada para el evento {evento_seleccionado}")
    for confirmado in controller.lista_confirmadas:
        if confirmado.evento == evento_seleccionado:
            st.write(confirmado.nombre)
