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
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("CLAVE INCORRECTA")
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE (DISEÑO DORADO) ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 3rem !important; font-weight: bold; text-align: center; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; font-size: 1.2rem !important; text-align: center; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ CENTRO DE MANDO LEGACY")

# --- 3. SECCIÓN ARGENTINA (PESOS ARS - GIGANTE) ---
tc = 1500 # Cotización 2026
st.subheader("🇦🇷 VALORIZACIÓN EN PESOS ARGENTINOS (ARS)")
a1, a2 = st.columns(2)
a1.metric("PATRIMONIO TOTAL ARS", f"${(12450000 * tc):,.0f}", "MEP/BLUE")
a2.metric("BITCOIN EN ARS", f"${(98450 * tc):,.0f}", "BLOCKCHAIN")

st.markdown("---")

# --- 4. SECCIÓN INTERNACIONAL (DÓLARES USD) ---
st.subheader("🇺🇸 VALORIZACIÓN EN DÓLARES (USD)")
u1, u2, u3 = st.columns(3)
u1.metric("NET WORTH USD", "$12.45M", "+2.4%")
u2.metric("BTC PRICE", "$98,450", "+2.5%")
u3.metric("RENTABILIDAD", "$298.8K", "SECURE")

st.markdown("---")

# --- 5. SIMULADOR Y IA ---
st.subheader("🚀 PROYECCIÓN DE CRECIMIENTO (USD)")
años = st.slider("AÑOS DE INVERSIÓN:", 1, 30, 10)
ret = st.slider("RETORNO ANUAL (%):", 5, 50, 15)
futuro = 12450000 * ((1 + (ret/100))**años)
st.metric("VALOR ESTIMADO FUTURO", f"${futuro:,.0f} USD")

# --- 6. GRÁFICOS Y IA (SIN ERRORES) ---
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 DISTRIBUCIÓN")
    df_data = pd.DataFrame({"Activo": ["Casas", "Bolsa", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df_data.set_index("Activo"))
with c2:
    st.subheader("🤖 IA ESTRATÉGICA")
    pregunta = st.text_input("CONSULTA TÉCNICA:")
    if pregunta:
        st.write(f"🏛️ **IA:** Dylan García, para '{pregunta}' la orden es MANTENER.")
    st.download_button("📥 DESCARGAR AUDITORÍA", "VALOR: $12.45M USD", file_name="Reporte_Legacy.txt")

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.autenticado = False
    st.rerun()
