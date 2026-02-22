import streamlit as st
import time

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")

# --- 2. MEMORIA ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo_mode' not in st.session_state: st.session_state.demo_mode = False
if 'demo_start' not in st.session_state: st.session_state.demo_start = 0

# --- 3. DISEÑO IMPERIAL ---
st.markdown("""
    <style>
    [data-testid='collapsedControl'], [data-testid='stSidebar'] { display: none !important; }
    .stApp { background-color: #000; border: 4px solid #d4af37; padding: 10px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .timer-text { color: #ff4b4b !important; font-weight: bold; font-size: 1.5rem; text-align: center; margin-bottom: 5px; }
    .ticker-wrap { width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 5px 0; margin-bottom: 15px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    .ws-link { display: block; color: #d4af37 !important; font-weight: bold; text-decoration: none; text-align: center; margin-bottom: 10px; font-size: 1.1rem; }
    div.stButton > button { background: none !important; border: none !important; color: #d4af37 !important; font-weight: bold !important; font-size: 1.3rem !important; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg = st.selectbox("🌐 REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.write("---")
        ws = "https://wa.me"
        if reg == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD**")
            st.markdown(f'<a href="{ws}PAYPAL" class="ws-link">🔵 PAY WITH PAYPAL (WSP)</a>', unsafe_allow_html=True)
            st.write("---")
            emp = st.text_input("COMPANY:").strip().upper()
            pw = st.text_input("KEY:", type="password")
            if st.button("🔓 UNLOCK"):
                if pw == "LEGACY2026": st.session_state.auth = True; st.session_state.emp_final = emp; st.rerun()
                else: st.error("DENIED")
            st.write("---")
            st.write("💡 *If you want to use the 5 min DEMO, please enter your company name above.*")
            if st.button("⚡ START 5 MIN DEMO"):
                if emp: st.session_state.auth = True; st.session_state.demo_mode = True; st.session_state.demo_start = time.time(); st.session_state.emp_final = f"DEMO_{emp}"; st.rerun()
                else: st.warning("Enter company name.")
        else:
            st.write("Suscripción: **$2.000.000 ARS**")
            st.markdown(f'<a href="{ws}MP" class="ws-link" style="color:#009ee3!important;">💳 MERCADO PAGO (WSP)</a>', unsafe_allow_html=True)
            st.markdown(f'<a href="{ws}DNI" class="ws-link" style="color:#004d40!important;">🏦 CUENTA DNI (WSP)</a>', unsafe_allow_html=True)
            st.write("---")
            emp = st.text_input("EMPRESA:").strip().upper()
            pw = st.text_input("CLAVE:", type="password")
            if st.button("🔓 ACCEDER"):
                if pw == "LEGACY2026": st.session_state.auth = True; st.session_state.emp_final = emp; st.rerun()
                else: st.error("DENEGADO")
            st.write("---")
            st.write("💡 *Si querés usar la demo de 5 min, poné el nombre de tu empresa arriba.*")
            if st.button("⚡ INICIAR DEMO 5 MIN"):
                if emp: st.session_state.auth = True; st.session_state.demo_mode = True; st.session_state.demo_start = time.time(); st.session_state.emp_final = f"DEMO_{emp}"; st.rerun()
                else: st.warning("Poné el nombre de tu empresa.")
    st.stop()

# --- 5. INTERIOR CON MOTOR DE TIEMPO ---
if st.session_state.demo_mode:
    remaining = max(0, 300 - int(time.time() - st.session_state.demo_start))
    if remaining <= 0:
        st.session_state.auth = False; st.session_state.demo_mode = False; st.rerun()
    
    mins, secs = divmod(remaining, 60)
    col_out, col_timer = st.columns([1, 2])
    with col_out:
        if st.button("🔒 EXIT DEMO"):
            st.session_state.auth = False; st.session_state.demo_mode = False; st.rerun()
    with col_timer:
        st.markdown(f"<p class='timer-text'>⏳ SESSION TIME: {mins:02d}:{secs:02d}</p>", unsafe_allow_html=True)

st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | NODE: {st.session_state.emp_final} | AES-256 ACTIVE 🏛️</div></div>',unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85,000,000")
with c2: st.metric("YACHTS", "$12,500,000")
with c3: st.metric("PRIVATE JETS", "$24,000,000")

st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER")
act = st.text_area("LISTA DE ACTIVOS (FERRARIS, PROPIEDADES, ETC):", key="sc_f_boss")
if st.button("🧬 SCAN"):
    if act:
        with st.spinner("..."): time.sleep(1); st.success("VALUATION: $42,500,000 USD")

st.write("---")
st.subheader("🤖 IA STRATEGIC ADVISOR")
p_ia = st.text_input("CONSULTA TÉCNICA:", key="ia_f_boss")
if p_ia:
    st.info(f"ADVISOR: Analysis for {st.session_state.emp_final} complete. Status: OPTIMAL.")

# EL MOTOR QUE HACE QUE EL TIEMPO BAJE SOLO CADA SEGUNDO
if st.session_state.demo_mode:
    time.sleep(1)
    st.rerun()
