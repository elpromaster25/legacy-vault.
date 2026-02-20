import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD BIOMÉTRICA ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="ACCESO PRIVADO", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🔐 TERMINAL DE ACCESO PRIVADO")
    password = st.text_input("LLAVE MAESTRA:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            with st.status("Iniciando Protocolos...", expanded=True) as status:
                st.write("🟢 Identidad Verificada: Dylan García.")
                status.update(label="Acceso Concedido", state="complete", expanded=False)
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("ACCESO DENEGADO.")
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE (DISEÑO DORADO) ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; text-transform: uppercase; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 3.2rem !important; font-weight: bold; text-align: center; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; font-size: 1.1rem !important; text-align: center; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; font-weight: bold; }
    .stSlider [data-baseweb="slider"] { color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TÍTULO Y RADAR ---
st.markdown("<marquee style='color: #d4af37; font-size: 1.1rem;'>● MERCADOS GLOBALES OPERANDO ● SEGURIDAD ACTIVA ● BITCOIN BULLISH ●</marquee>", unsafe_allow_html=True)
st.title("🏛️ CENTRO DE MANDO LEGACY")

# 4. MONITOR DE CAPITAL
m1, m2, m3 = st.columns(3)
m1.metric("VALOR NETO", "$12.45M", "+2.4%")
m2.metric("BITCOIN", "$98,450", "+2.5%")
m3.metric("RIESGO", "MÍNIMO", "SEGURO")

st.markdown("---")

# --- 5. SECTOR BITCOIN Y SIMULADOR (EL REGRESO) ---
col_b1, col_b2, col_b3 = st.columns()
with col_b2:
    st.image("https://img.icons8.com", width=120)
    st.subheader("🚀 PROYECCIÓN DE FORTUNA")
    años = st.slider("AÑOS DE INVERSIÓN:", 1, 30, 10)
    retorno = st.slider("RENDIMIENTO ANUAL ESPERADO (%):", 5, 50, 15)
    
    capital = 12450000
    futuro = capital * ((1 + (retorno/100))**años)
    st.metric("VALOR ESTIMADO", f"${futuro:,.0f} USD")

st.markdown("---")

# 6. GRÁFICOS Y IA
col_izq, col_der = st.columns(2)
with col_izq:
    st.subheader("📊 DISTRIBUCIÓN DE ACTIVOS")
    df = pd.DataFrame({"Activo": ["Inmuebles", "Stocks", "Crypto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df.set_index("Activo"))

with col_der:
    st.subheader("🤖 ESTRATEGA IA")
    pregunta = st.text_input("CONSULTA TÉCNICA:")
    if pregunta:
        with st.spinner('Analizando...'):
            time.sleep(1)
            st.write(f"🏛️ **IA:** Dylan García, para '{pregunta}' la orden es: MANTENER Y REBALANCIAR.")
    st.write("---")
    st.download_button("📥 DESCARGAR AUDITORÍA VIP", "CERTIFICADO: $12.45M USD", file_name="Reporte_Legacy.txt")

if st.sidebar.button("🔒 CERRAR SESIÓN"):
    st.session_state.autenticado = False
    st.rerun()
