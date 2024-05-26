import sys
import os

# Añadir rutas al sys.path al principio del archivo. No recomendado en producción, pero útil para scripts locales.
sys.path.append(r'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/view')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/modelos')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/utils')

# Importación de bibliotecas estándar y locales
import streamlit as st
from view.admin_view import mostrar_pagina_administrador
from view.compraventa_view import mostrar_compraventa
from view.asistencia_view import asistencia
from view.reportes_view import mostrar_pagina_reportes
from modelos.evento_b import EventoBar, EventoTeatro, EventoFilantropico
from utils.pdf_generator import generar_pdf
from modelos.boleteria_b import comprador

class GUIController:
    """
    Controlador de la GUI que maneja el estado de la aplicación y las operaciones principales.

    Atributos:
    precios_boleta_lista (list): Lista de precios de boletas.
    eventos_lista (list): Lista de eventos.
    compradores_list (list): Lista de compradores.
    lista_confirmadas (list): Lista de asistentes confirmados.
    patrocinadores_list (list): Lista de patrocinadores.
    """

    def __init__(self):
        """
        Inicializa el controlador de la GUI y el estado de la sesión.
        """
        if 'my_state' not in st.session_state:
            self.precios_boleta_lista = []
            self.eventos_lista = []
            self.compradores_list = []
            self.lista_confirmadas = []
            self.patrocinadores_list = []

            st.session_state['my_state'] = self
            st.session_state['page'] = 'main'
        else:
            self.precios_boleta_lista = st.session_state.my_state.precios_boleta_lista
            self.eventos_lista = st.session_state.my_state.eventos_lista
            self.compradores_list = st.session_state.my_state.compradores_list
            self.lista_confirmadas = st.session_state.my_state.lista_confirmadas

    def calcular_ingresos(self):
        """
        Calcula los ingresos por tipo de evento (Bar, Teatro, Filantrópico).

        Returns:
        dict: Ingresos por tipo de evento.
        """
        ingresos = {
            "Bar": 0,
            "Teatro": 0,
            "Filantropico": 0
        }

        for evento in self.eventos_lista:
            if isinstance(evento, EventoBar):
                for comprador in self.compradores_list:
                    if comprador.evento == evento.nombre:
                        total_ingreso = comprador.total_compra
                        ingreso_bar = total_ingreso * 0.20
                        ingresos["Bar"] += ingreso_bar
            elif isinstance(evento, EventoTeatro):
                for comprador in self.compradores_list:
                    if comprador.evento == evento.nombre:
                        total_ingreso = comprador.total_compra
                        retencion_tiquetera = total_ingreso * 0.07
                        ingreso_evento = total_ingreso - retencion_tiquetera - evento.valor_alquiler
                        ingresos["Teatro"] += ingreso_evento
            elif isinstance(evento, EventoFilantropico):
                ingresos["Filantropico"] += sum(evento.patrocinadores_valor_aportado)

        return ingresos

    def generar_pdf(self, comprador):
        """
        Genera un archivo PDF con la información del comprador.

        Parameters:
        comprador (Comprador): El objeto Comprador que contiene los datos del comprador.
        """
        generar_pdf(comprador)

    def main(self):
        """
        Función principal que controla la navegación y la lógica de la aplicación.
        """
        try:
            if 'page' not in st.session_state:
                st.session_state['page'] = 'main'

            st.sidebar.title("Navegación")
            if st.sidebar.button("Ir a la página principal"):
                st.session_state['page'] = 'main'
            if st.sidebar.button("Ir a la página de administrador"):
                st.session_state['page'] = 'admin'
            if st.sidebar.button("Ir a la página de compraventa"):
                st.session_state['page'] = 'compraventa'
            if st.sidebar.button("Ir a la página de asistencia"):
                st.session_state['page'] = 'asistencia'
            if st.sidebar.button("Ir a la página de reportes"):
                st.session_state['page'] = 'reportes'

            if st.session_state['page'] == 'admin':
                mostrar_pagina_administrador(self)
            elif st.session_state['page'] == 'compraventa':
                mostrar_compraventa(self)
            elif st.session_state['page'] == 'asistencia':
                asistencia(self)
            elif st.session_state['page'] == 'reportes':
                mostrar_pagina_reportes(self)
        except Exception as e:
            st.error(f"Se produjo un error: {e}")


# Fin del código


