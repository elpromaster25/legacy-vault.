import streamlit as st
import time

# --- 1. WHITELIST ---
VIP = ["EMAAR", "DAMAC", "NEOM", "GINEVRA", "REMAX", "SOTHEBYS", "THE AGENCY", "HINES", "JLL", "CARSO", "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS", "LEGACY", "DYLAN", "ADMIN", "TZIPINE"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []

# --- 2. DISEÑO SEGURO (DORADO) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide")
st.markdown("<style>.stApp { background-color: #000; border: 5px solid #d4af37; } h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }</style>", unsafe_allow_html=True)

# --- 3. ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg = st.selectbox("🌐 REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        if reg == "USA / GLOBAL":
            st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com" style="color:#d4af37; text-decoration:none; display:block; text-align:center; padding:10px; border:1px solid #d4af37; border-radius:5px;">🔵 PAYPAL ACCESS (EMAIL)</a>', unsafe_allow_html=True)
        else:
            st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com" style="color:#009ee3; text-decoration:none; display:block; text-align:center; padding:10px; border:1px solid #009ee3; border-radius:5px;">💳 MP / DNI (EMAIL)</a>', unsafe_allow_html=True)
        
        st.write("---")
        emp = st.text_input("COMPANY:").strip().upper()
        pw = st.text_input("KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT"):
            if pw == "LEGACY2026" and (emp in VIP or emp == "DYLAN777"):
                st.session_state.emp_final = emp
                st.session_state.auth = True; st.rerun()
            else: st.error("DENEGADO")
    st.stop()

# --- 4. INTERIOR ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
if st.session_state.emp_final == "DYLAN777":
    with st.expander("🕵️‍♂️ RADAR"):
        for r in st.session_state.reg: st.info(r)

st.metric("REAL ESTATE ASSETS", "$85,000,000")
st.subheader("🧬 SCANNER")
if st.button("🧬 SCAN"):
    with st.spinner("..."): time.sleep(1); st.success("VALUACIÓN: $42,500,000 USD")
