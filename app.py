import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Utils y vistas
from utils.gpt import inicializar_contexto_desde_txt
from utils.interfaz import mostrar_menu_vertical, cargar_estilo
from utils.vistas import vista_tutor
from pages.inicio import vista_inicio
from pages.tutor import vista_tutor

# ------------------------------ Cargar estilo --------------------------------
cargar_estilo()
# ---------------------------- Inicializar contexto ---------------------------
if "contexto" not in st.session_state:
    st.session_state.contexto = inicializar_contexto_desde_txt()

# ---------------------------- Barra de Navegación ----------------------------
opcion = mostrar_menu_vertical()

# ---------------------------- Cargar Página Seleccionada ---------------------
if opcion == "Inicio":
    vista_inicio()
elif opcion == "Tutor":
    vista_tutor()
elif opcion == "Configuración":
    st.info("La sección de configuración está en construcción.")
