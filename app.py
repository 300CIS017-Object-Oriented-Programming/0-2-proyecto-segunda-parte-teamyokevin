# gui_controller.py
import sys
import os


sys.path.append(r'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/controlador')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/modelos')
sys.path.insert(0, 'C:/Users/kevin/Desktop/Proyecto/Proyecto_entregas/3/0-2-proyecto-segunda-parte-teamyokevin/view')

from controlador.gui_controller import GUIController

import streamlit as st



def main():
    gui_controller = GUIController()
    gui_controller.main()


if __name__ == "__main__":
    main()

