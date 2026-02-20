import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'demo' not in st.session_state:
    st.session_state.demo = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# --- 2. DISEÑO IMPERIAL (CSS) ---
st.set_page_config(page_title="LEGACY QUANTUM VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 25px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; font-weight: bold; }
    [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 3.5rem !important; font-weight: bold; }
    
    .vip-banner { 
        background: linear-gradient(90deg, #b8860b, #d4af37, #f7e08b, #d4af37, #b8860b); 
        color: black !important; padding: 20px; text-align: center; 
        font-weight: bold; border-radius: 15px; margin-bottom: 25px; 
        font-size: 1.5rem; border: 2px solid #ffffff;
        box-shadow: 0px 0px 20px #d4af37;
    }
    
    .gold-border { border: 2px solid #d4af37; padding: 25px; border-radius: 20px; text-align: center; color: #d4af37; background-color: rgba(212, 175, 55, 0.05); }
    
    div.stButton > button {
        background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; 
        width: 100%; font-weight: bold; height: 3.5em; font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    st.markdown("<div class='gold-border'>💎 ACCESO VIP RESTRINGIDO<br>COSTO: 2.000.000 ARS / 12.000 USD</div>", unsafe_allow_html=True)
    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔑 INGRESAR CON LLAVE VIP"):
            st.session_state.auth = "login_form"
            st.rerun()
    with c2:
        if st.button("🚀 INICIAR DEMO TEMPORAL (5 MIN)"):
            st.session_state.demo = True
            st.session_state.start_time = time.time()
            st.rerun()
    st.stop()

# --- 4. LOGIN VIP ---
if st.session_state.auth == "login_form":
    st.subheader("🔐 VALIDACIÓN VIP")
    password = st.text_input("LLAVE MAESTRA:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("DENEGADO")
    st.stop()

# --- 5. CONTROL DEMO ---
if st.session_state.demo and not st.session_state.auth:
    elapsed = time.time() - st.session_state.start_time
    if elapsed > 300:
        st.title("⌛ TIEMPO EXPIRADO")
        st.markdown("<div class='vip-banner'>ADQUIERA SU ACCESO VIP PARA CONTINUAR</div>", unsafe_allow_html=True)
        if st.button("VOLVER"):
            st.session_state.demo = False
            st.rerun()
        st.stop()

# --- 6. COMMAND CENTER (TODO EL CONTENIDO) ---
if st.session_state.auth == True:
    st.markdown("<div class='vip-banner'>💎 ESTADO: ACCESO VIP TOTAL ACTIVADO | BIENVENIDO DYLAN GARCÍA</div>", unsafe_allow_html=True)

st.title("🏛️ COMMAND CENTER LEGACY")

if st.session_state.demo:
    st.warning(f"⚠️ MODO DEMO: {int(300 - (time.time() - st.session_state.start_time))}s restantes")

# SIMULADOR
años = st.slider("PROYECCIÓN (AÑOS):", 1, 30, 10)
ret = st.slider("RENTABILIDAD (%):", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)

st.write("---")
m1, m2 = st.columns(2)
m1.metric("VALOR USD", f"${fut_usd:,.0f}")
m2.metric("VALOR ARS", f"${(fut_usd * 1500):,.0f}")

st.write("---")
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 DISTRIBUCIÓN VIP")
    # --- ARREGLADO: LISTA CON NÚMEROS REALES ---
    df_assets = pd.DataFrame({
        "Activo": ["RE", "Stocks", "Crypto", "Art"],
        "Valor": [45, 30, 15, 10]
    })
    st.bar_chart(df_assets.set_index("Activo"))

with c2:
    st.subheader("🤖 IA VIP")
    pregunta = st.text_input("CONSULTA:")
    if pregunta:
        with st.spinner('Analizando...'):
            time.sleep(1)
            st.write(f"🏛️ **IA:** Dylan García, la orden estratégica es MANTENER POSICIONES.")

if st.sidebar.button("🔒 CERRAR"):
    st.session_state.auth = False
    st.session_state.demo = False
    st.rerun()
