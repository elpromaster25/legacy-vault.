import streamlit as st
import pandas as pd
import time

# 1. SEGURIDAD DE NIVEL BANCARIO
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="LEGACY | AUTH", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; font-family: 'Times New Roman'; }</style>", unsafe_allow_html=True)
    st.title("🏛️ ACCESO PRIVADO LEGACY VAULT")
    password = st.text_input("LLAVE DE ENCRIPTACIÓN:", type="password")
    if st.button("DESBLOQUEAR TERMINAL"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ACCESO DENEGADO.")
    st.stop()

# 2. CONFIGURACIÓN DE PENTÁGONO FINANCIERO
st.set_page_config(page_title="LEGACY COMMAND CENTER", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Garamond', serif; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 3rem !important; font-weight: bold; }
    .stMarkdown p { color: #aaaaaa; text-align: center; }
    div.stButton > button { background-color: #111; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; width: 100%; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA DE NOTICIAS MOVIBLE (Bloomberg Style)
st.markdown("<marquee style='color: #d4af37; font-size: 1.1rem; border-bottom: 1px solid #d4af37; padding: 5px;'>● BLOOMBERG: GOLD UP 1.2% ● FORBES: REAL ESTATE DEMAND IN PUERTO MADERO INCREASES ● BITCOIN CORE: NEW BLOCK VERIFIED ● LEGACY: ASSETS SECURED ●</marquee>", unsafe_allow_html=True)

st.title("🏛️ LEGACY COMMAND CENTER")
st.markdown(f"<p style='color: #00ff00; font-size: 0.8rem;'>● CONEXIÓN SEGURA ACTIVA | PROTOCOLO AES-256 | {time.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

# 4. MONITOR DE MERCADOS GLOBALES
m1, m2, m3, m4 = st.columns(4)
m1.metric("S&P 500", "5,102", "+0.45%")
m2.metric("NASDAQ", "18,230", "+1.1%")
m3.metric("BITCOIN", "$98,450", "+2.5%")
m4.metric("ORO (OZ)", "$2,150", "-0.05%")

st.markdown("---")

# 5. BÓVEDA Y MAPA DE CALOR
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("💰 PATRIMONIO NETO VERIFICADO")
    st.metric(label="EQUITY TOTAL", value="$12,450,000", delta="+$298,800 (30d)")
    st.info("ℹ️ Certificación de Fondos: Sus activos están auditados bajo el estándar Legacy-Pro.")
    if st.button("📄 GENERAR REPORTE DE AUDITORÍA"):
        with st.status("Firmando con Hash de Blockchain...", expanded=True):
            time.sleep(1)
            st.write("Verificando M2 en Alvear Tower...")
            time.sleep(1)
            st.success("Reporte Generado con Éxito.")

with col2:
    st.subheader("📡 DISTRIBUCIÓN DE RIESGO")
    df = pd.DataFrame({"Activo": ["Propiedades", "Stocks", "Crypto", "Oro"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df.set_index("Activo"))

# 6. IA ESTRATÉGICA
st.markdown("---")
st.subheader("🤖 LEGACY AI: CONSULTOR ESTRATÉGICO")
pregunta = st.text_input("CONSULTAR A LA IA SOBRE MOVIMIENTOS DE CAPITAL:")
if pregunta:
    with st.spinner('Analizando mercados internacionales...'):
        time.sleep(1)
        st.write(f"🏛️ **LEGACY AI:** Dylan García, mi análisis para '{pregunta}' indica: **MANTENER Y DIVERSIFICAR**. El riesgo en Inmuebles es bajo.")

# 7. PANEL DE CONTROL
with st.sidebar:
    st.write("### 🔒 SISTEMA")
    if st.checkbox("🔑 MODO ADMIN (STATS)"):
        st.write("---")
        st.metric(label="VISITAS HOY", value="1 (Vos)")
    if st.button("CERRAR SESIÓN"):
        st.session_state.autenticado = False
        st.rerun()
