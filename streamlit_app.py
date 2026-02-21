import streamlit as st
import time

# --- 1. MEMORIA DEL NODO (BLINDADA) ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []

# LISTA VIP
VIP = ["EMAAR", "REMAX", "THE AGENCY", "CARSO", "LEGACY", "DYLAN", "ADMIN"]

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("<style>.stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; } h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; } div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }</style>", unsafe_allow_html=True)

# --- 3. RADAR LATERAL (AISLADO) ---
with st.sidebar:
    st.markdown("### 🛡️ RADAR DE IMPACTO")
    # Usamos un FORM para que el botón de Admin NO refresque toda la página
    with st.form("admin_panel"):
        pin = st.text_input("ADMIN PIN:", type="password")
        check = st.form_submit_button("🛰️ SCAN NETWORK")
        if check and pin == "DYLAN777":
            st.success("BIENVENIDO FOUNDER.")
            if st.session_state.reg:
                for r in st.session_state.reg: st.info(r)
            else: st.warning("NODOS EN ESCUCHA...")
        elif check: st.error("PIN INVÁLIDO")
    
    if st.button("🔒 LOGOUT / SALIR"):
        st.session_state.auth = False
        st.rerun()

# --- 4. ACCESO AL BÚNKER ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.write("---")
        emp = st.text_input("COMPANY:").strip().upper()
        pw = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK"):
            if pw == "LEGACY2026" and emp in VIP:
                st.session_state.emp_final = emp
                st.session_state.reg.append(f"🟢 {emp} - {time.strftime('%H:%M')}")
                st.session_state.auth = True
                st.rerun()
            else: st.error("DENEGADO")
    st.stop()

# --- 5. INTERIOR ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
st.metric("REAL ESTATE", "$85,000,000")
st.write("---")
st.subheader("🧬 SCANNER DE ACTIVOS")
if st.button("🧬 INICIAR SCAN"):
    with st.status("Escaneando..."): time.sleep(1)
    st.success("VALUACIÓN: $42,500,000 USD")
