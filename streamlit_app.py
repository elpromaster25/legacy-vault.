import streamlit as st
import time

# --- 1. ESTRUCTURA ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")

# --- 2. MEMORIA ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo_start' not in st.session_state: st.session_state.demo_start = None

# --- 3. DISEÑO IMPERIAL ---
st.markdown("<style>[data-testid='collapsedControl'],[data-testid='stSidebar']{display:none!important;}.stApp{background-color:#000;border:4px solid #d4af37;padding:10px;}h1,h2,h3,p,label,.stMetric{color:#d4af37!important;text-align:center!important;}div.stButton > button{background:none!important;border:none!important;color:#d4af37!important;font-weight:bold!important;font-size:1.5rem!important;text-transform:uppercase;cursor:pointer;}.ws-link{display:block;color:#d4af37!important;font-weight:bold;text-decoration:none;text-align:center;margin-bottom:15px;font-size:1.2rem;}.mail-link{display:block;color:#ffffff!important;font-size:0.8rem;text-align:center;text-decoration:none;margin-top:5px;opacity:0.6;}</style>",unsafe_allow_html=True)

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
            st.markdown('<a href="mailto:dylanelpromaster25@gmail.com" class="mail-link">✉️ dylanelpromaster25@gmail.com</a>', unsafe_allow_html=True)
            st.write("---")
            emp = st.text_input("COMPANY:").strip().upper()
            pw = st.text_input("KEY:", type="password")
            if st.button("🔓 UNLOCK"):
                if pw == "LEGACY2026": st.session_state.auth = True; st.session_state.emp_final = emp; st.rerun()
            st.write("---")
            if st.button("⚡ START 5 MIN DEMO"):
                st.session_state.auth = True; st.session_state.emp_final = "GUEST_DEMO"; st.session_state.demo_start = time.time(); st.rerun()
        else:
            st.write("Suscripción: **$2.000.000 ARS**")
            st.markdown(f'<a href="{ws}MP" class="ws-link" style="color:#009ee3!important;">💳 MERCADO PAGO (WSP)</a>', unsafe_allow_html=True)
            st.markdown(f'<a href="{ws}DNI" class="ws-link" style="color:#004d40!important;">🏦 CUENTA DNI (WSP)</a>', unsafe_allow_html=True)
            st.markdown('<a href="mailto:dylanelpromaster25@gmail.com" class="mail-link">✉️ dylanelpromaster25@gmail.com</a>', unsafe_allow_html=True)
            st.write("---")
            emp = st.text_input("EMPRESA:").strip().upper()
            pw = st.text_input("CLAVE:", type="password")
            if st.button("🔓 ACCEDER"):
                if pw == "LEGACY2026": st.session_state.auth = True; st.session_state.emp_final = emp; st.rerun()
            st.write("---")
            if st.button("⚡ INICIAR DEMO 5 MIN"):
                st.session_state.auth = True; st.session_state.emp_final = "VISITANTE_DEMO"; st.session_state.demo_start = time.time(); st.rerun()
    st.stop()

# --- 5. INTERIOR CON AUTO-REFRESCO ---
if st.session_state.demo_start:
    elapsed = time.time() - st.session_state.demo_start
    remaining = max(0, 300 - int(elapsed))
    if remaining <= 0:
        st.session_state.auth = False; st.session_state.demo_start = None; st.rerun()
    mins, secs = divmod(remaining, 60)
    st.markdown(f"<h2 style='color:red !important;'>⚠️ DEMO TIME: {mins:02d}:{secs:02d}</h2>", unsafe_allow_html=True)
    # EL MOTOR DEL RELOJ:
    time.sleep(1)
    st.rerun()

st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85,000,000")
with c2: st.metric("YACHTS", "$12,500,000")
with c3: st.metric("PRIVATE JETS", "$24,000,000")
st.write("---")
if st.button("🧬 SCAN"): st.success("VALUATION: $42,500,000 USD")
if st.button("🔒 LOGOUT"): st.session_state.auth = False; st.session_state.demo_start = None; st.rerun()
