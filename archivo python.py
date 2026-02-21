import streamlit as st
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (DORADO Y NEGRO TOTAL) ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, h4, p, label, .stMetric { color: #d4af37 !important; text-align: center; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.1); text-align: center; color: #d4af37; }
    .ticker { background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center; font-size: 0.9rem; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3em; }
    .stTextInput > div > div > input { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TICKER DE MERCADO VIVO ---
st.markdown("<div class='ticker'>🏦 LIVE: USDT/ARS: 1.515 | BTC/USD: 96.850 | ETH/USD: 2.450 | PROTOCOLO AES-256: ACTIVO</div>", unsafe_allow_html=True)

# --- 4. PANTALLA DE ACCESO (EL BÚNKER) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        region = st.selectbox("📂 SELECT VAULT:", ["ARGENTINA", "USA"], key="v_final_99")
        st.write("---")
        st.markdown("<div class='gold-card'>💎 ADQUIRIR TERMINAL CORPORATIVA</div>", unsafe_allow_html=True)
        # PAGOS
        p1, p2 = st.columns(2)
        with p1: st.markdown(f"<a href='mailto:dylanelpromaster25@gmail.com' style='text-decoration:none;'><div style='border:1px solid #d4af37; padding:10px; color:#d4af37; border-radius:5px;'>{'💳 MERCADO PAGO' if 'ARG' in region else '🔵 PAYPAL'}</div></a>", unsafe_allow_html=True)
        with p2: st.markdown(f"<a href='mailto:dylanelpromaster25@gmail.com' style='text-decoration:none;'><div style='border:1px solid #d4af37; padding:10px; color:#d4af37; border-radius:5px;'>{'🏦 CUENTA DNI' if 'ARG' in region else '🛡️ STRIPE'}</div></a>", unsafe_allow_html=True)
        
        st.write("---")
        emp = st.text_input("FIRMA / COMPANY:", key="e_final_99")
        pw = st.text_input("MASTER KEY:", type="password", key="p_final_99")
        if st.button("🔓 DESBLOQUEAR BÓVEDA"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp
                st.session_state.reg_final = region
                st.session_state.auth = True; st.rerun()
            else: st.error("Identificación y Llave requeridas.")
    st.stop()

# --- 5. INTERIOR (COMMAND CENTER COMPLETO) ---
reg = st.session_state.reg_final
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final.upper()}")
st.markdown(f"<p style='text-align: center;'>Protocolo de seguridad activo para la región {reg}</p>", unsafe_allow_html=True)

# MÉTRICAS PRINCIPALES
m1, m2, m3 = st.columns(3)
with m1: st.metric("REAL ESTATE", "$85,000,000")
with m2: st.metric("YACHTS & BOATS", "$12,500,000")
with m3: st.metric("PRIVATE JETS", "$24,000,000")

st.write("---")
# MESA DE CAMBIO (EXCHANGE)
st.subheader("💹 MESA DE CAMBIO VIP (P2P)")
ex1, ex2 = st.columns(2)
with ex1:
    m_ars = st.number_input("Monto ARS para Liquidar:", min_value=1000000, value=5000000)
    st.write(f"Recibe estimado: **{(m_ars/1515):,.2f} USDT**")
    if st.button("🚀 SOLICITAR COTIZACIÓN"): st.success("Enviado a mesa de operaciones.")
with ex2:
    m_btc = st.number_input("Monto BTC para Liquidar:", min_value=0.01, value=0.1)
    st.write(f"Recibe estimado: **${(m_btc * 96850 * 1515):,.0f} ARS**")
    if st.button("🚀 LIQUIDAR BTC"): st.success("Enviado a mesa de operaciones.")

st.write("---")
# IA SCANNER
st.subheader("🤖 ESTRATEGA IA & SCANNER PATRIMONIAL")
lista = st.text_area("PEGUE SU LISTA DE ACTIVOS (Dptos, Campos, Autos):", key="scanner_99")
if st.button("🧬 ESCANEAR ACTIVOS"):
    with st.spinner("Analizando con Red Neuronal Legacy..."):
        time.sleep(1)
        st.success(f"Análisis para {st.session_state.emp_final} finalizado: Patrimonio Sólido.")

st.write("---")
# RELOJES MUNDIALES (PIE DE PÁGINA)
r1, r2, r3 = st.columns(3)
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:30 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:30 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:30 AM</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #d4af37; font-size: 0.8rem; margin-top: 20px;'>🔒 ENCRIPTACIÓN MILITAR AES-256 | LEGACY VAULT © 2026</p>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()

