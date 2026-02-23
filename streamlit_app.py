import streamlit as st
import time

# --- 1. MEMORIA DE NODO (COMMS FIXED) ---
VIP=["EMAAR","DAMAC","NEOM","GINEVRA","REMAX","SOTHEBYS","THE AGENCY","HINES","JLL","CARSO","BARNES","FEAU","ZINGRAF","GARCIN","JUNOT","KRETZ","KNIGHT FRANK","SAVILLS","CBRE","COLLIERS","LEGACY","DYLAN","ADMIN","TZIPINE","DEMO","DYLAN777"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'inbox' not in st.session_state: st.session_state.inbox = [] # RADAR ACTIVO

# --- 2. DISEÑO IMPERIAL & BLINDAJE (SIDEBAR HIDDEN) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")

# CSS PARA BORRAR TODO LO QUE NO SEA EL BÚNKER (IZQUIERDA Y ARRIBA)
st.markdown("""
    <style>
    /* Ocultar barra lateral y botones de edición */
    [data-testid="stSidebar"], [data-testid="collapsedControl"], .stDeployButton, #MainMenu, footer {display:none!important;}
    /* Ajustar márgenes para que se vea limpio */
    .block-container {padding-top: 2rem; padding-bottom: 0rem;}
    /* Colores Legacy */
    .stApp {background-color: #000; border: 4px solid #d4af37; padding: 10px;}
    h1, h2, h3, p, label, .stMetric {color: #d4af37!important; text-align: center!important;}
    .ticker-wrap {width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 5px 0; margin-bottom: 15px;}
    .ticker-move {display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold;}
    @keyframes marquee {0% {transform: translateX(0);} 100% {transform: translateX(-100%);}}
    div.stButton > button {background: none!important; border: none!important; color: #d4af37!important; font-weight: bold!important; font-size: 1.3rem!important; text-transform: uppercase;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA PÚBLICA (LOGIN + BUZÓN REPARADO) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.write("---")
        st.subheader("📩 SECURE MESSAGE LINE")
        m_name = st.text_input("NAME / NOMBRE:", placeholder="Enter your name", key="name_input")
        m_text = st.text_area("MESSAGE / MENSAJE:", placeholder="Type your inquiry...", key="msg_input")
        
        if st.button("📨 SEND / ENVIAR"):
            if m_name and m_text:
                new_msg = f"📩 {m_name}: {m_text} ({time.strftime('%H:%M')})"
                st.session_state.inbox.append(new_msg)
                st.success("SENT TO VAULT / ENVIADO A LA BÓVEDA")
            else:
                st.error("Fields required / Campos obligatorios")
        
        st.write("---")
        if reg_sel == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD / MONTH**")
            emp = st.text_input("COMPANY:", key="emp_usa").strip().upper()
            pw = st.text_input("KEY:", type="password", key="pw_usa")
            if st.button("🔓 UNLOCK"):
                if pw == "LEGACY2026" and (emp in VIP or emp == "DYLAN777"):
                    st.session_state.auth = True; st.session_state.emp_final = emp; st.rerun()
                else: st.error("ACCESS DENIED")
        else:
            st.write("Suscripción: **$2.000.000 ARS / MES**")
            emp = st.text_input("EMPRESA:", key="emp_arg").strip().upper()
            pw = st.text_input("CLAVE:", type="password", key="pw_arg")
            if st.button("🔓 ACCEDER"):
                if pw == "LEGACY2026" and (emp in VIP or emp == "DYLAN777"):
                    st.session_state.auth = True; st.session_state.emp_final = emp; st.rerun()
                else: st.error("ACCESO DENEGADO")
    st.stop()

# --- 4. INTERIOR (RADAR OPERATIVO) ---
st.title(f"🏛️ WELCOME: {st.session_state.emp_final}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | NODE: {st.session_state.emp_final} | SECURE CHANNEL ACTIVE 🏛️</div></div>', unsafe_allow_html=True)

if st.session_state.emp_final == "DYLAN777":
    with st.expander("🕵️‍♂️ RADAR ADMIN & INBOX", expanded=True):
        if not st.session_state.inbox: st.write("NO INCOMING SIGNALS / SIN SEÑALES")
        for msg in st.session_state.inbox: st.info(msg)

c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85,000,000")
with c2: st.metric("YACHTS", "$12,500,000")
with c3: st.metric("PRIVATE JETS", "$24,000,000")

st.write("---")
st.subheader("📈 STRATEGIC CAPITAL PROJECTION")
cap_init = st.number_input("INITIAL CAPITAL (USD):", value=85000000, step=1000000)
col_a, col_b = st.columns(2)
with col_a: anios = st.slider("TIME HORIZON (YEARS):", 1, 50, 10)
with col_b: bonus = st.slider("ANNUAL BONUS (%):", 1, 20, 5)
proyeccion = cap_init * ((1 + bonus/100) ** anios)
st.markdown(f"<div style='border:1px solid #d4af37; padding:20px; border-radius:10px; background:rgba(212,175,55,0.1); text-align:center;'><h3>FUTURE VALUATION: ${proyeccion:,.2f} USD</h3></div>", unsafe_allow_html=True)

if st.button("🔒 EXIT VAULT"):
    st.session_state.auth = False; st.rerun()
