import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE ESTADOS ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo' not in st.session_state: st.session_state.demo = False

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    .ticker { background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TICKER DE MERCADO ---
st.markdown("<div class='ticker'>🏦 LIVE: USD/ARS: 1.515 | BTC/USD: 96.850 | AES-256 ENCRYPTION: ACTIVE</div>", unsafe_allow_html=True)

# --- 4. PANTALLA DE ENTRADA (SISTEMA ANTI-BUG) ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        v_sel = st.selectbox("📂 SELECT VAULT:", ["ARGENTINA", "USA"], key="v_secure_fix_99")
        st.write("---")
        st.markdown("<div class='gold-card'>🚀 AUDITORÍA GRATUITA (5 MIN)</div>", unsafe_allow_html=True)
        if st.button("🚀 INICIAR DEMO", key="btn_demo_fix_99"):
            st.session_state.demo = True
            st.session_state.reg_final = v_sel
            st.session_state.start_time = time.time()
            st.rerun()
        st.write("---")
        st.markdown("<div class='gold-card'>🔑 LLAVE MAESTRA</div>", unsafe_allow_html=True)
        pw = st.text_input("MASTER KEY:", type="password", key="pw_secure_fix_99")
        if st.button("🔓 DESBLOQUEAR", key="btn_unlock_fix_99"):
            if pw == "LEGACY2026":
                st.session_state.auth = True
                st.session_state.reg_final = v_sel
                st.rerun()
            else: st.error("DENEGADO")
    st.stop()

# --- 5. MURO DE PAGO (SOLO SI EXPIRA) ---
if st.session_state.demo and not st.session_state.auth:
    if (time.time() - st.session_state.start_time) > 300:
        st.title("⌛ DEMO FINALIZADA")
        st.markdown(f"<div class='gold-card'>ACTIVATE VIP: {'2.000.000 ARS' if 'ARG' in st.session_state.reg_final else '12.000 USD'}</div>", unsafe_allow_html=True)
        st.info("📩 dylanelpromaster25@gmail.com")
        if st.button("⬅️ VOLVER"): st.session_state.demo = False; st.rerun()
        st.stop()

# --- 6. INTERIOR (EL IMPERIO RESTAURADO) ---
st.title(f"🏛️ COMMAND CENTER - {st.session_state.reg_final}")
if st.session_state.demo: st.sidebar.warning(f"⏳ DEMO ACTIVA: {int(300 - (time.time() - st.session_state.start_time))}s")

# MÉTRICAS
c1, c2 = st.columns(2)
c1.metric("FORTUNA USD", "$12,450,000")
if "ARG" in st.session_state.reg_final: c2.metric("FORTUNA ARS", "$18.799.500.000")

st.write("---")
# EXCHANGE P2P
st.subheader("💹 MESA DE CAMBIO VIP (LIQUIDACIÓN)")
col_ex1, col_ex2 = st.columns(2)
with col_ex1:
    m_ars = st.number_input("Monto ARS:", min_value=1000000, value=5000000)
    st.write(f"Recibe: **{(m_ars/1515):,.2f} USDT**")
    if st.button("🚀 COTIZAR ARS"): st.success("Solicitud enviada a la mesa de operaciones.")
with col_ex2:
    m_btc = st.number_input("Monto BTC:", min_value=0.01, value=0.1)
    st.write(f"Recibe: **${(m_btc * 96850 * 1515):,.0f} ARS**")
    if st.button("🚀 LIQUIDAR BTC"): st.success("Solicitud enviada.")

st.write("---")
# IA ADVISOR
st.subheader("🤖 ESTRATEGA IA: WALL STREET ADVISOR")
q = st.text_input("CONSULTA TÉCNICA:", key="ia_fix_99")
if q: st.write(f"🏛️ **IA:** Dylan García, para '{q}' la orden es MANTENER POSICIONES.")

st.write("---")
# RELOJES MUNDIALES (PIE DE PÁGINA)
c_t1, c_t2, c_t3 = st.columns(3)
with c_t1: st.markdown("<div class='gold-card'>🗽 NY: 11:51 AM</div>", unsafe_allow_html=True)
with c_t2: st.markdown("<div class='gold-card'>🏢 BA: 13:51 PM</div>", unsafe_allow_html=True)
with c_t3: st.markdown("<div class='gold-card'>🏰 LN: 16:51 PM</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #d4af37; font-size: 0.8rem;'>🔒 ENCRIPTACIÓN AES-256 | LEGACY VAULT © 2026</p>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.session_state.demo = False; st.rerun()
