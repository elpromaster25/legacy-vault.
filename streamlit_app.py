import streamlit as st
import time

# --- 1. BASE DE DATOS DE LOS 34 MISILES (AUTORIZADOS) ---
VIP = [
    "EMAAR", "DAMAC", "NAKHEEL", "AZIZI", "NEOM", # DUBAI / ARABIA
    "GINEVRA", "REMAX", "SOTHEBYS", "NEST SEEKERS", "ALVEAR", # ARG / LATAM
    "THE AGENCY", "HINES", "JLL", "DOUGLAS ELLIMAN", "FORTUNE", # USA
    "CARSO", "ABILIA", "GICSA", "BE GRAND", "TERRA", # MEXICO
    "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", # FRANCIA
    "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS", # LONDRES / GLOBAL
    "LEGACY", "DYLAN", "ADMIN", "TZIPINE" # TUS CLAVES
]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 20px; }
    .btn-paypal { background-color: #0070ba; color: white !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #fff; }
    .btn-mp { background-color: #009ee3; color: white !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #fff; }
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

# --- 4. ACCESO AL BÚNKER ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 SELECT REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        if reg_sel == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD**")
            st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com" class="btn-paypal">🔵 PAY WITH PAYPAL (USD)</a>', unsafe_allow_html=True)
        else:
            st.write("Suscripción: **$2.000.000 ARS**")
            st.markdown(f'<a href="https://wa.me" class="btn-mp">💳 MERCADO PAGO / DNI</a>', unsafe_allow_html=True)
        st.write("---")
        emp_raw = st.text_input("IDENTIFIQUE SU FIRMA / COMPANY:").strip().upper()
        pw_in = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT"):
            if pw_in == "LEGACY2026" and emp_raw in VIP:
                st.session_state.emp_final = emp_raw
                st.session_state.reg.append(f"🟢 {emp_raw} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            elif emp_raw != "":
                st.error("ACCESO DENEGADO")
                st.session_state.reg.append(f"🔴 ERROR: {emp_raw} - {time.strftime('%H:%M')}")
    st.stop()

# --- 5. INTERIOR TOTAL ---
st.title(f"🏛️ TERMINAL EXCLUSIVA: {st.session_state.emp_final}")
st.metric("REAL ESTATE", "$85,000,000")
st.subheader("🧬 QUANTUM ASSET SCANNER")
if st.button("🧬 INICIAR ESCANEO"):
    with st.spinner("Escaneando..."):
        time.sleep(1.5); st.success("VALUACIÓN: $42,500,000 USD")
