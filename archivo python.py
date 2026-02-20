import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD ---
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

# --- 2. CONFIGURACIÓN DE LUJO ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.2rem !important; font-weight: bold; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ CENTRO DE MANDO LEGACY")

# --- 3. SENSORES DE CAPITAL ---
tc = 1500 # Cotización estimada 2026
capital_usd = 12450000
btc_usd = 98450

col_usd, col_ars = st.columns(2)

with col_usd:
    st.subheader("🇺🇸 ACTIVOS (USD)")
    st.metric("VALOR NETO", f"${capital_usd:,.0f}", "+2.4%")
    st.metric("BITCOIN", f"${btc_usd:,.0f}", "+2.5%")

with col_ars:
    st.subheader("🇦🇷 ACTIVOS (ARS)")
    st.metric("VALOR NETO", f"${(capital_usd * tc):,.0f}", "MEP/BLUE")
    st.metric("BITCOIN", f"${(btc_usd * tc):,.0f}", "BLOCKCHAIN")

st.markdown("---")

# --- 4. BITCOIN Y SIMULADOR ---
st.image("https://img.icons8.com", width=100)
st.subheader("🚀 PROYECCIÓN DE FORTUNA (USD)")
años = st.slider("AÑOS DE INVERSIÓN:", 1, 30, 10)
ret = st.slider("RETORNO ANUAL (%):", 5, 50, 15)
futuro = capital_usd * ((1 + (ret/100))**años)
st.metric("VALOR ESTIMADO FUTURO", f"${futuro:,.0f} USD")

st.markdown("---")

# --- 5. GRÁFICO Y IA (CORREGIDO Y SEGURO) ---
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 DISTRIBUCIÓN")
    # Datos fijos para evitar errores
    df_data = pd.DataFrame({
        "Activo": ["Inmuebles", "Stocks", "Crypto", "Arte"],
        "Valor": [60, 20, 10, 10]
    })
    st.bar_chart(df_data.set_index("Activo"))

with c2:
    st.subheader("🤖 IA ESTRATÉGICA")
    pregunta = st.text_input("CONSULTA TÉCNICA:")
    if pregunta:
        st.write(f"🏛️ **IA:** Dylan García, para '{pregunta}' la orden es MANTENER.")
    st.download_button("📥 DESCARGAR AUDITORÍA", "CERTIFICADO: $12.45M USD", file_name="Reporte_Legacy.txt")

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.autenticado = False
    st.rerun()
