import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD DE BÓVEDA ---
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

# --- 3. PANEL DE CONTROL (ADMIN & TRADUCCIÓN) ---
st.sidebar.title("🛂 DASHBOARD CONTROL")
es_admin = st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN GARCÍA)")

if not es_admin:
    idioma = st.sidebar.selectbox("Region / Region:", ["🇦🇷 Argentina (Español)", "🇺🇸 USA / International (English)"])
else:
    idioma = "Admin"

# --- 4. DICCIONARIO DE TEXTOS ---
texts = {
    "🇦🇷 Argentina (Español)": {
        "banner": "🇦🇷 Si sos de Argentina tenes que pagar 2 millones por mes.",
        "titulo": "🏛️ CENTRO DE MANDO LEGACY",
        "res1": "PROYECCIÓN EN PESOS (ARS)",
        "res2": "EQUIVALENTE EN USD",
        "dist": "📊 DISTRIBUCIÓN DE ACTIVOS",
        "ia_sub": "🤖 IA ESTRATÉGICA VIP",
        "ia_q": "CONSULTA TÉCNICA A LA IA:",
        "ia_r": "IA: Estimado Dylan García, para esta consulta la orden es MANTENER.",
        "logout": "🔒 CERRAR SESIÓN"
    },
    "🇺🇸 USA / International (English)": {
        "banner": "🇺🇸 If you are from the United States etc, it costs 12 thousand per month.",
        "titulo": "🏛️ LEGACY COMMAND CENTER",
        "res1": "PROJECTION IN DOLLARS (USD)",
        "res2": "VALUE IN PESOS (ARS)",
        "dist": "📊 ASSET DISTRIBUTION",
        "ia_sub": "🤖 STRATEGIC AI VIP",
        "ia_q": "TECHNICAL CONSULTATION FOR AI:",
        "ia_r": "AI: Dear Dylan Garcia, for this query the order is to HOLD.",
        "logout": "🔒 LOGOUT"
    },
    "Admin": {
        "banner": "💎 MODO ADMIN GLOBAL: 2M ARS / 12K USD",
        "titulo": "🏛️ LEGACY MASTER TERMINAL",
        "res1": "TOTAL USD",
        "res2": "TOTAL ARS",
        "dist": "📊 GLOBAL ASSETS",
        "ia_sub": "🤖 MASTER AI ADVISOR",
        "ia_q": "ADMIN SYSTEM COMMAND:",
        "ia_r": "MASTER IA: All systems online. Capital is secured.",
        "logout": "🔒 EXIT TERMINAL"
    }
}

t = texts[idioma]

# --- 5. INTERFAZ DINÁMICA ---
st.markdown(f"<div class='pay-banner'>{t['banner']}</div>", unsafe_allow_html=True)
st.title(t["titulo"])

# SIMULADOR
años = st.slider("AÑOS / YEARS:", 1, 30, 10)
ret = st.slider("RETORNO / RETURN %:", 5, 50, 15)

# CÁLCULOS
tc = 1500 
cap_usd = 12450000
futuro_usd = cap_usd * ((1 + (ret/100))**años)
futuro_ars = futuro_usd * tc 

st.markdown("---")

# 6. RESULTADOS
res1, res2 = st.columns(2)
if "PESOS" in t["res1"] or "ARS" in t["res1"]:
    res1.metric(t["res1"], f"${futuro_ars:,.0f}")
    res2.metric(t["res2"], f"${futuro_usd:,.0f}")
else:
    res1.metric(t["res1"], f"${futuro_usd:,.0f}")
    res2.metric(t["res2"], f"${futuro_ars:,.0f}")

st.markdown("---")

# 7. GRÁFICOS Y IA (CONEXIÓN FINAL)
c1, c2 = st.columns(2)
with c1:
    st.subheader(t["dist"])
    # ARREGLADO: Valores del gráfico cerrados correctamente
    df_data = pd.DataFrame({"Activo": ["RE", "Stocks", "Crypto", "Art"], "Valor":})
    st.bar_chart(df_data.set_index("Activo"))

with c2:
    st.subheader(t["ia_sub"])
    user_query = st.text_input(t["ia_q"])
    if user_query:
        with st.spinner('Thinking / Analizando...'):
            time.sleep(1)
            st.write(f"🏛️ **{t['ia_r']}**")

# LOGOUT
if st.sidebar.button(t["logout"]):
    st.session_state.autenticado = False
    st.rerun()
