import streamlit as st
import pandas as pd
import time

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="LEGACY QUANTUM VAULT", layout="wide")

# --- 2. LÓGICA DE SESIÓN (ESTADOS) ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo' not in st.session_state: st.session_state.demo = False
if 'start_time' not in st.session_state: st.session_state.start_time = None

# --- 3. DISEÑO IMPERIAL (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 30px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; font-weight: bold; }
    [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 4rem !important; font-weight: bold; }
    .gold-banner { border: 3px solid #d4af37; padding: 25px; text-align: center; color: #d4af37; margin-bottom: 30px; border-radius: 15px; font-size: 1.5rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANTALLA DE ENTRADA (EL FILTRO) ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    st.markdown("<div class='gold-banner'>🇦🇷 ARGENTINA: 2.000.000 ARS / MES<br>🇺🇸 USA: 12.000 USD / MONTH</div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔑 LLAVE MAESTRA (VIP)"):
            st.session_state.auth = "login_form"
            st.rerun()
    with c2:
        if st.button("🚀 DEMO GRATUITA (5 MIN)"):
            st.session_state.demo = True
            st.session_state.start_time = time.time()
            st.rerun()
    st.stop()

# --- 5. FORMULARIO DE LOGIN ---
if st.session_state.auth == "login_form":
    st.subheader("🔐 INGRESE LLAVE DE ACCESO")
    password = st.text_input("PASSWORD:", type="password")
    if st.button("DESBLOQUEAR"):
        if password == "LEGACY2026":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("LLAVE INVÁLIDA")
    st.stop()

# --- 6. CONTROL DEMO ---
if st.session_state.demo and not st.session_state.auth:
    if (time.time() - st.session_state.start_time) > 300:
        st.title("⌛ ACCESO EXPIRADO")
        st.markdown("<div class='gold-banner'>ADQUIERA SU LLAVE VIP: 2.000.000 ARS / 12K USD</div>", unsafe_allow_html=True)
        if st.button("VOLVER AL INICIO"):
            st.session_state.demo = False
            st.rerun()
        st.stop()

# --- 7. COMMAND CENTER (EL PRODUCTO COMPLETO) ---
st.title("🏛️ COMMAND CENTER LEGACY")
if st.session_state.demo:
    st.warning(f"⚠️ MODO DEMO: {int(300 - (time.time() - st.session_state.start_time))}s restantes")

# SIMULADOR GIGANTE
col_s1, col_s2 = st.columns(2)
años = col_s1.slider("PROYECCIÓN (AÑOS):", 1, 30, 10)
ret = col_s2.slider("RENTABILIDAD (%):", 5, 50, 15)
capital_base = 12450000
fut_usd = capital_base * ((1 + (ret/100))**años)

st.write("---")
m1, m2 = st.columns(2)
m1.metric("VALOR USD", f"${fut_usd:,.0f}")
m2.metric("VALOR ARS", f"${(fut_usd * 1500):,.0f}")

st.write("---")
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 ACTIVOS ESTRATÉGICOS")
    # GRÁFICO CON NÚMEROS CARGADOS (SIN ERROR)
    df = pd.DataFrame({"Activo": ["Propiedades", "Stocks", "Crypto", "Arte"], "Valor": [45, 25, 20, 10]})
    st.bar_chart(df.set_index("Activo"))

with c2:
    st.subheader("🤖 ESTRATEGA IA")
    # CUADRO DE TEXTO PARA QUE LA IA FUNCIONE
    pregunta = st.text_input("REALIZAR CONSULTA TÉCNICA:")
    if pregunta:
        with st.spinner('Analizando...'):
            time.sleep(1)
            st.write(f"🏛️ **IA:** Dylan García, para la consulta '{pregunta}' la orden estratégica es **MANTENER POSICIONES**.")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.session_state.demo = False
    st.rerun()
