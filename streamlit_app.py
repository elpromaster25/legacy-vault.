import streamlit as st
import time

# --- 1. CONFIGURACIÓN DEL NODO ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")

# LISTA BLANCA (Empresas autorizadas)
VIP = ["EMAAR", "GINEVRA", "REMAX", "THE AGENCY", "LEGACY", "DYLAN", "ADMIN"]

# INICIALIZAR MEMORIA
if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'reg' not in st.session_state:
    st.session_state.reg = []

# --- 2. DISEÑO IMPERIAL ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESO RESTRINGIDO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        emp = st.text_input("FIRMA / COMPANY:").strip().upper()
        pw = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK"):
            if pw == "LEGACY2026" and emp in VIP:
                st.session_state.emp_final = emp
                st.session_state.reg.append(f"🟢 {emp} - {time.strftime('%H:%M')}")
                st.session_state.auth = True
                st.rerun()
            elif emp != "":
                st.error("ACCESO DENEGADO")
                st.session_state.reg.append(f"🔴 ERROR: {emp} - {time.strftime('%H:%M')}")
    st.stop()

# --- 4. INTERIOR DEL IMPERIO ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL: {emp}")

# MÉTRICAS CENTRADAS
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
        with st.status("Escaneando...", expanded=True) as s:
            time.sleep(1); s.update(label="Finalizado ✅", state="complete")
        st.markdown("<div class='gold-card'><h2>VALUACIÓN: $42,500,000 USD</h2></div>", unsafe_allow_html=True)

# ADMIN SIDEBAR
st.sidebar.markdown("### 🛡️ CONTROL")
if st.sidebar.text_input("PIN:", type="password") == "DYLAN777":
    for r in st.session_state.reg: st.sidebar.info(r)
if st.sidebar.button("🔒 EXIT"):
    st.session_state.auth = False
    st.rerun()
