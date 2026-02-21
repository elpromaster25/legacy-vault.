import streamlit as st
import time

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")

# LISTA DE EMPRESAS AUTORIZADAS
VIP = ["EMAAR", "GINEVRA", "REMAX", "THE AGENCY", "LEGACY", "DYLAN", "ADMIN"]

# INICIALIZAR SESIÓN
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO</div>", unsafe_allow_html=True)
        emp = st.text_input("FIRMA / COMPANY:").strip().upper()
        pw = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK"):
            if pw == "LEGACY2026" and emp in VIP:
                st.session_state.emp_final = emp
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("ACCESO DENEGADO")
    st.stop()

# --- 4. INTERIOR ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")

# MÉTRICAS
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85M")
with c2: st.metric("YACHTS", "$12.5M")
with c3: st.metric("PRIVATE JETS", "$24M")

st.write("---")

# SCANNER
st.subheader("🧬 SCANNER DE ACTIVOS")
activos = st.text_area("LISTA DE PROPIEDADES:")
if st.button("🧬 SCAN"):
    if activos:
        st.markdown(f"<div class='gold-card'><h2>VALUACIÓN: $42,500,000 USD</h2></div>", unsafe_allow_html=True)

# SIDEBAR
if st.sidebar.button("🔒 EXIT"):
    st.session_state.auth = False
    st.rerun()
