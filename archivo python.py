import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD DE ACCESO ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="ACCESO PRIVADO", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1 { color: #d4af37; text-align: center; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)
    st.title("🔐 TERMINAL DE ACCESO PRIVADO")
    password = st.text_input("LLAVE MAESTRA:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.2rem !important; font-weight: bold; }
    .pay-banner {
        background-color: rgba(212, 175, 55, 0.1);
        border: 2px solid #d4af37;
        color: #d4af37;
        padding: 15px;
        text-align: center;
        font-weight: bold;
        border-radius: 10px;
        margin-bottom: 20px;
        font-size: 1.3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SELECTOR DE REGIÓN (SIDEBAR) ---
st.sidebar.title("🌐 REGIÓN")
region = st.sidebar.selectbox("Ubicación del Inversor:", ["🇦🇷 Argentina", "🇺🇸 United States / International"])

# --- 4. CARTELES DINÁMICOS SEGÚN PAÍS ---
if region == "🇦🇷 Argentina":
    st.markdown("<div class='pay-banner'>🇦🇷 Si sos de Argentina tenes que pagar 2 millones por mes.</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='pay-banner'>🇺🇸 If you are from the United States etc, it costs 12 thousand per month.</div>", unsafe_allow_html=True)

st.title("🏛️ CENTRO DE MANDO LEGACY")

# 5. SIMULADOR
años = st.slider("AÑOS DE INVERSIÓN:", 1, 30, 10)
ret = st.slider("RENDIMIENTO ANUAL (%)", 5, 50, 15)

# CÁLCULOS MATEMÁTICOS
tc = 1500  # Cotización 2026
cap_usd = 12450000
futuro_usd = cap_usd * ((1 + (ret/100))**años)
futuro_ars = futuro_usd * tc 

st.markdown("---")

# 6. RESULTADOS SEGÚN REGIÓN
res1, res2 = st.columns(2)
if region == "🇦🇷 Argentina":
    res1.metric("PROYECCIÓN EN PESOS (ARS)", f"${futuro_ars:,.0f}")
    res2.metric("EQUIVALENTE EN DÓLARES (USD)", f"${futuro_usd:,.0f}")
else:
    res1.metric("PROYECCIÓN EN DÓLARES (USD)", f"${futuro_usd:,.0f}")
    res2.metric("VALOR EN PESOS (ARS)", f"${futuro_ars:,.0f}")

st.markdown("---")

# 7. GRÁFICOS Y IA (CORREGIDO)
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 DISTRIBUCIÓN")
    df_data = pd.DataFrame({"Activo": ["Casas", "Bolsa", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]})
    st.bar_chart(df_data.set_index("Activo"))
with c2:
    st.subheader("🤖 ESTRATEGA IA")
    pregunta = st.text_input("CONSULTA TÉCNICA:")
    if pregunta:
        st.write(f"🏛️ **IA:** Dylan García, para '{pregunta}' la orden es MANTENER.")
    st.download_button("📥 DESCARGAR AUDITORÍA", "VALOR: $12.45M USD", file_name="Reporte_Legacy.txt")

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.autenticado = False
    st.rerun()
