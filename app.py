# gui_controller.py
import sys
import os

sys.path.append(r'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/2/pythonProject')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/2/pythonProject/controlador')

from controlador.gui_controller import GUIController


import streamlit as st



if __name__ == "__main__":
    gui_controller = GUIController()
    if st.session_state['page'] == 'main':
        gui_controller.main()
    elif st.session_state['page'] == 'admin':
        gui_controller.mostrar_pagina_administrador()
    elif st.session_state['page'] == 'compraventa':
        gui_controller.mostrar_compraventa()
    elif st.session_state['page'] == 'asistencia':
        gui_controller.asistencia()
