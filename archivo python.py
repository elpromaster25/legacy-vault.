import streamlit as st
import pandas as pd
import time

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="LEGACY QUANTUM VAULT", page_icon="🏛️", layout="wide")

# --- 2. LÓGICA DE ACCESO (DEMO O LLAVE) ---
if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'demo' not in st.session_state:
    st.session_state.demo = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# --- 3. ESTILO DORADO ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 3rem !important; font-weight: bold; }
    .gold-box { border: 2px solid #d4af37; padding: 20px; border-radius: 10px; text-align: center; color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANTALLA DE ENTRADA ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔑 LLAVE MAESTRA (ADMIN/VIP)"):
            st.session_state.auth = "login"
            st.rerun()
    with c2:
        if st.button("🚀 DEMO GRATUITA (5 MINUTOS)"):
            st.session_state.demo = True
            st.session_state.start_time = time.time()
            st.rerun()
    
    st.write("---")
    st.markdown("<div class='gold-box'>🇦🇷 ARGENTINA: 2.000.000 ARS / MES<br>🇺🇸 USA: 12.000 USD / MONTH</div>", unsafe_allow_html=True)
    st.stop()

# --- 5. LOGIN ---
if st.session_state.auth == "login":
    st.subheader("🔐 INGRESE CREDENCIALES VIP")
    password = st.text_input("PASSWORD:", type="password")
    if st.button("DESBLOQUEAR"):
        if password == "LEGACY2026":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("DENEGADO")
    st.stop()

# --- 6. CONTROL DE TIEMPO DEMO ---
if st.session_state.demo and not st.session_state.auth:
    elapsed = time.time() - st.session_state.start_time
    if elapsed > 300:
        st.title("⌛ TIEMPO EXPIRADO")
        st.markdown("<div class='gold-box'>ADQUIERA SU LLAVE VIP PARA CONTINUAR<br>COSTO: 2 MILLONES ARS / 12K USD</div>", unsafe_allow_html=True)
        if st.button("VOLVER"):
            st.session_state.demo = False
            st.session_state.start_time = None
            st.rerun()
        st.stop()

# --- 7. PANEL DE CONTROL (EL PRODUCTO) ---
st.title("🏛️ COMMAND CENTER LEGACY")
if st.session_state.demo:
    st.warning(f"⚠️ MODO DEMO: {int(300 - (time.time() - st.session_state.start_time))}s restantes")

# SIMULADOR
años = st.slider("PROYECCIÓN (AÑOS):", 1, 30, 10)
ret = st.slider("RENTABILIDAD ANUAL (%):", 5, 50, 15)
capital = 12450000
futuro_usd = capital * ((1 + (ret/100))**años)

st.write("---")
m1, m2 = st.columns(2)
m1.metric("FORTUNA USD", f"${futuro_usd:,.0f}")
m2.metric("FORTUNA ARS", f"${(futuro_usd * 1500):,.0f}")

st.write("---")
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 ACTIVOS")
    df = pd.DataFrame({"Activo": ["Propiedades", "Stocks", "Crypto", "Art"], "Valor":})
    st.bar_chart(df.set_index("Activo"))
with c2:
    st.subheader("🤖 ESTRATEGA IA")
    q = st.text_input("CONSULTA TÉCNICA:")
    if q:
        st.write("🏛️ **IA:** Dylan García, la orden estratégica es MANTENER POSICIONES.")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.session_state.demo = False
    st.rerun()
