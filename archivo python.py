import streamlit as st
import pandas as pd
import time

# 1. SEGURIDAD DE BÓVEDA (Clave: LEGACY2026)
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="IDENTIFICACIÓN REQUERIDA", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO RESTRINGIDO: LEGACY QUANTUM")
    password = st.text_input("INGRESE LLAVE DE ENCRIPTACIÓN:", type="password")
    if st.button("DESBLOQUEAR TERMINAL"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ACCESO DENEGADO.")
    st.stop()

# 2. CONFIGURACIÓN DE ÉLITE (Aquí vuelve el diseño pesado)
st.set_page_config(page_title="LEGACY COMMAND CENTER", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Courier New'; text-align: center; letter-spacing: 2px; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 3rem !important; font-weight: bold; }
    .stMarkdown p { color: #888; font-family: 'Courier New'; text-align: center; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 3. INTERFAZ DE COMANDO
st.markdown("<marquee style='color: #d4af37; font-family: Courier New;'>● MERCADOS GLOBALES OPERANDO ● SEGURIDAD ACTIVA ● BITCOIN: BULLISH TREND ●</marquee>", unsafe_allow_html=True)
st.title("🏛️ LEGACY COMMAND CENTER")
st.markdown(f"<p style='color: #00ff00; font-size: 0.8rem;'>● CONEXIÓN SEGURA ACTIVA | PROTOCOLO AES-256 | {time.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

# 4. MÉTRICAS DE MERCADO
m1, m2, m3, m4 = st.columns(4)
m1.metric("S&P 500", "5,026", "+0.45%")
m2.metric("NASDAQ", "17,861", "+1.1%")
m3.metric("BITCOIN", "$98,450", "+2.5%")
m4.metric("ORO (XAU)", "$2,150", "-0.05%")

st.markdown("---")

# 5. BÓVEDA PRINCIPAL
c1, c2 = st.columns(2)
with c1:
    st.subheader("💰 PATRIMONIO NETO")
    st.metric(label="EQUITY TOTAL", value="$12,450,000", delta="+$298,800 (30D)")
    st.download_button("📄 EXPORTAR INFORME BANCARIO", "PATRIMONIO VERIFICADO: $12.45M USD", file_name="Legacy_Report.txt")

with c2:
    st.subheader("📊 DISTRIBUCIÓN DE ACTIVOS")
    df = pd.DataFrame({"Activo": ["Propiedades", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df.set_index("Activo"))

# 6. IA ESTRATÉGICA
st.markdown("---")
st.subheader("🤖 LEGACY IA: PROTOCOLO DE CONSULTA")
pregunta = st.text_input("INGRESE CONSULTA PARA EL ANALISTA DE IA:")
if pregunta:
    with st.spinner('Analizando variables...'):
        time.sleep(1)
        st.write(f"🕵️ **ANALISTA IA:** Dylan García, para '{pregunta}' la orden es: MANTENER Y REBALANCIAR.")

# 7. LOGOUT SEGURO
if st.sidebar.button("🔒 CERRAR TERMINAL"):
    st.session_state.autenticado = False
    st.rerun()
