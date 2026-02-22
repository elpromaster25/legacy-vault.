import streamlit as st
import time

# --- 1. WHITELIST DE LOS 34 GIGANTES ---
VIP = ["EMAAR", "DAMAC", "NEOM", "GINEVRA", "REMAX", "SOTHEBYS", "THE AGENCY", "HINES", "JLL", "CARSO", "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS", "LEGACY", "DYLAN", "ADMIN", "TZIPINE"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []
if 'founder' not in st.session_state: st.session_state.founder = False

# --- 2. DISEÑO IMPERIAL (SIN FLECHA + BOTONES DIRECTOS) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    [data-testid="collapsedControl"], [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    .stApp { background-color: #000; border: 2px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 10px; }
    .btn-pay { background-color: #1a1a1a; color: #ffffff !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #d4af37; }
    div.stButton > button { background-color: #d4af37 !important; color: #000 !important; width: 100% !important; font-weight: bold !important; height: 3.5em !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESO (LOGIN) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 SELECT REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        # CONFIGURACIÓN DE LOS 3 BOTONES DE EMAIL
        if reg_sel == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD**")
            m_pp = "mailto:dylanelpromaster25@://gmail.com."
            st.markdown(f'<a href="{m_pp}" class="btn-pay">🔵 PAY WITH PAYPAL (EMAIL)</a>', unsafe_allow_html=True)
        else:
            st.write("Suscripción: **$2.000.000 ARS**")
            m_mp = "mailto:dylanelpromaster25@://gmail.com."
            m_dni = "mailto:dylanelpromaster25@://gmail.com."
            st.markdown(f'<a href="{m_mp}" class="btn-pay" style="background:#009ee3; border-color:#fff;">💳 PAGAR CON MERCADO PAGO</a>', unsafe_allow_html=True)
            st.markdown(f'<a href="{m_dni}" class="btn-pay" style="background:#004d40; border-color:#fff;">🏦 PAGAR CON CUENTA DNI</a>', unsafe_allow_html=True)
        
        st.write("---")
        emp = st.text_input("COMPANY:").strip().upper()
        pw = st.text_input("KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT"):
            if emp == "DYLAN777" and pw == "LEGACY2026":
                st.session_state.founder = True; st.session_state.emp_final = "FOUNDER CONTROL"; st.session_state.auth = True; st.rerun()
            elif pw == "LEGACY2026" and emp in VIP:
                st.session_state.emp_final = emp; st.session_state.reg.append(f"🟢 {emp} - {time.strftime('%H:%M')}"); st.session_state.auth = True; st.rerun()
            elif emp != "":
                st.error("🚫 DENEGADO."); st.session_state.reg.append(f"🔴 ERROR: {emp} - {time.strftime('%H:%M')}")
    st.stop()

# --- 4. INTERIOR (SOLO DYLAN VE EL RADAR ABAJO) ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
st.metric("REAL ESTATE ASSETS", "$85,000,000")
st.write("---")
if st.button("🧬 SCANNER"):
    st.success("VALUACIÓN DETECTADA: $42,500,000 USD")

if st.session_state.founder:
    st.write("---")
    with st.expander("🕵️‍♂️ RADAR DE IMPACTOS (SOLO DYLAN)"):
        for r in st.session_state.reg: st.info(r)

if st.button("🔒 LOGOUT"):
    st.session_state.auth = False; st.session_state.founder = False; st.rerun()
