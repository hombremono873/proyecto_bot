import streamlit as st
from utils.gpt import crear_cliente_openai, inicializar_contexto, generar_respuesta
#--------------------------------Vista Tutor------------------------------------

def vista_tutor():
    st.header("📊 Tutor Virtual en Desarrollo de Algoritmos")


    # Crear cliente GPT
    cliente = crear_cliente_openai()
    if isinstance(cliente, str):
        st.error(cliente)
        return

    # Contexto en sesión (para conservar historial)
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