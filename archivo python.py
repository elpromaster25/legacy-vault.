import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo' not in st.session_state: st.session_state.demo = False
if 'start_time' not in st.session_state: st.session_state.start_time = None
if 'mensajes' not in st.session_state: st.session_state.mensajes = []

# --- 2. ESTILO DORADO MAXIMIZADO ---
st.set_page_config(page_title="LEGACY QUANTUM VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 3.5rem !important; font-weight: bold; }
    .gold-box { border: 2px solid #d4af37; padding: 20px; text-align: center; color: #d4af37; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    st.markdown("<div class='gold-box'>🇦🇷 ARGENTINA: 2.000.000 ARS / MES<br>🇺🇸 USA: 12.000 USD / MONTH</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔑 LLAVE MAESTRA"): st.session_state.auth = "login_form"; st.rerun()
    with c2:
        if st.button("🚀 DEMO GRATUITA"): st.session_state.demo = True; st.session_state.start_time = time.time(); st.rerun()
    st.stop()

# --- 4. LOGIN ---
if st.session_state.auth == "login_form":
    st.subheader("🔐 INGRESE LLAVE MAESTRA")
    password = st.text_input("PASSWORD:", type="password")
    if st.button("DESBLOQUEAR"):
        if password == "LEGACY2026": st.session_state.auth = True; st.rerun()
        else: st.error("DENEGADO")
    st.stop()

# --- 5. CONTROL DEMO ---
if st.session_state.demo and not st.session_state.auth:
    if (time.time() - st.session_state.start_time) > 300:
        st.title("⌛ TIEMPO EXPIRADO")
        st.markdown("<div class='gold-box'>ADQUIERA SU LLAVE VIP: 2.000.000 ARS / 12K USD</div>", unsafe_allow_html=True)
        if st.button("INICIO"): st.session_state.demo = False; st.rerun()
        st.stop()

# --- 6. COMMAND CENTER (TODO EL CONTENIDO) ---
st.title("🏛️ COMMAND CENTER LEGACY")
if st.session_state.demo: st.warning(f"⚠️ MODO DEMO: {int(300 - (time.time() - st.session_state.start_time))}s")

# SIMULADOR COMPLETO
col_s1, col_s2 = st.columns(2)
años = col_s1.slider("PROYECCIÓN (AÑOS):", 1, 30, 10)
ret = col_s2.slider("RENTABILIDAD (%):", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)

st.write("---")
m1, m2 = st.columns(2)
m1.metric("VALOR USD", f"${fut_usd:,.0f}")
m2.metric("VALOR ARS", f"${(fut_usd * 1500):,.0f}")

st.write("---")
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 ACTIVOS ESTRATÉGICOS")
    df = pd.DataFrame({"Activo": ["Propiedades", "Stocks", "Crypto", "Arte"], "Valor": [45, 25, 20, 10]})
    st.bar_chart(df.set_index("Activo"))

with c2:
    st.subheader("🤖 IA ADVISOR VIP")
    pregunta = st.text_input("CONSULTA TÉCNICA:")
    if pregunta:
        with st.spinner('Analizando...'):
            time.sleep(1)
            st.write(f"🏛️ **IA:** Dylan García, para '{pregunta}' la orden es MANTENER POSICIONES.")

# MODO ADMIN EN SIDEBAR
if st.sidebar.checkbox("🔓 MODO ADMIN"):
    st.sidebar.write("📬 Mensajes recibidos:")
    st.sidebar.info("Esperando nuevos interesados...")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False; st.session_state.demo = False; st.rerun()
