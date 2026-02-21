import streamlit as st
import time

# --- 1. RESET ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (DORADO Y NEGRO) ---
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

# --- 3. TICKER ---
st.markdown("<div class='ticker'>🏦 LIVE: USDT/ARS: 1.515 | BTC/USD: 96.850 | PROTOCOLO AES-256: ACTIVO</div>", unsafe_allow_html=True)

# --- 4. ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        region = st.selectbox("📂 SELECT VAULT:", ["ARGENTINA", "USA"], key="v_99")
        st.write("---")
        st.markdown("<div class='gold-card'>💎 ADQUIRIR TERMINAL CORPORATIVA</div>", unsafe_allow_html=True)
        st.write("---")
        emp = st.text_input("FIRMA / COMPANY:", key="e_99")
        pw = st.text_input("MASTER KEY:", type="password", key="p_99")
        if st.button("🔓 DESBLOQUEAR BÓVEDA"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp
                st.session_state.reg_final = region
                st.session_state.auth = True
                st.rerun()
            else: st.error("Identificación requerida.")
    st.stop()

# --- 5. INTERIOR ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final.upper()}")
m1, m2, m3 = st.columns(3)
with m1: st.metric("REAL ESTATE", "$85,000,000")
with m2: st.metric("YACHTS", "$12,500,000")
with m3: st.metric("PRIVATE JETS", "$24,000,000")

st.write("---")
st.subheader("🤖 IA SCANNER")
lista = st.text_area("LISTA DE ACTIVOS:", key="sc_99")
if st.button("🧬 ESCANEAR"):
    with st.spinner("Analizando..."):
        time.sleep(1)
        st.success(f"Análisis para {st.session_state.emp_final} completado.")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.rerun()
