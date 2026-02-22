import streamlit st
import time

# --- 1. WHITELIST DE LOS 34 GIGANTES ---
VIP = ["EMAAR", "DAMAC", "NEOM", "GINEVRA", "REMAX", "SOTHEBYS", "THE AGENCY", "HINES", "JLL", "CARSO", "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS", "LEGACY", "DYLAN", "ADMIN", "TZIPINE"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []

# --- 2. DISEÑO IMPERIAL (MATA FLECHA + ORO TOTAL) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    [data-testid="collapsedControl"], [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    .stApp { background-color: #000; border: 2px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 20px; }
    .ticker-wrap { width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    .btn-pay { background-color: #1a1a1a; color: #ffffff !important; padding: 12px; border-radius: 8px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 8px; border: 1px solid #d4af37; }
    div.stButton > button { background-color: #d4af37 !important; color: #000 !important; width: 100% !important; font-weight: bold !important; height: 3.5em !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIN ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 SELECT REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        if reg_sel == "USA / GLOBAL":
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-pay">🔵 PAY WITH PAYPAL (EMAIL)</a>', unsafe_allow_html=True)
        else:
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-pay" style="background:#009ee3; border-color:#fff;">💳 PAGO MERCADO PAGO / DNI</a>', unsafe_allow_html=True)
        st.write("---")
        emp = st.text_input("COMPANY / FIRMA:").strip().upper()
        pw = st.text_input("KEY / CLAVE:", type="password")
        if st.button("🔓 UNLOCK VAULT / ACCEDER"):
            if pw == "LEGACY2026" and (emp in VIP or emp == "DYLAN777"):
                st.session_state.emp_final = emp
                if emp != "DYLAN777": st.session_state.reg.append(f"🟢 {emp} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            elif emp != "":
                st.error("🚫 DENEGADO. Contact support: dylanelpromaster25@gmail.com")
                st.session_state.reg.append(f"🔴 ERROR: {emp} - {time.strftime('%H:%M')}")
    st.stop()

# --- 4. INTERIOR (RESTAURADO AL 100%) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL: {emp}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | NODE: {emp} 🏛️</div></div>', unsafe_allow_html=True)

if emp == "DYLAN777":
    with st.expander("🕵️‍♂️ RADAR (SOLO FOUNDER)"):
        for r in st.session_state.reg: st.info(r)

c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85,000,000")
with c2: st.metric("YACHTS", "$12,500,000")
with c3: st.metric("PRIVATE JETS", "$24,000,000")

st.write("---")
st.subheader("🤖 IA STRATEGIC ADVISOR")
q = st.text_input("CONSULTA A LA IA:")
if q:
    with st.spinner("Analizando..."): time.sleep(1); st.success(f"Análisis completado para {emp}. Estado: ÓPTIMO.")

st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER")
act = st.text_area("LISTA DE ACTIVOS:", key="sc_final")
if st.button("🧬 INICIAR ESCANEO"):
    if act:
        with st.spinner("Escaneando..."): time.sleep(1.5); st.markdown(f"<div class='gold-card'><h2>VALUACIÓN: $42,500,000 USD</h2></div>", unsafe_allow_html=True)

# RELOJES
st.write("---")
_, r1, r2, r3, _ = st.columns(5)
with r1: st.write("🗽 NY: 07:30 PM")
with r2: st.write("🏢 BA: 09:30 PM")
with r3: st.write("🏰 LN: 12:30 AM")

if st.button("🔒 LOGOUT"): st.session_state.auth = False; st.rerun()
