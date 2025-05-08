import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from utils.gpt import crear_cliente_openai, inicializar_contexto, generar_respuesta
import os
# ---------------------------- Vista de Inicio ----------------------------
        
def vista_inicio():
    st.markdown("## 👋 Bienvenido al Tutor Virtual de Algoritmos")
    st.markdown("""
    Este tutor te ayudará a entender los algoritmos paso a paso usando lenguaje natural.

    Puedes:
    - 📘 Elegir un tema como estructuras condicionales, ciclos, o divide y vencerás.
    - 🤖 Consultar al tutor con tus dudas.
    - 🧠 Recibir explicaciones detalladas, ejemplos y desafíos interactivos.

    ---
    👉 Selecciona una opción en el menú lateral para comenzar.
    """)

# ---------------------------- Vista del Tutor ----------------------------

def vista_tutor():
    st.header("📊 Tutor Virtual en Desarrollo de Algoritmos")

    cliente = crear_cliente_openai()
    if isinstance(cliente, str):
        st.error(cliente)
        return

    if "contexto" not in st.session_state:
        st.session_state.contexto = inicializar_contexto()

    pregunta = st.text_input("¿Sobre qué algoritmo tienes dudas hoy?")

    if st.button("Enviar") and pregunta:
        st.session_state.contexto.append({"role": "user", "content": pregunta})
        respuesta = generar_respuesta(cliente, st.session_state.contexto)
        st.session_state.contexto.append({"role": "assistant", "content": respuesta})

        st.markdown("### 🤖 Respuesta del Tutor")
        st.write(respuesta)

    st.info("¿Listo para comenzar? Explora el menú lateral.")
