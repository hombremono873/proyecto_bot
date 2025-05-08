import streamlit as st
import os
from streamlit_option_menu import option_menu

# ------------------- Estilos para el Menú Personalizado -------------------

MENU_STYLE = {
    "container": {
        "background-color": "#1f1f2e",
        "padding": "10px",
        "border-radius": "8px"
    },
    "icon": {
        "color": "#00c0ff",
        "font-size": "20px"
    },
    "nav-link": {
        "font-size": "16px",
        "text-align": "left",
        "margin": "5px",
        "--hover-color": "#33334d",
        "color": "#ffffff"
    },
    "nav-link-selected": {
        "background-color": "#00c0ff",
        "color": "white",
        "font-weight": "bold"
    }
}
# ------------------- Menú Vertical (Sidebar Personalizado) -------------------

def mostrar_menu_vertical():
    with st.sidebar:
        # Encabezado visual personalizado con "IA"
        st.markdown("""
            <div style='display:flex; align-items:center; margin-bottom:10px;'>
                <span style='
                    background-color: #00c0ff;
                    color: white;
                    padding: 4px 8px;
                    border-radius: 6px;
                    font-weight: bold;
                    font-size: 14px;
                    margin-right: 8px;
                '>IA</span>
                <span style='color:#00c0ff; font-weight:bold; font-size:18px;'>Tutor IA</span>
            </div>
        """, unsafe_allow_html=True)

        # Menú personalizado con estilos aplicados desde MENU_STYLE
        seleccion = option_menu(
            menu_title=None,
            options=["Inicio", "Tutor", "Configuración"],
            icons=["house", "robot", "gear"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
            key="menu_vertical",
            styles=MENU_STYLE
            #styles={} 
        )
    return seleccion

# ------------------- Cargar Estilos Globales (CSS externo) -------------------

def cargar_estilo():
    ruta_css = os.path.join("estilos", "estilo.css")
    if os.path.exists(ruta_css):
        with open(ruta_css, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
