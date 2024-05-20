import sys
import os

# PEP8: Añadir rutas al sys.path debería estar al principio del archivo, aunque en un entorno real esto no es una práctica recomendada.
sys.path.append(r'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/2/pythonProject')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/2/pythonProject/view')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/2/pythonProject/modelos')

# Importación de bibliotecas estándar y locales
import streamlit as st
import bcrypt
from modelos.boleteria_b import PrecioBoleta, comprador
from modelos.evento_b import Evento, GestorEventos, EventoBar, EventoTeatro, EventoFilantropico
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# PEP8: Nombres de clases en CamelCase
class GUIController:
    def __init__(self):
        # Inicialización del estado de la aplicación.
        if 'my_state' not in st.session_state:
            self.precios_boleta_lista = []
            self.eventos_lista = []
            self.compradores_list = []
            self.lista_confirmadas = []
            self.patrocinadores_list = []
            st.session_state['my_state'] = self
            st.session_state['page'] = 'main'  # Agregar el estado de la página a st.session_state
        else:
            self.precios_boleta_lista = st.session_state.my_state.precios_boleta_lista
            self.eventos_lista = st.session_state.my_state.eventos_lista
            self.compradores_list = st.session_state.my_state.compradores_list
            self.lista_confirmadas = st.session_state.my_state.lista_confirmadas

    # PEP8: Nombres de funciones en snake_case
    def generar_pdf(self, comprador):
        # Genera un archivo PDF con la información del comprador.
        c = canvas.Canvas("comprador.pdf", pagesize=letter)

        # Datos del comprador
        c.drawString(100, 750, f"Nombre: {comprador.nombre}")
        c.drawString(100, 735, f"Apellido: {comprador.apellido}")
        c.drawString(100, 720, f"Edad: {comprador.edad}")
        c.drawString(100, 705, f"Correo: {comprador.correo}")
        c.drawString(100, 690, f"Telefono: {comprador.telefono}")
        c.drawString(100, 675, f"Dirección: {comprador.direccion}")
        c.drawString(100, 660, f"Boletas: {comprador.boletas}")
        c.drawString(100, 645, f"Número de boletas compradas: {comprador.numero_boletas_compradas}")
        c.drawString(100, 630, f"Total de la compra: {comprador.total_compra}")

        # Recomendaciones para el evento
        c.drawString(100, 600, "Recomendaciones para el evento:")
        c.drawString(100, 585, "1. Llega temprano para evitar filas.")
        c.drawString(100, 570, "2. No olvides tu boleta y tu identificación.")
        c.drawString(100, 555, "3. Sigue las indicaciones de seguridad del lugar.")
        c.drawString(100, 540, "4. Disfruta del evento!")

        c.save()

    def mostrar_pagina_administrador(self):
        """Página para administradores."""
        st.title("Panel de Administrador")

        if st.button("Volver a la página principal"):
            st.session_state['page'] = 'main'

        # Formulario para agregar un evento
        st.subheader("Agregar un nuevo evento")
        tipo_evento = st.selectbox("Tipo de evento", ["EventoBar", "EventoTeatro", "EventoFilantropico"])
        nombre_evento = st.text_input("Nombre del evento")
        fecha = st.date_input("Fecha del evento")
        hora_apertura = st.time_input("Hora de apertura de puertas")
        hora_evento = st.time_input("Hora del evento")
        lugar = st.text_input("Lugar del evento")
        direccion = st.text_input("Dirección del evento")
        ciudad = st.text_input("Ciudad del evento")
        estado_evento = st.selectbox("Estado del evento", ["Por realizar", "Realizado", "Cancelado", "Aplazado", "Cerrado"])
        aforo_total = st.text_input("Aforo del evento")
        artistas = st.text_input("Artistas (separados por comas)")

        # Campos específicos de cada tipo de evento
        valor_alquiler = None
        patrocinadores = None
        if tipo_evento == "EventoTeatro":
            valor_alquiler = st.number_input("Valor de alquiler")
        elif tipo_evento == "EventoFilantropico":
            patrocinadores = st.text_input("Patrocinadores (separados por comas)")


        # Campos de entrada para PrecioBoleta
        st.subheader("Agregar Tipos de boleta")
        categoria = st.selectbox("Categoria de la boleta", ["VIP", "Intermedio", "General"])
        fase_venta = st.selectbox("Fase de venta", ["Preventa Exclusiva", "Venta General", "Venta de última hora"])
        precio = st.number_input("Precio de la boleta")
        descuento = st.number_input("Descuento de la boleta")

        if st.button("Agregar boleta"):
            # Añade un tipo de boleta a la lista de precios
            precio_boleta = PrecioBoleta(categoria, fase_venta, precio, descuento)
            self.precios_boleta_lista.append(precio_boleta)
            st.session_state.my_state.precios_boleta_lista = self.precios_boleta_lista
            st.success("Boleta agregada exitosamente")

        if st.button("Agregar evento"):
            # Añade un evento a la lista de eventos según el tipo seleccionado
            lista_artistas = artistas.split(",")
            if tipo_evento == "EventoBar":
                nuevo_evento = EventoBar(nombre_evento, fecha, hora_apertura, hora_evento, lugar, direccion, ciudad,
                                         estado_evento, aforo_total, self.precios_boleta_lista, lista_artistas)
            elif tipo_evento == "EventoTeatro":
                nuevo_evento = EventoTeatro(nombre_evento, fecha, hora_apertura, hora_evento, lugar, direccion, ciudad,
                                            estado_evento, aforo_total, self.precios_boleta_lista, lista_artistas,
                                            valor_alquiler)
            elif tipo_evento == "EventoFilantropico":
                lista_patrocinadores = patrocinadores.split(",")
                nuevo_evento = EventoFilantropico(nombre_evento, fecha, hora_apertura, hora_evento, lugar, direccion,
                                                  ciudad, estado_evento, aforo_total, self.precios_boleta_lista,
                                                  lista_artistas, lista_patrocinadores)

            self.eventos_lista.append(nuevo_evento)
            st.session_state.my_state.eventos_lista = self.eventos_lista
            st.success("Evento agregado exitosamente")

            # Reiniciar la lista de boletas
            self.precios_boleta_lista = []
            st.session_state.my_state.precios_boleta_lista = self.precios_boleta_lista

        # Mostrar todos los eventos
        st.subheader("Eventos actuales")
        for evento in self.eventos_lista:
            st.write(f"Nombre del evento: {evento.nombre}")
            st.write(f"Fecha del evento: {evento.fecha}")
            st.write(f"Hora de apertura: {evento.hora_apertura}")
            st.write(f"Hora del evento: {evento.hora_show}")
            st.write(f"Lugar del evento: {evento.lugar}")
            st.write(f"Dirección del evento: {evento.direccion}")
            st.write(f"Ciudad del evento: {evento.ciudad}")
            st.write(f"Estado del evento: {evento.estado}")
            st.write(f"Aforo total: {evento.aforo_total}")
            st.write(f"Artistas: {', '.join(evento.artistas)}")
            st.write(f"Boletas actuales: {evento.precio_boleta}")
            if isinstance(evento, EventoTeatro):
                st.write(f"Valor de alquiler: {evento.valor_alquiler}")
            if isinstance(evento, EventoFilantropico):
                st.write(f"Patrocinadores: {', '.join(evento.patrocinadores)}")
            for boleta in evento.precio_boleta:
                st.write(f"Boleta: {boleta.categoria}, Fase de venta: {boleta.fase_venta}, Precio: {boleta.precio}")
            st.write("-------------------------------------------------")
        st.write(f"Boletas actuales: {self.precios_boleta_lista}")

    def mostrar_compraventa(self):
        """Página de compra y venta de boletas."""
        st.title("Panel de Compra y Venta")

        if st.button("Volver a la página principal"):
            st.session_state['page'] = 'main'

        # Crear una lista con los nombres de todos los eventos
        nombres_eventos = [evento.nombre for evento in self.eventos_lista]

        boleta_comprada = None
        st.subheader("Ingrese sus datos por favor")
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        edad = st.number_input("Edad")
        correo = st.text_input("Correo")
        telefono = st.text_input("Telefono")
        direccion = st.text_input("Dirección")
        numero_boletas_compradas = st.number_input("Número de boletas", min_value=1)

        # Crear una lista desplegable con los nombres de los eventos
        evento_seleccionado = st.selectbox("Seleccione un evento", [''] + nombres_eventos)

        for evento in self.eventos_lista:
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
                st.write(f"Boletas disponibles:")
                categorias_boletas = [boleta.categoria for boleta in evento.precio_boleta]

                # Crear una lista desplegable con las categorías de las boletas
                boleta_seleccionada = st.selectbox("Seleccione una boleta", [''] + categorias_boletas)

                # Buscar la boleta seleccionada y calcular el total de la compra
                for boleta in evento.precio_boleta:
                    if boleta.categoria == boleta_seleccionada:
                        total_compra = boleta.precio * numero_boletas_compradas
                        st.write(f"Total de la compra: {total_compra}")
                        boleta_comprada = boleta_seleccionada  # Almacenar el tipo de boleta seleccionada en una variable
                st.write("-------------------------------------------------")

        if st.button("Comprar boletas"):
            # Añadir el comprador a la lista de compradores y generar PDF con la información
            comprador_actual = comprador(nombre, apellido, edad, correo, telefono, direccion, boleta_comprada,
                                         numero_boletas_compradas, total_compra)
            self.compradores_list.append(comprador_actual)
            st.success("Boletas compradas exitosamente")
            self.generar_pdf(comprador_actual)

    def asistencia(self):
        """Página para la gestión de asistencia."""
        st.title("Panel de Asistencia")

        if st.button("Volver a la página principal"):
            st.session_state['page'] = 'main'

        # Crear una lista con los nombres de todos los eventos
        nombres_eventos = [evento.nombre for evento in self.eventos_lista]
        if not nombres_eventos:
            st.error("No hay eventos disponibles.")
            return

        st.write("Seleccione el evento al que va a asistir")
        evento_seleccionado = st.selectbox("Seleccione un evento", [''] + nombres_eventos)

        # Crear una lista con los nombres de todos los compradores
        nombres_compradores = [current_comprador.nombre for current_comprador in self.compradores_list]
        if not nombres_compradores:
            st.error("No hay compradores disponibles.")
            return

        st.write("Seleccione el comprador")
        comprador_seleccionado = st.selectbox("Seleccione un comprador", [''] + nombres_compradores)

        if st.button("Confirmar asistencia"):
            for current_comprador in self.compradores_list:
                if current_comprador.nombre == comprador_seleccionado:
                    self.lista_confirmadas.append(current_comprador)
                    st.success(f"Asistencia confirmada para {current_comprador.nombre}")
                    break
            else:
                st.error("El comprador seleccionado no existe.")

        # Mostrar la lista de personas confirmadas
        st.subheader("Lista de asistencia confirmada")
        for confirmado in self.lista_confirmadas:
            st.write(confirmado.nombre)

    def main(self):
        """Función principal."""
        try:
            if 'page' not in st.session_state:
                st.session_state['page'] = 'main'

            # Botones para navegar entre las diferentes páginas
            if st.button("Ir a la página de administrador"):
                st.session_state['page'] = 'admin'
            if st.button("Ir a la página de compraventa"):
                st.session_state['page'] = 'compraventa'
            if st.button("Ir a la página de asistencia"):
                st.session_state['page'] = 'asistencia'

            # Mostrar la página correspondiente según el estado
            if st.session_state['page'] == 'admin':
                self.mostrar_pagina_administrador()
            elif st.session_state['page'] == 'compraventa':
                self.mostrar_compraventa()
            elif st.session_state['page'] == 'asistencia':
                self.asistencia()
        except Exception as e:
            # Manejo de errores
            st.error(f"Se produjo un error: {e}")

# Fin del código


#Faltan calculos de ingresos por tipo de evento