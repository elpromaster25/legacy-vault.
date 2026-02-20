import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="IDENTIFICACIÓN REQUERIDA", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #050505; } h1 { color: #d4af37; text-align: center; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO RESTRINGIDO: LEGACY QUANTUM")
    password = st.text_input("INGRESE LLAVE DE ENCRIPTACIÓN:", type="password")
    if st.button("DESBLOQUEAR TERMINAL"):
        if password == "LEGACY2026":
            with st.status("Verificando Huella Digital...", expanded=True) as status:
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
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Courier New'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 3rem !important; font-weight: bold; text-align: center; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; justify-content: center !important; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; border-radius: 0px; width: 100%; }
    /* Estilo para el Slider de Oro */
    .stSlider [data-baseweb="slider"] { color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INTERFAZ ---
st.markdown("<marquee style='color: #d4af37;'>● MERCADOS OPERANDO ● SEGURIDAD ACTIVA ● BITCOIN BULLISH ●</marquee>", unsafe_allow_html=True)
st.title("🏛️ LEGACY COMMAND CENTER")

# --- 4. MÉTRICAS SUPERIORES ---
t1, t2, t3, t4 = st.columns(4)
t1.metric("STATUS", "SECURE", "100%")
t2.metric("S&P 500", "5,026", "+0.4%")
t3.metric("BITCOIN", "$98,450", "+2.5%")
t4.metric("RIESGO", "BAJO", "SÓLIDO")

st.markdown("---")

# --- 5. EL "GANCHO" DEL EMPRESARIO: PROYECCIÓN PATRIMONIAL ---
st.subheader("🚀 SIMULADOR DE CRECIMIENTO PATRIMONIAL")
st.write("Mueva la barra para proyectar su fortuna con nuestra IA en los próximos 10 años.")

col_s1, col_s2 = st.columns([2, 1])
with col_s1:
    años = st.slider("AÑOS DE INVERSIÓN:", 1, 30, 10)
    interes = st.slider("RETORNO ANUAL ESPERADO (%):", 5, 50, 15)
with col_s2:
    capital_inicial = 12450000
    futuro = capital_inicial * ((1 + (interes/100))**años)
    st.metric("FORTUNA ESTIMADA", f"${futuro:,.0f}")
    st.write(f"Con un retorno del {interes}% anual.")

st.markdown("---")

# --- 6. BITCOIN Y GRÁFICOS ---
c1, c2 = st.columns(2)
with c1:
    st.image("https://img.icons8.com", width=120)
    st.metric("VALOR BTC/USD", "$98,450.00")
    st.download_button("📄 EXPORTAR AUDITORÍA VIP", "PATRIMONIO: $12.45M", file_name="Legacy_Audit.txt")

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

if st.sidebar.button("🔒 CERRAR TERMINAL"):
    st.session_state.autenticado = False
    st.rerun()
