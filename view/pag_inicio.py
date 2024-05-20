# import sys
# import os
#
# sys.path.append(r'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/2/pythonProject')
# sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/2/pythonProject/modelos')
#
# import streamlit as st
# import bcrypt
# from modelos.boleteria_b import PrecioBoleta
# from modelos.evento_b import Evento, GestorEventos
#
#
#
#
# # import evento_b
# # Lista de usuarios autorizados (simulación)
#
# usuarios_autorizados = {
#     "admin": {
#         "password": bcrypt.hashpw("admin123".encode("utf-8"), bcrypt.gensalt()),
#         "role": "admin"
#     },
#     "comprador": {
#         "password": bcrypt.hashpw("comprador123".encode("utf-8"), bcrypt.gensalt()),
#         "role": "comprador"
#     }
# }
#
#
# def autenticar_usuario(username, password):
#     """Función para autenticar al usuario."""
#     if username in usuarios_autorizados:
#         stored_password = usuarios_autorizados[username]["password"]
#         return bcrypt.checkpw(password.encode("utf-8"), stored_password)
#     return False
#
#
# def crear_usuario(username, password, role="comprador"):
#     """Función para crear un nuevo usuario."""
#     if username not in usuarios_autorizados:
#         hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
#         usuarios_autorizados[username] = {"password": hashed_password, "role": role}
#         return True
#     return False
#
#
# def pagina_inicio():
#     """Página de inicio."""
#     st.title("Bienvenido a la Boletería")
#
#     # Formulario de inicio de sesión
#     username = st.text_input("Nombre de usuario")
#     password = st.text_input("Contraseña", type="password")
#     if st.button("Iniciar sesión"):
#         if autenticar_usuario(username, password):
#             st.success(f"Bienvenido, {username}!")
#             role = usuarios_autorizados[username]["role"]
#             if role == "admin":
#                 # Indicar que el administrador ha iniciado sesión y reiniciar la aplicación
#                 st.session_state.admin_logged_in = True
#                 st.experimental_rerun()
#             else:
#                 mostrar_pagina_comprador()
#         else:
#             st.error("Nombre de usuario o contraseña incorrectos")
#
#     # Formulario de creación de cuenta
#     st.subheader("Crear una cuenta")
#     nuevo_usuario = st.text_input("Nuevo nombre de usuario")
#     nueva_password = st.text_input("Nueva contraseña", type="password")
#     role = st.radio("Selecciona tu rol", ("Administrador", "Comprador"))
#     if st.button("Crear cuenta"):
#         if crear_usuario(nuevo_usuario, nueva_password, role):
#             st.success("Cuenta creada exitosamente")
#         else:
#             st.warning("El nombre de usuario ya existe")
#
#
# def mostrar_pagina_administrador():
#     """Página para administradores."""
#     st.title("Panel de Administrador")
#     precio_boleta = []
#     # Inicializar las variables en st.session_state si aún no existen
#     if "precios_boleta_lista" not in st.session_state:
#         st.session_state.precios_boleta_lista = []
#     if "eventos_lista" not in st.session_state:
#         st.session_state.eventos_lista = []
#
#     # Formulario para agregar un evento
#     st.subheader("Agregar un nuevo evento")
#     nombre_evento = st.text_input("Nombre del evento")
#     fecha = st.date_input("Fecha del evento")
#     hora_apertura = st.time_input("Hora de apertura de puertas")
#     hora_evento = st.time_input("Hora del evento")
#     lugar = st.text_input("Lugar del evento")
#     direccion = st.text_input("Dirección del evento")
#     ciudad = st.text_input("Ciudad del evento")
#     estado_evento = st.selectbox("Estado del evento", ("Por realizar", "Realizado", "Cancelado", "Aplazado", "Cerrado"))
#     aforo_total = st.text_input("Aforo del evento")
#     artistas = st.text_input("Artistas (separados por comas)")
#
#     # Campos de entrada para PrecioBoleta
#     st.subheader("Agregar Tipos de boleta")
#     categoria = st.selectbox("Categoria de la boleta", ("VIP", "Intermedio", "General"))
#     fase_venta = st.text_input("Fase de venta")
#     precio = st.number_input("Precio de la boleta")
#     descuento = st.number_input("Descuento de la boleta")
#     precios_boleta_lista = []
#
#     if st.button("Agregar boleta"):
#         # Crear un nuevo objeto PrecioBoleta
#         precio_boleta = PrecioBoleta(categoria, fase_venta, precio, descuento)
#         # Agregar el objeto PrecioBoleta a la lista
#         st.session_state.precios_boleta_lista.append(precio_boleta)
#         st.success("Boleta agregada exitosamente")
#         #st.write(f"Boletas actuales: {st.session_state.precios_boleta_lista}")
#
#     if st.button("Agregar evento"):
#         # Crear un nuevo objeto PrecioBoleta
#         #precio_boleta = Boleteria.PrecioBoleta(categoria, fase_venta, precio, descuento)
#
#
#         # Crear un nuevo evento con el objeto PrecioBoleta
#         lista_artistas = artistas.split(",")  # Dividir los nombres de los artistas por comas
#         nuevo_evento = Evento(nombre_evento, fecha, hora_apertura, hora_evento, lugar, direccion, ciudad,
#                                       estado_evento,aforo_total, st.session_state.precios_boleta_lista,lista_artistas)
#         lista_artistas_copia = lista_artistas.copy()
#         # Agregar los artistas al nuevo evento
#         for artista in lista_artistas_copia:
#             st.write("??????????????")
#             # Obtener la lista actual de artistas
#             artistas_actuales = nuevo_evento.artistas
#             # Agregar el nuevo artista a la lista
#             artistas_actuales.append(artista.strip())
#             # Establecer la lista actualizada de artistas
#             nuevo_evento.artistas = artistas_actuales
#
#         #precios_boleta_lista_copia = precios_boleta_lista.copy()
#         st.write(f"Boletas actuales copia: {precios_boleta_lista}")
#
#         #st.write(f"Boletas actuales: {precio_boleta1}")
#         #st.write(f"Boletas actuales: {precios_boleta_lista}")
#         nuevo_evento.agregar_precio_boleta(*precios_boleta_lista)
#
#         # Agregar el nuevo evento a la lista de eventos
#         st.session_state.gestor_eventos = GestorEventos()
#         st.session_state.gestor_eventos.agregar_evento(nuevo_evento)
#         st.success("Evento agregado exitosamente")
#
#         # Mostrar todos los eventos
#         st.subheader("Eventos actuales")
#         for evento in st.session_state.gestor_eventos.eventos:
#             st.write(f"Nombre del evento: {evento.nombre}")
#             st.write(f"Fecha del evento: {evento.fecha}")
#             st.write(f"Hora de apertura: {evento.hora_apertura}")
#             st.write(f"Hora del evento: {evento.hora_show}")
#             st.write(f"Lugar del evento: {evento.lugar}")
#             st.write(f"Dirección del evento: {evento.direccion}")
#             st.write(f"Ciudad del evento: {evento.ciudad}")
#             st.write(f"Estado del evento: {evento.estado}")
#             st.write(f"Aforo total: {evento.aforo_total}")
#             st.write(f"Artistas: {', '.join(evento.artistas)}")
#             st.write(f"Boletas actuales: {evento.precio_boleta}")
#
#             for boleta in evento.precio_boleta:
#                 st.write(
#                     f"Boleta: {boleta.categoria}, Fase de venta: {boleta.fase_venta}, Precio: {boleta.precio}, Descuento: {boleta.descuento}")
#         st.write(f"Boletas actuales: {precios_boleta_lista}")
#
#
#
# def mostrar_pagina_comprador():
#     """Página para compradores."""
#     st.title("Explora y compra boletas")
#     # Aquí puedes agregar funcionalidades para compradores
#
#
# # Ejecutar la aplicación
# if __name__ == "__main__":
#     # Verificar si el administrador ha iniciado sesión
#     if st.session_state.get("admin_logged_in", False):
#         mostrar_pagina_administrador()
#     else:
#         pagina_inicio()