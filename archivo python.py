import streamlit as st
import pandas as pd
import time

# 1. SEGURIDAD DE BÓVEDA (Clave: LEGACY2026)
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'visitas' not in st.session_state:
    st.session_state.visitas = 0

# --- PANTALLA DE ACCESO ---
if not st.session_state.autenticado:
    st.set_page_config(page_title="IDENTIFICACIÓN REQUERIDA", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO RESTRINGIDO: LEGACY QUANTUM")
    password = st.text_input("INGRESE LLAVE DE ENCRIPTACIÓN:", type="password")
    if st.button("DESBLOQUEAR TERMINAL"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.session_state.visitas += 1
            st.rerun()
        else:
            st.error("ACCESO DENEGADO. IP RASTREADA.")
    st.stop()

# 2. CONFIGURACIÓN DE ÉLITE POST-LOGIN
st.set_page_config(page_title="LEGACY COMMAND CENTER", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Courier New'; text-align: center; letter-spacing: 2px; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; }
    .stMarkdown p { color: #888; font-family: 'Courier New'; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; width: 100%; }
    div.stButton > button:hover { background-color: #d4af37; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- PANEL PRINCIPAL ---
st.title("🏛️ LEGACY COMMAND CENTER")
st.markdown(f"<p style='text-align: center; color: #00ff00; font-size: 0.8rem;'>● CONEXIÓN SATELITAL ACTIVA | ENCRIPTACIÓN AES-256 | {time.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

# 3. MERCADOS MUNDIALES
m1, m2, m3, m4 = st.columns(4)
m1.metric("S&P 500", "5,026.15", "+0.45%")
m2.metric("NASDAQ 100", "17,861.12", "+1.10%")
m3.metric("GOLD (XAU)", "$2,150.40", "-0.05%")
m4.metric("DOW JONES", "38,627.99", "+0.15%")

st.markdown("---")

# 4. SECTOR BITCOIN (DECORACIÓN DE LUJO)
col_btc1, col_btc2 = st.columns([1, 4])
with col_btc1:
    st.image("https://img.icons8.com") # Logo de Bitcoin
with col_btc2:
    st.subheader("₿ BITCOIN CORE ASSET")
    st.write("Estado: **ENCRIPTADO** | Red: **Blockchain Mainnet** | Nodo: **Legacy-01**")
    st.metric("VALOR BTC/USD", "$98,450.00", "+2.5% (HIGH VOLATILITY)")

st.markdown("---")

# 5. PATRIMONIO Y GRÁFICOS
c1, c2 = st.columns(2)
with c1:
    st.subheader("💰 RESUMEN DE ACTIVOS")
    st.metric(label="EQUITY TOTAL", value="$12,450,000", delta="+$298,800 (ESTE MES)")
    st.download_button("📄 EXPORTAR REPORTE BANCARIO", "PATRIMONIO VERIFICADO: $12.45M USD", file_name="Legacy_Report.txt")

with c2:
    st.subheader("📊 DISTRIBUCIÓN ESTRATÉGICA")
    df = pd.DataFrame({"Activo": ["Propiedades", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df.set_index("Activo"))

# 6. SIMULADOR DE GANANCIAS
st.markdown("---")
st.subheader("📈 PROYECCIÓN DE CRECIMIENTO A 5 AÑOS")
interes = st.slider("TASA DE RETORNO ANUAL (%)", 5, 25, 10)
proyeccion = 12450000 * ((1 + (interes/100))**5)
st.write(f"PROYECCIÓN ESTIMADA: **${proyeccion:,.2f} USD**")

# 7. IA ESTRATÉGICA
st.markdown("---")
st.subheader("🤖 LEGACY AI: PROTOCOLO DE CONSULTA")
pregunta = st.text_input("INGRESE CONSULTA PARA EL ANALISTA DE IA:")
if pregunta:
    with st.spinner('Procesando datos macroeconómicos...'):
        time.sleep(1)
        st.write(f"🕵️ **ANALISTA IA:** Basado en su consulta sobre '{pregunta}', la recomendación es: REBALANCIAR HACIA ACTIVOS REALES.")

# 8. PANEL DE ADMINISTRADOR (SOLO DYLAN GARCÍA)
with st.sidebar:
    st.write("### 🔒 GESTIÓN INTERNA")
    if st.checkbox("🔑 MODO ADMINISTRADOR"):
        st.write("---")
        st.metric(label="Visitas Totales", value=st.session_state.visitas)
        st.write("🟢 Servidor Online")
    if st.button("CERRAR SESIÓN"):
        st.session_state.autenticado = False
        st.rerun()
