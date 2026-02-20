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
    st.stop()

# --- 2. CONFIGURACIÓN DE ÉLITE ---
st.set_page_config(page_title="LEGACY VAULT", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.2rem !important; font-weight: bold; }
    .pay-banner { background-color: rgba(212, 175, 55, 0.1); border: 2px solid #d4af37; color: #d4af37; padding: 15px; text-align: center; font-weight: bold; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANEL DE CONTROL (TRADUCCIÓN) ---
st.sidebar.title("🛂 PANEL / DASHBOARD")
es_admin = st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN)")

if not es_admin:
    idioma = st.sidebar.selectbox("Region:", ["🇦🇷 Argentina (Español)", "🇺🇸 USA / International (English)"])
else:
    idioma = "Admin"

# --- 4. TEXTOS DINÁMICOS SEGÚN IDIOMA ---
texts = {
    "🇦🇷 Argentina (Español)": {
        "banner": "🇦🇷 Si sos de Argentina tenes que pagar 2 millones por mes.",
        "titulo": "🏛️ CENTRO DE MANDO LEGACY",
        "sim_titulo": "🚀 PROYECCIÓN DE FORTUNA",
        "anios": "AÑOS DE INVERSIÓN:",
        "retorno": "RETORNO ANUAL (%):",
        "res1": "PROYECCIÓN EN PESOS (ARS)",
        "res2": "EQUIVALENTE EN USD",
        "dist": "📊 DISTRIBUCIÓN DE ACTIVOS",
        "ia": "🤖 IA ESTRATÉGICA",
        "pregunta": "CONSULTA TÉCNICA:",
        "boton_aud": "📥 DESCARGAR AUDITORÍA",
        "logout": "🔒 CERRAR"
    },
    "🇺🇸 USA / International (English)": {
        "banner": "🇺🇸 If you are from the United States etc, it costs 12 thousand per month.",
        "titulo": "🏛️ LEGACY COMMAND CENTER",
        "sim_titulo": "🚀 WEALTH PROJECTION",
        "anios": "INVESTMENT YEARS:",
        "retorno": "ANNUAL RETURN (%):",
        "res1": "PROJECTION IN DOLLARS (USD)",
        "res2": "VALUE IN PESOS (ARS)",
        "dist": "📊 ASSET DISTRIBUTION",
        "ia": "🤖 STRATEGIC AI",
        "pregunta": "TECHNICAL CONSULTATION:",
        "boton_aud": "📥 DOWNLOAD AUDIT",
        "logout": "🔒 LOGOUT"
    },
    "Admin": {
        "banner": "💎 GLOBAL ADMIN MODE: 2M ARS / 12K USD",
        "titulo": "🏛️ LEGACY MASTER TERMINAL",
        "sim_titulo": "🚀 GLOBAL PROJECTION CONTROL",
        "anios": "YEARS:",
        "retorno": "RETURN %:",
        "res1": "TOTAL USD",
        "res2": "TOTAL ARS",
        "dist": "📊 GLOBAL ASSETS",
        "ia": "🤖 MASTER AI",
        "pregunta": "ADMIN INPUT:",
        "boton_aud": "📥 EXPORT MASTER DATA",
        "logout": "🔒 EXIT"
    }
}

t = texts[idioma]

# --- 5. INTERFAZ DINÁMICA ---
st.markdown(f"<div class='pay-banner'>{t['banner']}</div>", unsafe_allow_html=True)
st.title(t["titulo"])

# SIMULADOR
st.subheader(t["sim_titulo"])
col_s1, col_s2 = st.columns(2)
with col_s1:
    años = st.slider(t["anios"], 1, 30, 10)
with col_s2:
    ret = st.slider(t["retorno"], 5, 50, 15)

# CÁLCULOS
tc = 1500 
futuro_usd = 12450000 * ((1 + (ret/100))**años)
futuro_ars = futuro_usd * tc 

st.markdown("---")
res1, res2 = st.columns(2)
res1.metric(t["res1"], f"${futuro_usd:,.0f}" if "USD" in t["res1"] else f"${futuro_ars:,.0f}")
res2.metric(t["res2"], f"${futuro_ars:,.0f}" if "ARS" in t["res2"] else f"${futuro_usd:,.0f}")

st.markdown("---")

# 6. GRÁFICOS Y IA
c1, c2 = st.columns(2)
with c1:
    st.subheader(t["dist"])
    df_data = pd.DataFrame({"Activo": ["Propiedades", "Stocks", "Crypto", "Arte"], "Valor":})
    st.bar_chart(df_data.set_index("Activo"))
with c2:
    st.subheader(t["ia"])
    preg = st.text_input(t["pregunta"])
    if preg:
        st.write(f"🏛️ **AI:** Dylan García, recommendation for '{preg}': HOLD.")
    st.download_button(t["boton_aud"], f"VALUE: {futuro_usd} USD", file_name="Legacy_Audit.txt")

if st.sidebar.button(t["logout"]):
    st.session_state.autenticado = False
    st.rerun()
