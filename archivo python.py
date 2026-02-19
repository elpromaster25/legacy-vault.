import streamlit as st
import pandas as pd

# 1. BASE DE DATOS DE LLAVES VIP (Aquí creas los accesos que vendes)
# "CLAVE": "NOMBRE DEL DUEÑO DE LA FORTUNA"
LLAVES_VIP = {
    "LEGACY2026": "ADMIN DYLAN",
    "MADERO2000": "INVERSIONES PUERTO MADERO",
    "NORDELTA_VIP": "FAMILIA EINSTEIN",
    "GLOBAL_VAULT": "CLIENTE INTERNACIONAL"
}

# Configuración de página inicial (Antes del Login)
st.set_page_config(page_title="LEGACY VAULT | ACCESO", page_icon="🔒", layout="centered")

# Estética General
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    .stMarkdown p { color: white; text-align: center; }
    div.stButton > button { background-color: #d4af37; color: black; font-weight: bold; width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Control de Sesión
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
    st.session_state.usuario = ""

# --- PANTALLA DE LOGIN ---
if not st.session_state.autenticado:
    st.title("🗝️ LEGACY VAULT")
    st.write("Bienvenido al sistema de gestión de activos de alta gama. Ingrese su llave personalizada.")
    
    password = st.text_input("LLAVE DE ACCESO:", type="password")
    
    if st.button("DESBLOQUEAR PATRIMONIO"):
        if password in LLAVES_VIP:
            st.session_state.autenticado = True
            st.session_state.usuario = LLAVES_VIP[password]
            st.success(f"Acceso Concedido: {st.session_state.usuario}")
            st.rerun()
        else:
            st.error("Llave inválida. Intento de acceso denegado.")
    st.stop()

# --- PANEL PRINCIPAL (POST-LOGIN) ---
st.title("🗝️ PANEL DE CONTROL VIP")
st.write(f"SISTEMA ACTIVO PARA: **{st.session_state.usuario}**")
st.markdown("---")

# Métricas de los Millones
col1, col2 = st.columns(2)
with col1:
    st.metric(label="VALOR NETO TOTAL", value="$12,450,000 USD", delta="+2.4% (Mensual)")
    st.info("💡 IA Sugerencia: Recomendamos diversificar un 5% extra en activos líquidos.")

with col2:
    st.subheader("📊 Distribución del Capital")
    data = {"Activo": ["Inmuebles", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]}
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Activo"))

# Asistente IA
st.markdown("---")
st.subheader("🤖 ESTRATEGA IA PRIVADO")
pregunta = st.text_input("Consultar sobre movimientos de mercado o riesgos:")
if pregunta:
    with st.spinner('Analizando variables...'):
        st.write(f"🏛️ **LEGACY AI:** Estimado **{st.session_state.usuario}**, tras analizar '{pregunta}', mi informe indica una tendencia alcista. Mantener posición.")

# Sidebar de Seguridad
with st.sidebar:
    st.image("https://img.icons8.com")
    st.write("### 🔒 SEGURIDAD")
    st.write(f"Usuario: {st.session_state.usuario}")
    if st.button("CERRAR BÓVEDA"):
        st.session_state.autenticado = False
        st.rerun()
    st.write("---")
    st.write("© 2026 LEGACY VAULT S.A.")
