import streamlit as st
import time
VIP=["EMAAR","DAMAC","NEOM","GINEVRA","REMAX","SOTHEBYS","THE AGENCY","HINES","JLL","CARSO","BARNES","FEAU","ZINGRAF","GARCIN","JUNOT","KRETZ","KNIGHT FRANK","SAVILLS","CBRE","COLLIERS","LEGACY","DYLAN","ADMIN","TZIPINE","DEMO","DYLAN777"]
if 'auth' not in st.session_state: st.session_state.auth=False
if 'reg' not in st.session_state: st.session_state.reg=[]
st.set_page_config(page_title="LEGACY VAULT",layout="wide",initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='collapsedControl'],[data-testid='stSidebar']{display:none!important;}.stApp{background-color:#000;border:4px solid #d4af37;padding:10px;}h1,h2,h3,p,label,.stMetric{color:#d4af37!important;text-align:center!important;}.ticker-wrap{width:100%;overflow:hidden;border-bottom:1px solid #d4af37;padding:10px 0;margin-bottom:20px;}.ticker-move{display:inline-block;white-space:nowrap;padding-left:100%;animation:marquee 30s linear infinite;color:#d4af37;font-weight:bold;}@keyframes marquee{0%{transform:translateX(0);}100%{transform:translateX(-100%);}}.ws-link{display:block;color:#d4af37!important;font-weight:bold;text-decoration:none;text-align:center;margin-bottom:15px;font-size:1.2rem;}div.stButton>button{background:none!important;border:none!important;color:#d4af37!important;font-weight:bold!important;font-size:1.5rem!important;text-transform:uppercase;cursor:pointer;}</style>",unsafe_allow_html=True)
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel=st.selectbox("🌐 REGION:",["USA / GLOBAL","ARGENTINA"])
    _,col_c,_=st.columns([1,1.5,1])
    with col_c:
        st.write("---")
        ws="https://wa.me"
        st.markdown(f'<a href="{ws}DEMO" class="ws-link">⚡ SOLICITAR DEMO (WSP)</a>',unsafe_allow_html=True)
        if reg_sel=="USA / GLOBAL":
            st.markdown(f'<a href="{ws}PAYPAL" class="ws-link">🔵 PAY WITH PAYPAL (WSP)</a>',unsafe_allow_html=True)
        else:
            st.markdown(f'<a href="{ws}MP" class="ws-link">💳 MERCADO PAGO (WSP)</a>',unsafe_allow_html=True)
            st.markdown(f'<a href="{ws}DNI" class="ws-link">🏦 CUENTA DNI (WSP)</a>',unsafe_allow_html=True)
        st.write("---")
        emp=st.text_input("COMPANY:").strip().upper()
        pw=st.text_input("KEY:",type="password")
        if st.button("🔓 ACCEDER"):
            if pw=="LEGACY2026" and (emp in VIP or emp=="DYLAN777"):
                st.session_state.emp_final=emp
                if emp!="DYLAN777":st.session_state.reg.append(f"🟢 {emp}-{time.strftime('%H:%M')}")
                st.session_state.auth=True
                st.rerun()
            else:st.error("🚫 DENEGADO")
    st.stop()
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | NODE: {st.session_state.emp_final} | VALUATION: $85,000,000 🏛️</div></div>',unsafe_allow_html=True)
if st.session_state.emp_final=="DYLAN777":
    with st.expander("🕵️‍♂️ RADAR"):
        for r in st.session_state.reg:st.info(r)
st.metric("REAL ESTATE ASSETS","$85,000,000")
st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER")
act=st.text_area("LISTA DE ACTIVOS (FERRARIS, YATES, ETC):",key="sc_final")
if st.button("🧬 SCAN"):
    if act:
        with st.spinner("..."):time.sleep(1)
        st.success("VALUACIÓN: $42,500,000 USD")
st.write("---")
st.subheader("🤖 IA STRATEGIC ADVISOR")
p_ia=st.text_input("CONSULTA TÉCNICA:",key="ia_final")
if p_ia:
    st.info(f"ADVISOR: Análisis para {st.session_state.emp_final} completado. Estado: ÓPTIMO.")
if st.button("🔒 LOGOUT"):
    st.session_state.auth=False
    st.rerun()
