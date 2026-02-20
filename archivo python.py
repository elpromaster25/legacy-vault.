import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE ESTADOS ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo' not in st.session_state: st.session_state.demo = False
if 'start_time' not in st.session_state: st.session_state.start_time = None

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | CHECKOUT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    .payment-box { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; margin: 10px; text-align: center; background: #1a1a1a; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        region = st.selectbox("🌎 ELIJA SU REGIÓN / SELECT REGION:", ["🇦🇷 Argentina", "🇺🇸 USA"], key="reg_init")
        st.write("---")
        st.markdown("<div class='gold-card'>🚀 AUDITORÍA TÉCNICA GRATUITA (5 MIN)</div>", unsafe_allow_html=True)
        if st.button("🚀 INICIAR DEMO GRATIS"):
            st.session_state.demo = True
            st.session_state.start_time = time.time()
            st.session_state.reg_final = region
            st.rerun()
        st.write("---")
        st.markdown("<div class='gold-card'>🔑 LLAVE MAESTRA PERMANENTE</div>", unsafe_allow_html=True)
        pw = st.text_input("PASSWORD:", type="password", key="login_pw")
        if st.button("🔓 DESBLOQUEAR ACCESO TOTAL"):
            if pw == "LEGACY2026":
                st.session_state.auth = True
                st.session_state.reg_final = region
                st.rerun()
            else: st.error("DENEGADO")
    st.stop()

# --- 4. MURO DE PAGO (CUANDO TERMINA LA DEMO) ---
if st.session_state.demo and not st.session_state.auth:
    restante = 300 - (time.time() - st.session_state.start_time)
    
    if restante <= 0:
        st.title("⌛ TIEMPO DE DEMO FINALIZADO")
        st.subheader(f"Para continuar operando, active su suscripción VIP")
        
        # MÉTODOS DE PAGO SEGÚN REGIÓN
        col1, col2 = st.columns(2)
        
        if st.session_state.reg_final == "🇦🇷 Argentina":
            with col1: st.markdown("<div class='payment-box'>💳 <b>MERCADO PAGO</b><br>Transferencia inmediata</div>", unsafe_allow_html=True)
            with col2: st.markdown("<div class='payment-box'>🏦 <b>CUENTA DNI</b><br>Pago QR / Clave DNI</div>", unsafe_allow_html=True)
            st.markdown("<h3 style='margin-top:20px;'>TOTAL: $2.000.000 ARS / MES</h3>", unsafe_allow_html=True)
        else:
            with col1: st.markdown("<div class='payment-box'>🔵 <b>PAYPAL</b><br>Credit Card / Global Balance</div>", unsafe_allow_html=True)
            with col2: st.markdown("<div class='payment-box'>🛡️ <b>STRIPE</b><br>Secure Payment Gateway</div>", unsafe_allow_html=True)
            st.markdown("<h3 style='margin-top:20px;'>TOTAL: $12.000 USD / MONTH</h3>", unsafe_allow_html=True)
        
        st.write("---")
        st.info("📩 Envíe comprobante a: dylanelpromaster25@gmail.com para recibir su LLAVE MAESTRA.")
        if st.button("⬅️ VOLVER AL INICIO"):
            st.session_state.demo = False
            st.rerun()
        st.stop()
    else:
        # CRONÓMETRO ACTIVO EN SIDEBAR
        st.sidebar.warning(f"⏳ CIERRE DE DEMO EN: {int(restante)} seg.")
        time.sleep(1)
        st.rerun()

# --- 5. COMMAND CENTER (INTERIOR) ---
st.title(f"🏛️ COMMAND CENTER - {st.session_state.reg_final}")
st.write("---")
# (Aquí sigue el resto de tu IA, Simulador y Exchange...)
st.metric("USD VALUE", "$12,450,000")
if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.session_state.demo = False
    st.rerun()
