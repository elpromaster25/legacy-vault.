import streamlit as st
import pandas as pd
import time

# --- 1. SEGURIDAD DE ACCESO ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.set_page_config(page_title="ACCESO PRIVADO", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h1 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🔐 TERMINAL DE ACCESO PRIVADO")
    
    # LOGIN ÚNICO
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
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MODO ADMINISTRADOR (SIDEBAR) ---
st.sidebar.title("🛂 PANEL DE CONTROL")
es_admin = st.sidebar.checkbox("🔓 MODO ADMIN (DYLAN GARCÍA)")

if not es_admin:
    region = st.sidebar.selectbox("Ubicación del Inversor:", ["🇦🇷 Argentina", "🇺🇸 United States / International"])
else:
    st.sidebar.success("MODO MONITOR GLOBAL ACTIVO")

# --- 4. CARTELES DINÁMICOS (O TODOS SI ES ADMIN) ---
if es_admin:
    st.markdown("<div class='pay-banner'>🇦🇷 MODO ADMIN: Precio Arg 2M / Precio USA 12K USD</div>", unsafe_allow_html=True)
    st.markdown("<div class='pay-banner'>🇺🇸 ADMIN VIEW: All regions visible</div>", unsafe_allow_html=True)
else:
    if region == "🇦🇷 Argentina":
        st.markdown("<div class='pay-banner'>🇦🇷 Si sos de Argentina tenes que pagar 2 millones por mes.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='pay-banner'>🇺🇸 If you are from the United States etc, it costs 12 thousand per month.</div>", unsafe_allow_html=True)

st.title("🏛️ CENTRO DE MANDO LEGACY")

# 5. SIMULADOR
años = st.slider("AÑOS DE INVERSIÓN:", 1, 30, 10)
ret = st.slider("RENDIMIENTO ANUAL (%)", 5, 50, 15)

# CÁLCULOS
tc = 1500 
futuro_usd = 12450000 * ((1 + (ret/100))**años)
futuro_ars = futuro_usd * tc 

st.markdown("---")

# 6. RESULTADOS (Doble si es Admin)
if es_admin:
    r1, r2 = st.columns(2)
    r1.metric("GLOBAL USD", f"${futuro_usd:,.0f}")
    r2.metric("GLOBAL ARS", f"${futuro_ars:,.0f}")
else:
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
    st.subheader("🤖 IA ESTRATÉGICA")
    pregunta = st.text_input("CONSULTA TÉCNICA:")
    if pregunta:
        st.write(f"🏛️ **IA:** Dylan García, para '{pregunta}' la orden es MANTENER.")

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.autenticado = False
    st.rerun()
