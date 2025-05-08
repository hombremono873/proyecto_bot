# ------------------- Leer y retornar la api_key para acceder a GPT ------------------------------
from openai import OpenAI
import os
def obtener_api_key(ruta_archivo_clave):
    """
    Lee y retorna la clave API desde un archivo local.
    Se espera que el archivo contenga solo la clave en una sola línea.
    """
    try:
        with open(ruta_archivo_clave, encoding="utf-8") as f:
            clave = f.read().strip()
            if not clave:
                raise ValueError("El archivo de clave API está vacío.")
            return clave
    except FileNotFoundError:
        return "⚠️ Error: archivo de clave no encontrado."
    except Exception as e:
        return f"⚠️ Error al leer la clave API: {str(e)}"



# ------------------- Crear Cliente AI ------------------------------
#ruta_clave = "/Tutor_Algoritmos/KeySecret.txt"
def crear_cliente_openai():
    ruta_clave = os.path.join(os.getcwd(), "KeySecret.txt")
    key = obtener_api_key(ruta_clave)
    if "⚠️" in key:
        return key  # Retorna el mensaje de error directamente
    return OpenAI(api_key=key)

# ------------------------------------Crear Cliente OpenAI ------------------------------
#cliente = crear_cliente_openai()
# ------------------------Inicialización delContexto-------------------------------------
def inicializar_contexto():
    """
    Retorna el contexto inicial para un asistente de ciberseguridad.
    """
    return [
        {
            "role": "system",
            "content": (
                "Eres un asistente profesor, y tu mision es enseñarme a programar en lenguaje natural produzca diagramas de flujo usando graphviz."
                "Respondes de forma clara, precisa y profesional. "
                "Me muestras ejemplos segun la solicitud del usuario"
               
                
            )
        }
    ]
    
# --------------------------------Conexion---------------------------------------------------
#gpt-4o-mini
def generar_respuesta(cliente, contexto, modelo="gpt-4o-mini", temperatura=0):
    try:
        respuesta = cliente.chat.completions.create(
            model=modelo,
            messages=contexto,
            temperature=temperatura
        )
        mensaje_asistente = respuesta.choices[0].message.content
        return mensaje_asistente
    except Exception as e:
        return f"⚠️ Error al generar respuesta: {str(e)}"

# -----------------------------Lectura de La Base del Conocimiento ---------------------------------   
# Lee el contenido del archivo base de prompts
def leer_prompts_base(ruta):
    try:
        with open(ruta, encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        return f"⚠️ Error al leer prompts base: {e}"

# Inicializa el contexto de sistema desde el archivo
def inicializar_contexto_desde_txt():
    # Calcula ruta relativa al archivo base.txt
    ruta = r"C:\Users\OMAR TORRES\Desktop\Tutor_Algoritmos\Implementación Tutor Virtual para.txt"
    contenido = leer_prompts_base(ruta)
    return [{"role": "system", "content": contenido}]
#---------------------------------------------------------------------------------------------------

