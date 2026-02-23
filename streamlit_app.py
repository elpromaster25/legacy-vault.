import streamlit as st
import time

# --- 1. RADAR ETERNO (MEMORIA GLOBAL) ---
@st.cache_resource
def get_global_radar():
    return [] 

radar_global = get_global_radar()

def register_hit(name):
    timestamp = time.strftime('%H:%M:%S')
    log = f"📡 SIGNAL: {name} entered at {timestamp}"
    if log not in radar_global: radar_global.append(log)

VIP=["EMAAR","DAMAC","NEOM","GINEVRA","REMAX","SOTHEBYS","THE AGENCY","HINES","JLL","CARSO","BARNES","FEAU","ZINGRAF","GARCIN","JUNOT","KRETZ","KNIGHT FRANK","SAVILLS","CBRE","COLLIERS","LEGACY","DYLAN","ADMIN","TZIPINE","DEMO","DYLAN777"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo_mode' not in st.session_state: st.session_state.demo_mode = False

# --- 2. DISEÑO IMPERIAL & BLINDAJE (SIN BARRAS) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    header, [data-testid="stSidebar"], [data-testid="collapsedControl"], .stDeployButton, #MainMenu, footer {
        visibility: hidden; display: none !important;
    }
    .stApp {background-color: #000; border: 4px solid #d4af37; padding: 10px;}
    h1, h2, h3, p, label, .stMetric {color: #d4af37!important; text-align: center!important;}
    .ticker-wrap {width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 5px 0; margin-bottom: 15px;}
    .ticker-move {display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold;}
    @keyframes marquee {0% {transform: translateX(0);} 100% {transform: translateX(-100%);}}
    div.stButton > button {background: none!important; border: none!important; color: #d4af37!important; font-weight: bold!important; font-size: 1.2rem!important; text-transform: uppercase;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIN & DEMO ---
if not st.session_state.auth and not st.session_state.demo_mode:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.subheader("📩 SECURE MESSAGE LINE")
        m_n = st.text_input("NAME:", key="n")
        m_t = st.text_area("MESSAGE:", key="m")
        if st.button("📨 SEND"):
            if m_n and m_t:
                radar_global.append(f"📩 {m_n}: {m_t} ({time.strftime('%H:%M')})")
                st.success("SENT"); time.sleep(1); st.rerun()
        st.write("---")
        emp = st.text_input("COMPANY / USER:").strip().upper()
        pw = st.text_input("KEY / PASS:", type="password")
        c_a, c_b = st.columns(2)
        with c_a:
            if st.button("🔓 UNLOCK"):
                if pw == "LEGACY2026" and (emp in VIP or emp == "DYLAN777"):
                    register_hit(emp); st.session_state.auth = True; st.session_state.emp_final = emp; st.rerun()
                else: st.error("DENIED")
        with c_b:
            if st.button("⏱️ DEMO"):
                register_hit("GUEST_DEMO"); st.session_state.demo_mode = True
                st.session_state.start_t = time.time(); st.rerun()
    st.stop()

# --- 4. INTERIOR DEL BÚNKER (DIBUJO PRIMERO) ---
emp_now = "GUEST (DEMO)" if st.session_state.demo_mode else st.session_state.emp_final
st.title(f"🏛️ VAULT NODE: {emp_now}")

# RADAR DYLAN777
if not st.session_state.demo_mode and st.session_state.emp_final == "DYLAN777":
    with st.expander("🕵️‍♂️ QUANTUM RADAR (LIVE SIGNALS)", expanded=True):
        if not radar_global: st.write("SILENCE")
        else:
            for s in reversed(radar_global): st.info(s)
        if st.button("🗑️ RESET RADAR"):
            radar_global.clear(); st.rerun()

st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 98,200 | GOLD: 2,120 | NODE: {emp_now} | AES-256 ACTIVE 🏛️</div></div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85,000,000")
with c2: st.metric("YACHTS", "$12,500,000")
with c3: st.metric("JETS", "$24,000,000")

st.write("---")
st.subheader("📈 STRATEGIC CAPITAL PROJECTION")
cap = st.number_input("INITIAL:", value=85000000)
a = st.slider("YEARS:", 1, 50, 10)
b = st.slider("BONUS %:", 1, 20, 5)
st.success(f"FUTURE VALUATION: ${(cap * ((1 + b/100) ** a)):,.2f} USD")

# --- 5. LÓGICA DE TIEMPO (AL FINAL PARA NO TRABAR EL DIBUJO) ---
if st.session_state.demo_mode:
    if 'start_t' not in st.session_state: st.session_state.start_t = time.time()
    elapsed = time.time() - st.session_state.start_t
    rem = max(0, int(300 - elapsed))
    
    st.write("---")
    st.warning(f"⏳ DEMO EXPIRES IN: {rem} SECONDS")
    
    if rem <= 0:
        st.session_state.demo_mode = False; st.rerun()
    else:
        time.sleep(1)
        st.rerun()

if st.button("🔒 EXIT VAULT"):
    st.session_state.auth = False; st.session_state.demo_mode = False; st.rerun()
