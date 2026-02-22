import streamlit as st
import time

# --- 1. WHITELIST ---
VIP = ["EMAAR", "DAMAC", "NEOM", "GINEVRA", "REMAX", "SOTHEBYS", "THE AGENCY", "HINES", "JLL", "CARSO", "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS", "LEGACY", "DYLAN", "ADMIN", "TZIPINE"]

if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (TEXTO FORZADO + SIN FLECHA) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    [data-testid="collapsedControl"], [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
    .stApp { background-color: #000; border: 2px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    button p { color: #000000 !important; font-weight: bold !important; font-size: 1.1rem !important; }
    div.stButton > button { background-color: #d4af37 !important; width: 100% !important; height: 3.5em !important; border-radius: 8px !important; }
    .btn-pay { background-color: #1a1a1a; color: #ffffff !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg = st.selectbox("🌐 REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        if reg == "USA / GLOBAL":
            st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com" class="btn-pay">🔵 PAYPAL ACCESS (EMAIL)</a>', unsafe_allow_html=True)
        else:
            st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com" class="btn-pay" style="background:#009ee3;">💳 PAGO MP / DNI (EMAIL)</a>', unsafe_allow_html=True)
        st.write("---")
        emp = st.text_input("COMPANY:").strip().upper()
        pw = st.text_input("KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT / ACCEDER"):
            if pw == "LEGACY2026" and (emp in VIP or emp == "DYLAN777"):
                st.session_state.emp_final = emp
                st.session_state.auth = True; st.rerun()
            else: st.error("DENEGADO.")
    st.stop()

# --- 4. INTERIOR TOTAL (EL IMPERIO) ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
st.metric("REAL ESTATE ASSETS", "$85,000,000")

st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER")
act = st.text_area("LISTA DE ACTIVOS (FERRARIS, YATES, PROPIEDADES):")
if st.button("🧬 INICIAR ESCANEO"):
    if act:
        with st.spinner("..."): time.sleep(1)
        st.success("VALUACIÓN DETECTADA: $42,500,000 USD")

st.write("---")
st.subheader("🤖 IA STRATEGIC ADVISOR")
if st.text_input("CONSULTA TÉCNICA:"):
    st.info("Estado: LIQUIDEZ ÓPTIMA.")

if st.button("🔒 LOGOUT"): st.session_state.auth = False; st.rerun()
