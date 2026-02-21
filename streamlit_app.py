import streamlit as st
import time

# --- 1. BASE DE DATOS DE LOS 34 MISILES (WHITELIST) ---
VIP = [
    "EMAAR", "DAMAC", "NAKHEEL", "AZIZI", "NEOM", 
    "GINEVRA", "REMAX", "SOTHEBYS", "NEST SEEKERS", "ALVEAR", 
    "THE AGENCY", "HINES", "JLL", "DOUGLAS ELLIMAN", "FORTUNE", 
    "CARSO", "ABILIA", "GICSA", "BE GRAND", "TERRA", 
    "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", 
    "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS", 
    "LEGACY", "DYLAN", "ADMIN", "TZIPINE", "USER", "GUEST"
]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []

# --- 2. DISEÑO IMPERIAL (MÁXIMO CONTRASTE) ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 20px; }
    .ticker-wrap { width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    
    /* BOTONES DE PAGO CON CONTRASTE */
    .btn-paypal { background-color: #0070ba; color: #ffffff !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #fff; }
    .btn-mp { background-color: #009ee3; color: #ffffff !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #fff; }
    .btn-dni { background-color: #004d40; color: #ffffff !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #fff; }
    
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. RADAR DE IMPACTO (SIDEBAR) ---
with st.sidebar:
    st.markdown("### 🛡️ CONTROL FUNDADOR")
    with st.form("admin_panel"):
        pin = st.text_input("ADMIN PIN:", type="password", key="p_adm")
        check = st.form_submit_button("🛰️ SCAN NETWORK")
        if check and pin == "DYLAN777":
            st.success("BIENVENIDO DYLAN.")
            if st.session_state.reg:
                for r in st.session_state.reg: st.info(r)
            else: st.warning("NODOS EN ESCUCHA...")
        elif check: st.error("PIN INVÁLIDO")
    if st.button("🔒 LOGOUT / SALIR"):
        st.session_state.auth = False; st.rerun()

# --- 4. ACCESO AL BÚNKER (USA/ARG) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 SELECT REGION / ELIJA REGIÓN:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        if reg_sel == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD**")
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-paypal">🔵 PAY WITH PAYPAL (USD)</a>', unsafe_allow_html=True)
        else:
            st.write("Suscripción: **$2.000.000 ARS**")
            # BOTONES DE ARGENTINA RESTAURADOS
            st.markdown(f'<a href="https://wa.me" class="btn-mp">💳 PAGAR CON MERCADO PAGO</a>', unsafe_allow_html=True)
            st.markdown(f'<a href="https://wa.me" class="btn-dni">🏦 PAGAR CON CUENTA DNI</a>', unsafe_allow_html=True)
        
        st.write("---")
        emp_raw = st.text_input("IDENTIFIQUE SU FIRMA / COMPANY:").strip().upper()
        pw_in = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT"):
            if pw_in == "LEGACY2026" and emp_raw in VIP:
                st.session_state.emp_final = emp_raw
                st.session_state.reg.append(f"🟢 {emp_raw} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            elif emp_raw != "":
                st.error(f"🚫 FIRMA '{emp_raw}' NO RECONOCIDA.")
                st.warning("⚠️ Contact support for VIP access: dylanelpromaster25@gmail.com")
                st.session_state.reg.append(f"🔴 ERROR: {emp_raw} - {time.strftime('%H:%M')}")
    st.stop()

# --- 5. INTERIOR TOTAL ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | NODE: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# MÉTRICAS
_, c1, c2, c3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with c1: st.metric("REAL ESTATE", "$85,000,000")
with c2: st.metric("YACHTS", "$12,500,000")
with c3: st.metric("PRIVATE JETS", "$24,000,000")

st.write("---")
# IA Y SCANNER
st.subheader("🤖 IA STRATEGIC ADVISOR")
st.info(f"Análisis activo para **{emp}**. Portafolio en estado SOLVENTE.")

st.subheader("🧬 QUANTUM ASSET SCANNER")
act = st.text_area("LISTA DE ACTIVOS:", key="sc_in_final")
if st.button("🧬 INICIAR ESCANEO"):
    if act:
        with st.spinner("Escaneando..."):
            time.sleep(1.5); st.success("VALUACIÓN DETECTADA: $42,500,000 USD")
