import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE ESTADOS ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo' not in st.session_state: st.session_state.demo = False
if 'start_time' not in st.session_state: st.session_state.start_time = None

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    .payment-box { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; margin: 10px; text-align: center; background: #1a1a1a; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA (LIMPIEZA TOTAL) ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        # SELECTOR LIMPIO: "ARGENTINA" / "USA"
        v_sel = st.selectbox("📂 SELECT VAULT / SELECCIONAR BÓVEDA:", ["ARGENTINA", "USA"], key="vault_final_x88")
        st.write("---")
        
        st.markdown("<div class='gold-card'>🚀 AUDITORÍA TÉCNICA GRATUITA (5 MIN)</div>", unsafe_allow_html=True)
        if st.button("🚀 INICIAR DEMO GRATIS", key="btn_demo_x88"):
            st.session_state.demo = True
            st.session_state.start_time = time.time()
            st.session_state.reg_final = v_sel
            st.rerun()
            
        st.write("---")
        st.markdown("<div class='gold-card'>🔑 LLAVE MAESTRA PERMANENTE</div>", unsafe_allow_html=True)
        # CONTRASEÑA CON KEY ÚNICA PARA QUE NO SE MEZCLE NADA
        pw = st.text_input("MASTER KEY:", type="password", key="password_secure_x88")
        
        if st.button("🔓 DESBLOQUEAR", key="btn_unlock_x88"):
            if pw == "LEGACY2026":
                st.session_state.auth = True
                st.session_state.reg_final = v_sel
                st.rerun()
            else: st.error("DENEGADO / DENIED")
    st.stop()

# --- 4. MURO DE PAGO (POST-DEMO) ---
if st.session_state.demo and not st.session_state.auth:
    restante = 300 - (time.time() - st.session_state.start_time)
    if restante <= 0:
        st.title("⌛ TIEMPO DE DEMO FINALIZADO")
        st.subheader("Active su suscripción VIP para continuar")
        col1, col2 = st.columns(2)
        if "ARGENTINA" in st.session_state.reg_final:
            with col1: st.markdown("<div class='payment-box'>💳 <b>MERCADO PAGO</b></div>", unsafe_allow_html=True)
            with col2: st.markdown("<div class='payment-box'>🏦 <b>CUENTA DNI</b></div>", unsafe_allow_html=True)
            st.markdown("<h3>TOTAL: $2.000.000 ARS</h3>", unsafe_allow_html=True)
        else:
            with col1: st.markdown("<div class='payment-box'>🔵 <b>PAYPAL</b></div>", unsafe_allow_html=True)
            with col2: st.markdown("<div class='payment-box'>🛡️ <b>STRIPE</b></div>", unsafe_allow_html=True)
            st.markdown("<h3>TOTAL: $12.000 USD</h3>", unsafe_allow_html=True)
        st.info("📩 Envíe comprobante a: dylanelpromaster25@gmail.com")
        if st.button("⬅️ VOLVER", key="btn_back_x88"):
            st.session_state.demo = False
            st.rerun()
        st.stop()
    else:
        st.sidebar.warning(f"⏳ DEMO: {int(restante)} seg.")
        time.sleep(1)
        st.rerun()

# --- 5. INTERIOR (COMMAND CENTER) ---
st.title(f"🏛️ COMMAND CENTER - {st.session_state.reg_final}")
st.write("---")
# Simulador de Fortuna
st.metric("USD VALUE", "$12,450,000")
st.write("---")
# IA Estratégica
st.subheader("🤖 ESTRATEGA IA")
q = st.text_input("CONSULTA:", key="ia_query_x88")
if q: st.write("🏛️ **IA:** Dylan García, la orden es MANTENER POSICIONES.")

if st.sidebar.button("🔒 SALIR", key="btn_exit_x88"):
    st.session_state.auth = False
    st.session_state.demo = False
    st.rerun()
