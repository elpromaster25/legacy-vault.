import streamlit as st
import pandas as pd
import time

# 1. SEGURIDAD (La llave de oro)
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="ACCESO PRIVADO", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO RESTRINGIDO: LEGACY")
    password = st.text_input("INGRESE CLAVE:", type="password")
    if st.button("DESBLOQUEAR"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("CLAVE INCORRECTA")
    st.stop()

# 2. DISEÑO DE LUJO
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; }
    .stMarkdown p { color: #888; }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTENIDO (Lo que se ve)
st.title("🏛️ LEGACY COMMAND CENTER")
st.markdown("<marquee style='color: #d4af37;'>● MERCADOS GLOBALES OPERANDO ● SEGURIDAD ACTIVA ● BITCOIN: BULLISH ●</marquee>", unsafe_allow_html=True)

# Métricas
m1, m2, m3, m4 = st.columns(4)
m1.metric("S&P 500", "5,026", "+0.4%")
m2.metric("BITCOIN", "$98,450", "+2.5%")
m3.metric("EQUITY TOTAL", "$12.45M", "+2.4%")
m4.metric("STATUS", "SECURE", "ONLINE")

st.markdown("---")

# Gráfico y IA
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 Distribución de Capital")
    df = pd.DataFrame({"Activo": ["Propiedades", "Acciones", "Cripto"], "Valor": [60, 20, 20]})
    st.bar_chart(df.set_index("Activo"))

with c2:
    st.subheader("🤖 Analista IA")
    pregunta = st.text_input("Consulta a la IA:")
    if pregunta:
        st.write(f"🕵️ **IA:** Dylan García, para '{pregunta}' la orden es MANTENER.")

# Botón de Salir
if st.sidebar.button("Cerrar Sesión"):
    st.session_state.autenticado = False
    st.rerun()
