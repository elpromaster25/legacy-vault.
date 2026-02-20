import streamlit as st
import pandas as pd
import time
import random

# --- 1. SEGURIDAD DE ACCESO ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="IDENTIFICACIÓN REQUERIDA", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO RESTRINGIDO: LEGACY QUANTUM")
    password = st.text_input("INGRESE LLAVE DE ENCRIPTACIÓN:", type="password")
    if st.button("DESBLOQUEAR TERMINAL"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ACCESO DENEGADO. IP RASTREADA.")
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE ---
st.set_page_config(page_title="LEGACY COMMAND CENTER", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Courier New'; text-align: center; letter-spacing: 2px; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.5rem !important; }
    .stMarkdown p { color: #888; font-family: 'Courier New'; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; height: 3em; width: 100%; }
    div.stButton > button:hover { background-color: #d4af37; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA DE ESTADO SATELITAL ---
st.markdown(f"<p style='text-align: right; color: #00ff00; font-size: 0.7rem;'>● SERVIDOR ENCRIPTADO: ACTIVO | SEÑAL SATELITAL: 99% | FECHA: {time.strftime('%d/%m/%Y')}</p>", unsafe_allow_html=True)

st.title("🏛️ LEGACY COMMAND CENTER")
st.markdown("<p style='text-align: center;'>CENTRAL DE INTELIGENCIA FINANCIERA PARA ACTIVOS GLOBALES</p>", unsafe_allow_html=True)

# --- 4. TERMINAL DE MERCADOS ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("S&P 500", "5,026", "+0.45%")
m2.metric("NASDAQ", "17,861", "+1.1%")
m3.metric("BITCOIN", "$98,450", "+2.5%")
m4.metric("GOLD", "$2,150", "-0.05%")

st.markdown("---")

# --- 5. BÓVEDA PRINCIPAL ---
c1, c2 = st.columns([1, 2])
with c1:
    st.subheader("💰 PATRIMONIO NETO")
    st.metric(label="EQUITY TOTAL", value="$12,450,000", delta="+$298,800 (ESTE MES)")
    st.info("ℹ️ Auditoría Real-Time: Sus activos están protegidos por el protocolo Legacy-Secure.")
    st.download_button("📄 EXPORTAR INFORME BANCARIO", "PATRIMONIO VERIFICADO: $12.45M", file_name="Legacy_Report.txt")

with c2:
    st.subheader("📡 MAPA DE CALOR DE INVERSIONES")
    # Gráfico de barras pro
    chart_data = pd.DataFrame({"Activo": ["Propiedades", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(chart_data.set_index("Activo"))

# --- 6. SIMULADOR DE ESCENARIOS ---
st.markdown("---")
st.subheader("🚨 SIMULADOR DE ESCENARIOS DE RIESGO")
col_s1, col_s2 = st.columns(2)
with col_s1:
    escenario = st.selectbox("ELEGIR ESCENARIO:", ["Mercado Estable", "Crisis de Inflación", "Boom Tecnológico"])
with col_s2:
    if st.button("EJECUTAR SIMULACIÓN"):
        with st.spinner("PROCESANDO MODELO MATEMÁTICO..."):
            time.sleep(2)
            if escenario == "Mercado Estable":
                st.write("🟢 **RESULTADO:** Crecimiento sostenido del 8% anual.")
            elif escenario == "Crisis de Inflación":
                st.write("🔴 **RESULTADO:** Pérdida del 12% en liquidez. Recomendación: Mover activos a ORO.")
            else:
                st.write("💎 **RESULTADO:** Su inversión en Cripto y Tech explotaría un 45%.")

# --- 7. IA ESTRATÉGICA ---
st.markdown("---")
st.subheader("🤖 LEGACY AI: PROTOCOLO DE CONSULTA")
pregunta = st.text_input("INGRESE CONSULTA PARA EL ANALISTA DE IA:")
if pregunta:
    st.write(f"🕵️ **ANALISTA IA:** Basado en su consulta sobre '{pregunta}', la orden es: MANTENER Y REBALANCIAR.")

# --- 8. LOGOUT SEGURO ---
if st.sidebar.button("🔒 CERRAR TERMINAL"):
    st.session_state.autenticado = False
    st.rerun()

