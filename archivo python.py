import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD DE ACCESO ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="IDENTIFICACIÓN REQUERIDA", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO RESTRINGIDO: LEGACY QUANTUM")
    password = st.text_input("INGRESE LLAVE DE ENCRIPTACIÓN:", type="password")
    if st.button("DESBLOQUEAR TERMINAL"):
        if password == "LEGACY2026":
            with st.status("Iniciando Protocolos...", expanded=True) as status:
                st.write("🧬 Escaneando Firma Digital...")
                time.sleep(1)
                st.write("🟢 Identidad Verificada: Dylan García.")
                status.update(label="Acceso Concedido", state="complete", expanded=False)
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ACCESO DENEGADO.")
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE (FUERZA BRUTA DORADA) ---
st.set_page_config(page_title="LEGACY COMMAND CENTER", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    /* Fondo y fuentes generales */
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Courier New'; text-align: center; letter-spacing: 2px; }
    
    /* ESTE ES EL TRUCO PARA LAS MÉTRICAS GIGANTES Y DORADAS */
    [data-testid="stMetric"] {
        text-align: center;
        background-color: rgba(212, 175, 55, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 15px;
        border-radius: 5px;
    }
    [data-testid="stMetricValue"] {
        color: #d4af37 !important;
        font-size: 3rem !important;
        font-weight: bold !important;
        justify-content: center !important;
    }
    [data-testid="stMetricLabel"] {
        color: #ffffff !important;
        justify-content: center !important;
        font-size: 1.1rem !important;
    }
    
    .stMarkdown p { color: #888; font-family: 'Courier New'; text-align: center; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA DE NOTICIAS ---
st.markdown("<marquee style='color: #d4af37; font-family: Courier New;'>● MERCADOS GLOBALES OPERANDO ● SEGURIDAD ACTIVA ● BITCOIN BULLISH TREND ●</marquee>", unsafe_allow_html=True)
st.title("🏛️ LEGACY COMMAND CENTER")

# --- 4. MÉTRICAS SUPERIORES (AHORA SÍ, DORADAS Y GRANDES) ---
t1, t2, t3, t4 = st.columns(4)
t1.metric("STATUS", "SECURE", "100%")
t2.metric("S&P 500", "5,026", "+0.4%")
t3.metric("BITCOIN", "$98,450", "+2.5%")
t4.metric("RIESGO", "BAJO", "SÓLIDO")

st.markdown("---")

# --- 5. SECTOR BITCOIN PRO (CENTRADO) ---
col_izq, col_central, col_der = st.columns([1, 2, 1]) 
with col_central:
    st.image("https://img.icons8.com", width=160)
    st.metric("VALOR ACTUAL BTC/USD", "$98,450.00", "+2.5%")
    st.write("RED: **BLOCKCHAIN MAINNET**")

st.markdown("---")

# --- 6. BÓVEDA Y GRÁFICOS ---
c1, c2 = st.columns(2)
with c1:
    st.subheader("💰 PATRIMONIO NETO")
    st.metric(label="EQUITY TOTAL", value="$12,450,000", delta="+$298,800")
    st.download_button("📄 EXPORTAR INFORME", "PATRIMONIO: $12.45M USD", file_name="Legacy_Report.txt")

with c2:
    st.subheader("📊 DISTRIBUCIÓN")
    chart_data = pd.DataFrame({"Activo": ["Propiedades", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(chart_data.set_index("Activo"))

# --- 7. IA Y CIERRE ---
st.markdown("---")
st.subheader("🤖 IA ESTRATÉGICA")
pregunta = st.text_input("CONSULTA:")
if pregunta:
    st.write(f"🕵️ **ANALISTA:** Dylan García, para '{pregunta}' la orden es MANTENER.")

with st.sidebar:
    if st.button("🔒 CERRAR TERMINAL"):
        st.session_state.autenticado = False
        st.rerun()
