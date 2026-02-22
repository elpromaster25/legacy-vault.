import streamlit as st
import time

# --- 1. WHITELIST DE LOS 34 MISILES ---
VIP = ["EMAAR", "DAMAC", "NEOM", "GINEVRA", "REMAX", "SOTHEBYS", "THE AGENCY", "HINES", "JLL", "CARSO", "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS", "LEGACY", "DYLAN", "ADMIN", "TZIPINE", "DEMO"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []

# --- 2. DISEÑO CLÁSICO (SIN ERRORES) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 10px; }
    div.stButton > button { background-color: #d4af37 !important; color: #000 !important; width: 100%; font-weight: bold; height: 3.5em; }
    .btn-pay { background-color: #1a1a1a; color: #fff !important; padding: 12px; border-radius: 8px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 8px; border: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIN ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg = st.selectbox("🌐 SELECT REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        # BOTONES DE MAIL QUE SÍ ANDAN
        st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-pay" style="background:#d4af37; color:#000 !important;">⚡ SOLICITAR DEMO (5 MIN)</a>', unsafe_allow_html=True)
        if reg == "USA / GLOBAL":
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-pay">🔵 PAY WITH PAYPAL (EMAIL)</a>', unsafe_allow_html=True)
        else:
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-pay" style="background:#009ee3;">💳 MERCADO PAGO / DNI</a>', unsafe_allow_html=True)
        
        st.write("---")
        emp = st.text_input("COMPANY:").strip().upper()
        pw = st.text_input("KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT / ACCEDER"):
            if pw == "LEGACY2026" and (emp in VIP or emp == "DYLAN777"):
                st.session_state.emp_final = emp
                st.session_state.auth = True; st.rerun()
            else: st.error("DENEGADO.")
    st.stop()

# --- 4. INTERIOR TOTAL ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
if st.session_state.emp_final == "DYLAN777":
    with st.expander("🕵️‍♂️ RADAR"):
        for r in st.session_state.reg: st.info(r)

st.metric("REAL ESTATE ASSETS", "$85,000,000")
st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER")
act = st.text_area("LISTA DE ACTIVOS (FERRARIS, ETC):")
if st.button("🧬 SCAN"):
    if act:
        with st.spinner("..."): time.sleep(1); st.success("VALUACIÓN: $42,500,000 USD")

if st.sidebar.button("🔒 LOGOUT"): st.session_state.auth = False; st.rerun()
