import streamlit as st
import time

# --- 1. WHITELIST DE LOS 34 GIGANTES ---
VIP = ["EMAAR", "DAMAC", "NEOM", "GINEVRA", "REMAX", "SOTHEBYS", "THE AGENCY", "HINES", "JLL", "CARSO", "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS", "LEGACY", "DYLAN", "ADMIN", "TZIPINE"]

if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (SIN FLECHA + TICKER + TEXTO FORZADO) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    [data-testid="collapsedControl"], [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
    .stApp { background-color: #000; border: 2px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .ticker-wrap { width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    button p { color: #000000 !important; font-weight: bold !important; font-size: 1.1rem !important; }
    div.stButton > button { background-color: #d4af37 !important; width: 100% !important; height: 3.5em !important; border-radius: 8px !important; }
    .btn-pay { background-color: #1a1a1a; color: #ffffff !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIN ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg = st.selectbox("🌐 REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        if reg == "USA / GLOBAL":
            st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com" class="btn-pay">🔵 PAY WITH PAYPAL (EMAIL)</a>', unsafe_allow_html=True)
        else:
            st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com" class="btn-pay" style="background:#009ee3; border-color:#fff;">💳 PAGO MP / DNI (EMAIL)</a>', unsafe_allow_html=True)
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
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL: {emp}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | NODE: {emp} | VALUATION: $85,000,000 🏛️</div></div>', unsafe_allow_html=True)

st.metric("REAL ESTATE ASSETS", "$85,000,000")

st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER")
activos = st.text_area("LISTA DE ACTIVOS (FERRARIS, YATES, PROPIEDADES):", key="sc_input")
if st.button("🧬 INICIAR ESCANEO"):
    if activos:
        with st.spinner("Analizando activos..."):
            time.sleep(1.5)
            st.markdown(f"<div style='border:1px solid #d4af37; padding:15px; border-radius:10px; background:rgba(212,175,55,0.05); text-align:center;'><h2>VALUACIÓN DETECTADA: $42,500,000 USD</h2></div>", unsafe_allow_html=True)
    else: st.warning("Por favor, ingrese una lista de activos.")

st.write("---")
st.subheader("🤖 IA STRATEGIC ADVISOR")
pregunta = st.text_input("CONSULTA TÉCNICA A LA IA:", key="ia_input")
if pregunta:
    with st.spinner("Procesando..."):
        time.sleep(1)
        st.success(f"🏛️ ADVISOR: Análisis completado para {emp}. Estado: SOLVENTE. Riesgo: MÍNIMO.")

if st.button("🔒 LOGOUT"): st.session_state.auth = False; st.rerun()
