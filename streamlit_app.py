import streamlit as st
import time

# --- 1. RADAR ETERNO (MEMORIA DEL SERVIDOR) ---
@st.cache_resource
def get_global_radar():
    return [] 

radar_global = get_global_radar()

# --- 2. REGISTRO DE ENTRADAS ---
def register_hit(name):
    timestamp = time.strftime('%H:%M:%S')
    log = f"📡 SIGNAL: {name} entered the Vault at {timestamp}"
    if log not in radar_global:
        radar_global.append(log)

VIP=["EMAAR","DAMAC","NEOM","GINEVRA","REMAX","SOTHEBYS","THE AGENCY","HINES","JLL","CARSO","BARNES","FEAU","ZINGRAF","GARCIN","JUNOT","KRETZ","KNIGHT FRANK","SAVILLS","CBRE","COLLIERS","LEGACY","DYLAN","ADMIN","TZIPINE","DEMO","DYLAN777"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo_mode' not in st.session_state: st.session_state.demo_mode = False

# --- 3. DISEÑO IMPERIAL & BLINDAJE TOTAL (SIDEBAR HIDDEN) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    header, [data-testid="stSidebar"], [data-testid="collapsedControl"], .stDeployButton, #MainMenu, footer {
        visibility: hidden; display: none !important;
    }
    .block-container {padding: 1rem 2rem !important;}
    .stApp {background-color: #000; border: 4px solid #d4af37; padding: 10px;}
    h1, h2, h3, p, label, .stMetric {color: #d4af37!important; text-align: center!important;}
    .ticker-wrap {width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 5px 0; margin-bottom: 15px;}
    .ticker-move {display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold;}
    @keyframes marquee {0% {transform: translateX(0);} 100% {transform: translateX(-100%);}}
    div.stButton > button {background: none!important; border: none!important; color: #d4af37!important; font-weight: bold!important; font-size: 1.2rem!important; text-transform: uppercase;}
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANTALLA PÚBLICA (LOGIN + DEMO INTEGRADA) ---
if not st.session_state.auth and not st.session_state.demo_mode:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.write("---")
        st.subheader("📩 SECURE MESSAGE LINE")
        m_name = st.text_input("NAME / NOMBRE:", key="pub_n")
        m_text = st.text_area("MESSAGE / MENSAJE:", key="pub_m")
        if st.button("📨 SEND / ENVIAR"):
            if m_name and m_text:
                msg = f"📩 MESSAGE from {m_name}: {m_text} ({time.strftime('%H:%M')})"
                radar_global.append(msg)
                st.success("SENT / ENVIADO")
                time.sleep(1); st.rerun()
        
        st.write("---")
        st.subheader("🔑 ACCESS CONTROL")
        emp = st.text_input("COMPANY / EMPRESA:").strip().upper()
        pw = st.text_input("KEY / CLAVE:", type="password")
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🔓 UNLOCK"):
                if pw == "LEGACY2026" and (emp in VIP or emp == "DYLAN777"):
                    register_hit(emp)
                    st.session_state.auth = True; st.session_state.emp_final = emp; st.rerun()
                else: st.error("DENIED")
        with col_btn2:
            if st.button("⏱️ START DEMO"):
                register_hit("GUEST_DEMO")
                st.session_state.demo_mode = True; st.session_state.start_time = time.time(); st.rerun()
                
    st.stop()

# --- 5. INTERIOR (BÚNKER + RELOJ DE DEMO) ---
emp_display = "GUEST (DEMO)" if st.session_state.demo_mode else st.session_state.emp_final
st.title(f"🏛️ VAULT NODE: {emp_display}")

# LÓGICA DE TIEMPO PARA DEMO
if st.session_state.demo_mode:
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, int(300 - elapsed))
    st.warning(f"⏳ DEMO ACCESS EXPIRES IN: {remaining} SECONDS")
    if remaining <= 0:
        st.session_state.demo_mode = False; st.error("DEMO EXPIRED"); time.sleep(2); st.rerun()

st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | NODE: {emp_display} | AES-256 ACTIVE 🏛️</div></div>', unsafe_allow_html=True)

# RADAR ADMIN (SOLO DYLAN777)
if not st.session_state.demo_mode and st.session_state.emp_final == "DYLAN777":
    with st.expander("🕵️‍♂️ QUANTUM RADAR (LIVE SIGNALS)", expanded=True):
        if not radar_global: st.write("SILENCE")
        else:
            for signal in reversed(radar_global): st.info(signal)
        if st.button("🗑️ RESET"): radar_global.clear(); st.rerun()

# CONTENIDO DEL BÚNKER
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
if st.button("🧬 SCAN ASSETS"): st.success("SCANNING COMPLETE: $42,500,000 USD DETECTED")

st.write("---")
st.subheader("🤖 IA STRATEGIC ADVISOR")
if st.text_input("CONSULTA:", key="ia_box"): st.info("ANALYSIS COMPLETE.")

if st.button("🔒 EXIT VAULT"):
    st.session_state.auth = False; st.session_state.demo_mode = False; st.rerun()
