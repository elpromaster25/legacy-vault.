import streamlit as st
import time

# --- 1. RESET Y CONFIGURACIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False

st.set_page_config(page_title="LEGACY | VAULT", layout="wide")
st.markdown("<style>.stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; } h1, h2, h3 { color: #d4af37 !important; text-align: center; }</style>", unsafe_allow_html=True)

# --- 2. PANTALLA DE ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    with col_ce:
        emp = st.text_input("FIRMA / COMPANY:", key="e_final")
        pw = st.text_input("MASTER KEY:", type="password", key="p_final")
        if st.button("🔓 DESBLOQUEAR"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp
                st.session_state.auth = True
                st.rerun()
            else: st.error("Datos obligatorios.")
    st.stop()

# --- 3. INTERIOR (EL PRODUCTO) ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final.upper()}")
st.write("---")
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85M")
with c2: st.metric("YACHTS", "$12.5M")
with c3: st.metric("JETS", "$24M")
st.write("---")
st.subheader("🤖 ESTRATEGA IA")
st.info(f"Análisis activo para {st.session_state.emp_final}.")
if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
