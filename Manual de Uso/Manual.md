# Manual de Uso

## Descripción

Este proyecto es una aplicación de gestión de eventos que permite a los administradores agregar nuevos eventos, definir tipos de boletas y ver detalles de eventos existentes.

## Requisitos

- **Python 3.x**
- **Streamlit**: `pip install streamlit`
- **Dependencias del Proyecto**: Asegúrate de que las rutas del sistema apuntan correctamente a los directorios de tus módulos y modelos.

## Instalación

1. **Clona el repositorio o descarga los archivos necesarios**:
   ```sh
   git clone https://github.com/usuario/proyecto.git
   cd proyecto
   pip install -r requirements.txt

## Uso

1. **Ejecutar la Aplicación**:

    streamlit run main.py

## Funciones

1. **Mostrar la Página del Administrador**:

    La función mostrar_pagina_administrador(controller) se encarga de renderizar la página del panel de administrador. Aquí se describe cómo usarla:

    -Función Principal:

    def mostrar_pagina_administrador(controller):
        st.title("Panel de Administrador")

        if st.button("Volver a la página principal"):
            st.session_state['page'] = 'main'

    1.1 **Agregar Nuevo Evento**:
        -La sección para agregar un nuevo evento permite al administrador especificar el tipo de evento y sus detalles:

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

    1.2 **Agregar Boletas**:
        -Define los detalles de las boletas disponibles para el evento:

            st.subheader("Agregar Tipos de boleta")
            categoria = st.selectbox("Categoria de la boleta", ["VIP", "Intermedio", "General"])
            fase_venta = st.selectbox("Fase de venta", ["Preventa Exclusiva", "Venta General", "Venta de última hora"])
            precio = st.number_input("Precio de la boleta")
            descuento = st.number_input("Descuento de la boleta")

            if st.button("Agregar boleta"):
                precio_boleta = PrecioBoleta(categoria, fase_venta, precio, descuento)
                controller.precios_boleta_lista.append(precio_boleta)
                st.session_state.my_state.precios_boleta_lista = controller.precios_boleta_lista
                st.success("Boleta agregada exitosamente")

    1.3 **Agregar Evento al Sistema**:
        -Una vez completados los detalles del evento, el administrador puede agregar el evento al sistema:
        
            if st.button("Agregar evento"):
                lista_artistas = artistas.split(",")
                if tipo_evento == "EventoBar":
                    nuevo_evento = EventoBar(
                        nombre_evento, fecha, hora_apertura, hora_evento, lugar, direccion, ciudad,
                        estado_evento, aforo_total, controller.precios_boleta_lista, lista_artistas
            )
        elif tipo_evento == "EventoTeatro":
            nuevo_evento = EventoTeatro(
                nombre_evento, fecha, hora_apertura, hora_evento, lugar, direccion, ciudad,
                estado_evento, aforo_total, controller.precios_boleta_lista, lista_artistas, valor_alquiler
            )
        elif tipo_evento == "EventoFilantropico":
            lista_patrocinadores = patrocinadores.split(",")
            lista_patrocinadores_valor = list(map(float, patrocinadores_valor_aportado.split(",")))
            nuevo_evento = EventoFilantropico(
                nombre_evento, fecha, hora_apertura, hora_evento, lugar, direccion, ciudad,
                estado_evento, aforo_total, controller.precios_boleta_lista, lista_artistas,
                lista_patrocinadores, lista_patrocinadores_valor
            )

        controller.eventos_lista.append(nuevo_evento)
        st.session_state.my_state.eventos_lista = controller.eventos_lista
        st.success("Evento agregado exitosamente")

        controller.precios_boleta_lista = []
        st.session_state.my_state.precios_boleta_lista = controller.precios_boleta_lista

    1.4 **Ver y Actualizar Eventos Existentes**:
        -El administrador puede seleccionar y ver los detalles de los eventos existentes, así como actualizar el estado de un evento:

                st.subheader("Eventos actuales")
                nombres_eventos = [evento.nombre for evento in controller.eventos_lista]
                evento_seleccionado = st.selectbox("Seleccione un evento", nombres_eventos)

                for evento in controller.eventos_lista:
                    if evento.nombre == evento_seleccionado:
                        st.write(f"Nombre del evento: {evento.nombre}")
                        st.write(f"Fecha del evento: {evento.fecha}")
                        st.write(f"Hora de apertura: {evento.hora_apertura}")
                        st.write(f"Hora del evento: {evento.hora_show}")
                        st.write(f"Lugar del evento: {evento.lugar}")
                        st.write(f"Dirección del evento: {evento.direccion}")
                        st.write(f"Ciudad del evento: {evento.ciudad}")
                        st.write(f"Estado del evento: {evento.estado}")
                        st.write(f"Aforo del evento: {evento.aforo_total}")
                        st.write(f"Artistas: {', '.join(evento.artistas)}")
                        st.write(
                            f"Boletas disponibles: {', '.join([f'{boleta.categoria} - {boleta.precio}' for boleta in evento.precio_boleta])}")

                        if isinstance(evento, EventoTeatro):
                            st.write(f"Valor de alquiler: {evento.valor_alquiler}")
                        if isinstance(evento, EventoFilantropico):
                            st.write(f"Patrocinadores: {', '.join(evento.patrocinadores)}")
                            st.write(
                                f"Valores aportados por patrocinadores: {', '.join(map(str, evento.patrocinadores_valor_aportado))}")

                        if evento.estado != "Realizado":
                            nuevo_estado = st.selectbox("Nuevo estado del evento",
                                                        ["Por realizar", "Realizado", "Cancelado", "Aplazado", "Cerrado",
                                                        "Sold out"])
                            if st.button("Actualizar estado del evento"):
                                evento.estado = nuevo_estado
                                st.success("Estado del evento actualizado exitosamente")
                        else:
                            st.write("El estado 'Realizado' no se puede cambiar.")

                        st.write("---------------------------------------------------------------------------------------------")






