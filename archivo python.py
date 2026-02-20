import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD DE ACCESO (EL SCANNER DE HUELLA) ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="IDENTIFICACIÓN REQUERIDA", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO RESTRINGIDO: LEGACY QUANTUM")
    password = st.text_input("INGRESE LLAVE DE ENCRIPTACIÓN:", type="password")
    if st.button("DESBLOQUEAR TERMINAL"):
        if password == "LEGACY2026":
            with st.status("Iniciando Protocolos de Seguridad...", expanded=True) as status:
                st.write("🧬 Escaneando Firma Digital Única...")
                time.sleep(1)
                st.write("🛰️ Verificando Localización Satelital...")
                time.sleep(1)
                st.write("🟢 Identidad Verificada: Dylan García.")
                status.update(label="Acceso Concedido", state="complete", expanded=False)
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ACCESO DENEGADO.")
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE ---
st.set_page_config(page_title="LEGACY COMMAND CENTER", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Courier New'; text-align: center; letter-spacing: 2px; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.8rem !important; font-weight: bold; }
    .stMarkdown p { color: #888; font-family: 'Courier New'; text-align: center; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA DE NOTICIAS ---
st.markdown("<marquee style='color: #d4af37; font-family: Courier New;'>● NY STOCK EXCHANGE: OPEN ● LONDRES: OPERANDO ● BITCOIN: BULLISH TREND ●</marquee>", unsafe_allow_html=True)
st.title("🏛️ LEGACY COMMAND CENTER")

# --- 4. MÉTRICAS DE MERCADO (LIMPIAS) ---
t1, t2, t3, t4 = st.columns(4)
t1.metric("STATUS", "SECURE", "100%")
t2.metric("S&P 500", "5,026", "+0.4%")
t3.metric("BITCOIN", "$98,450", "+2.5%")
t4.metric("RIESGO", "BAJO", "SÓLIDO")

st.markdown("---")

# --- 5. SECTOR BITCOIN PRO (REDISEÑADO PARA QUE NO SE CRUCE) ---
st.subheader("₿ BITCOIN CORE ASSET MONITOR")
col_b1, col_b2, col_b3 = st.columns([1, 2, 1])
with col_b2:
    st.image("https://img.icons8.com", use_container_width=False)
    st.write("RED: **BLOCKCHAIN MAINNET** | NODO: **LEGACY-ALPHA-01**")
    st.metric("VALOR ACTUAL BTC/USD", "$98,450.00", "+2.5% (HIGH VOLATILITY)")

st.markdown("---")

# --- 6. BÓVEDA Y GRÁFICOS ---
c1, c2 = st.columns(2)
with c1:
    st.subheader("💰 PATRIMONIO NETO")
    st.metric(label="EQUITY TOTAL", value="$12,450,000", delta="+$298,800")
    st.download_button("📄 EXPORTAR INFORME", "PATRIMONIO: $12.45M USD", file_name="Legacy_Report.txt")

with c2:
    st.subheader("📊 DISTRIBUCIÓN")
    df = pd.DataFrame({"Activo": ["Propiedades", "Stocks", "Crypto", "Arte"], "Valor":})
    st.bar_chart(df.set_index("Activo"))

# --- 7. IA Y CIERRE ---
st.markdown("---")
st.subheader("🤖 IA ESTRATÉGICA")
pregunta = st.text_input("CONSULTA:")
if pregunta:
    st.write(f"🕵️ **ANALISTA:** Dylan García, la recomendación es MANTENER.")

with st.sidebar:
    if st.button("🔒 CERRAR TERMINAL"):
        st.session_state.autenticado = False
        st.rerun()
