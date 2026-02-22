import streamlit as st
import time

# --- 1. MEMORIA DE SESIÓN (WHITELIST Y BUZÓN) ---
VIP=["EMAAR","DAMAC","NEOM","GINEVRA","REMAX","SOTHEBYS","THE AGENCY","HINES","JLL","CARSO","BARNES","FEAU","ZINGRAF","GARCIN","JUNOT","KRETZ","KNIGHT FRANK","SAVILLS","CBRE","COLLIERS","LEGACY","DYLAN","ADMIN","TZIPINE","DEMO","DYLAN777"]
if 'auth' not in st.session_state: st.session_state.auth=False
if 'demo_mode' not in st.session_state: st.session_state.demo_mode=False
if 'demo_start' not in st.session_state: st.session_state.demo_start=0
if 'demo_used' not in st.session_state: st.session_state.demo_used=False
if 'inbox' not in st.session_state: st.session_state.inbox=[] # TU CENTRAL DE MENSAJES

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY VAULT",layout="wide",initial_sidebar_state="collapsed")
st.markdown("""<style>[data-testid='collapsedControl'],[data-testid='stSidebar']{display:none!important;}.stApp{background-color:#000;border:4px solid #d4af37;padding:10px;}h1,h2,h3,p,label,.stMetric{color:#d4af37!important;text-align:center!important;}.timer-text{color:#ff4b4b!important;font-weight:bold;font-size:1.5rem;text-align:center;}.ticker-wrap{width:100%;overflow:hidden;border-bottom:1px solid #d4af37;padding:5px 0;margin-bottom:15px;}.ticker-move{display:inline-block;white-space:nowrap;padding-left:100%;animation:marquee 30s linear infinite;color:#d4af37;font-weight:bold;}@keyframes marquee{0%{transform:translateX(0);}100%{transform:translateX(-100%);}}div.stButton > button{background:none!important;border:none!important;color:#d4af37!important;font-weight:bold!important;font-size:1.3rem!important;text-transform:uppercase;}</style>""",unsafe_allow_html=True)

# --- 3. PANTALLA PÚBLICA (ACCESO Y MENSAJES) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel=st.selectbox("🌐 REGION:",["USA / GLOBAL","ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    
    with col_c:
        st.write("---")
        # --- EL BUZÓN PÚBLICO (AFUERA) ---
        st.subheader("📩 SECURE MESSAGE LINE")
        m_name = st.text_input("NAME / NOMBRE:", key="public_name")
        m_text = st.text_area("MESSAGE / MENSAJE:", key="public_msg")
        if st.button("📨 SEND / ENVIAR"):
            if m_name and m_text:
                st.session_state.inbox.append(f"📩 {m_name}: {m_text} ({time.strftime('%H:%M')})")
                st.success("ENCRYPTED AND SENT / ENVIADO")
        
        st.write("---")
        # LOGIN
        emp=st.text_input("COMPANY / EMPRESA:").strip().upper()
        pw=st.text_input("KEY / CLAVE:",type="password")
        if st.button("🔓 UNLOCK / ACCEDER"):
            if pw=="LEGACY2026" and (emp in VIP or emp=="DYLAN777"):
                st.session_state.auth=True; st.session_state.emp_final=emp; st.rerun()
            else: st.error("DENEGADO / DENIED")
        
        # DEMO
        if not st.session_state.demo_used:
            st.write("---")
            if st.button("⚡ START 5 MIN DEMO"):
                if emp: st.session_state.auth=True; st.session_state.demo_mode=True; st.session_state.demo_used=True; st.session_state.demo_start=time.time(); st.session_state.emp_final=f"DEMO_{emp}"; st.rerun()
                else: st.warning("Enter company name.")
    st.stop()

# --- 4. INTERIOR (BÓVEDA) ---
if st.session_state.demo_mode:
    rem=max(0,300-int(time.time()-st.session_state.demo_start))
    if rem<=0: st.session_state.auth=False; st.session_state.demo_mode=False; st.rerun()
    m,s=divmod(rem,60); st.markdown(f"<p class='timer-text'>⏳ SESSION: {m:02d}:{s:02d}</p>",unsafe_allow_html=True)

st.title(f"🏛️ WELCOME: {st.session_state.emp_final}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 LIVE | BTC: 96,840 | GOLD: 2,045 | AES-256 ACTIVE 🏛️</div></div>',unsafe_allow_html=True)

# EL RADAR (SOLO PARA DYLAN)
if st.session_state.emp_final == "DYLAN777":
    with st.expander("🕵️‍♂️ RADAR & INBOX"):
        st.subheader("MESSAGES RECEIVED:")
        for msg in st.session_state.inbox: st.info(msg)

c1,c2,c3=st.columns(3)
with c1: st.metric("REAL ESTATE", "$85,000,000")
with c2: st.metric("YACHTS", "$12,500,000")
with c3: st.metric("PRIVATE JETS", "$24,000,000")

st.write("---")
if st.button("🧬 SCAN"):
    st.success("VALUATION: $42,500,000 USD")

if st.button("🔒 EXIT"):
    st.session_state.auth=False; st.session_state.demo_mode=False; st.rerun()

if st.session_state.demo_mode: time.sleep(1); st.rerun()
