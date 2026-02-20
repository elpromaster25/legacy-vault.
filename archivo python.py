import streamlit as st
import pandas as pd
import time

# --- LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'mensajes' not in st.session_state: st.session_state.mensajes = []

# --- DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | EXCHANGE", layout="wide")
st.markdown("<style>.stApp { background-color: #000000; border: 6px solid #d4af37; padding: 25px; } h1, h2, h3 { color: #d4af37 !important; text-align: center; } .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }</style>", unsafe_allow_html=True)

# --- TICKER EN VIVO ---
st.markdown("<div style='background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center;'>🏦 EXCHANGE VIVO | USDT/ARS: 1.515 | BTC/USD: 96.800 | FEE: 1.5% VIP</div>", unsafe_allow_html=True)

# (Aquí iría tu pantalla de entrada que ya tenemos...)
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    with col_ce:
        st.markdown("<div class='gold-card'>💎 ACCESO RESTRINGIDO<br>LLAVE MAESTRA REQUERIDA</div>", unsafe_allow_html=True)
        pw = st.text_input("PASSWORD:", type="password")
        if st.button("DESBLOQUEAR"):
            if pw == "LEGACY2026": st.session_state.auth = True; st.rerun()
    st.stop()

# --- COMMAND CENTER CON EXCHANGE ---
st.title("🏛️ COMMAND CENTER & EXCHANGE")

# NUEVA SECCIÓN: MESA DE CAMBIO (LO QUE DIJO TU PAPÁ)
st.write("---")
st.subheader("💹 MESA DE CAMBIO VIP (P2P)")
col_ex1, col_ex2 = st.columns(2)

with col_ex1:
    st.markdown("<div class='gold-card'>💰 VENDER PESOS (ARS)</div>", unsafe_allow_html=True)
    monto_ars = st.number_input("Cantidad de Pesos:", min_value=1000000, value=2000000, step=500000)
    recibe_usdt = monto_ars / 1515
    st.metric("RECIBE USDT (DIGITAL DOLLAR)", f"{recibe_usdt:,.2f}")

with col_ex2:
    st.markdown("<div class='gold-card'>₿ VENDER BITCOIN (BTC)</div>", unsafe_allow_html=True)
    monto_btc = st.number_input("Cantidad de BTC:", min_value=0.01, value=0.10, step=0.01)
    recibe_ars = monto_btc * 96800 * 1515
    st.metric("RECIBE PESOS (ARS)", f"${recibe_ars:,.0f}")

if st.button("🚀 SOLICITAR OPERACIÓN E INSTRUCCIONES DE DEPÓSITO"):
    # Esto te llega a vos al Modo Admin
    st.session_state.mensajes.append({"mail": "CLIENTE VIP", "nota": f"QUIERE CAMBIAR: {monto_ars} ARS", "hora": time.strftime('%H:%M')})
    st.success("✅ Solicitud enviada a la mesa de Dylan García. Un operador lo contactará para la liquidación.")

st.write("---")
# (Acá sigue tu simulador y la IA abajo...)
st.subheader("🤖 ESTRATEGA IA")
q = st.text_input("CONSULTA:")
if q: st.write("🏛️ **IA:** Analizando mercado... Orden: COMPRAR USDT.")

# MODO ADMIN
if st.sidebar.checkbox("🔓 MODO ADMIN"):
    if st.sidebar.text_input("CLAVE:", type="password") == "DYLAN777":
        if st.session_state.mensajes: st.sidebar.table(pd.DataFrame(st.session_state.mensajes))
