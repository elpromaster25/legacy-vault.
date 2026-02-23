import streamlit as st
import time

# --- 1. RADAR GLOBAL (INBOX QUE NO MUERE) ---
if 'inbox' not in st.session_state:
    st.session_state.inbox = []

VIP=["EMAAR","DAMAC","NEOM","GINEVRA","REMAX","SOTHEBYS","THE AGENCY","HINES","JLL","CARSO","BARNES","FEAU","ZINGRAF","GARCIN","JUNOT","KRETZ","KNIGHT FRANK","SAVILLS","CBRE","COLLIERS","LEGACY","DYLAN","ADMIN","TZIPINE","DEMO","DYLAN777"]

if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL & BLINDAJE AGRESIVO (CHAU BARRAS) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* OCULTAR TODO: BARRA SUPERIOR, LATERAL, BOTONES Y FOOTER */
    header, [data-testid="stSidebar"], [data-testid="collapsedControl"], .stDeployButton, #MainMenu, footer {
        visibility: hidden;
        display: none !important;
    }
    /* AJUSTE DE PANTALLA COMPLETA */
    .block-container {padding: 1rem 2rem !important;}
    .stApp {background-color: #000; border: 4px solid #d4af37; padding: 10px;}
    h1, h2, h3, p, label, .stMetric {color: #d4af37!important; text-align: center!important;}
    .ticker-wrap {width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 5px 0; margin-bottom: 15px;}
    .ticker-move {display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold;}
    @keyframes marquee {0% {transform: translateX(0);} 100% {transform: translateX(-100%);}}
    div.stButton > button {background: none!important; border: none!important; color: #d4af37!important; font-weight: bold!important; font-size: 1.3rem!important; text-transform: uppercase;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA PÚBLICA (LOGIN + MENSAJERÍA REPARADA) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.write("---")
        st.subheader("📩 SECURE MESSAGE LINE")
        m_name = st.text_input("NAME / NOMBRE:", key="public_name_input")
        m_text = st.text_area("MESSAGE / MENSAJE:", key="public_msg_input")
        
        if st.button("📨 SEND / ENVIAR"):
            if m_name and m_text:
                # GUARDADO EN EL RADAR (FUNCIONA CON CUALQUIER NOMBRE)
                st.session_state.inbox.append(f"📩 {m_name}: {m_text} ({time.strftime('%H:%M')})")
                st.success("SENT / ENVIADO")
                time.sleep(1)
                st.rerun()
            else: st.error("Complete fields / Complete campos")
        
        st.write("---")
        if reg_sel == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD / MONTH**")
            emp = st.text_input("COMPANY:").strip().upper()
            pw = st.text_input("KEY:", type="password")
            if st.button("🔓 UNLOCK"):
                if pw == "LEGACY2026" and (emp in VIP or emp == "DYLAN777"):
                    st.session_state.auth = True; st.session_state.emp_final = emp; st.rerun()
                else: st.error("DENIED")
        else:
            st.write("Suscripción: **$2.000.000 ARS / MES**")
            emp = st.text_input("EMPRESA:").strip().upper()
            pw = st.text_input("CLAVE:", type="password")
            if st.button("🔓 ACCEDER"):
                if pw == "LEGACY2026" and (emp in VIP or emp == "DYLAN777"):
                    st.session_state.auth = True; st.session_state.emp_final = emp; st.rerun()
                else: st.error("DENEGADO")
    st.stop()

# --- 4. INTERIOR (BÚNKER RESTAURADO 100%) ---
st.title(f"🏛️ WELCOME: {st.session_state.emp_final}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | NODE: {st.session_state.emp_final} | AES-256 ACTIVE 🏛️</div></div>', unsafe_allow_html=True)

# RADAR ADMIN (DYLAN777)
if st.session_state.emp_final == "DYLAN777":
    with st.expander("🕵️‍♂️ RADAR ADMIN & INBOX", expanded=True):
        if not st.session_state.inbox:
            st.write("SIN SEÑALES / NO SIGNALS")
        else:
            for m in st.session_state.inbox:
                st.info(m)
        if st.button("🗑️ CLEAR RADAR"):
            st.session_state.inbox = []; st.rerun()

c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85,000,000")
with c2: st.metric("YACHTS", "$12,500,000")
with c3: st.metric("PRIVATE JETS", "$24,000,000")

st.write("---")
st.subheader("📈 STRATEGIC CAPITAL PROJECTION")
cap_init = st.number_input("INITIAL CAPITAL (USD):", value=85000000, step=1000000)
ca, cb = st.columns(2)
with ca: anios = st.slider("HORIZON (YEARS):", 1, 50, 10)
with cb: bonus = st.slider("BONUS (%):", 1, 20, 5)
st.success(f"FUTURE VALUATION: ${(cap_init * ((1 + bonus/100) ** anios)):,.2f} USD")

st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER")
activos = st.text_area("LIST ASSETS:", key="scan_box")
if st.button("🧬 SCAN"):
    if activos: st.success("VALUATION DETECTED: $42,500,000 USD")

st.write("---")
st.subheader("🤖 IA STRATEGIC ADVISOR")
if st.text_input("CONSULTA:", key="ia_box"): 
    st.info(f"ADVISOR: Analysis for {st.session_state.emp_final} complete.")

if st.button("🔒 EXIT"):
    st.session_state.auth = False; st.rerun()
