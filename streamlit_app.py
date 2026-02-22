import streamlit as st
import time
VIP=["EMAAR","DAMAC","NEOM","GINEVRA","REMAX","SOTHEBYS","THE AGENCY","HINES","JLL","CARSO","BARNES","FEAU","ZINGRAF","GARCIN","JUNOT","KRETZ","KNIGHT FRANK","SAVILLS","CBRE","COLLIERS","LEGACY","DYLAN","ADMIN","TZIPINE","DEMO","DYLAN777"]
if 'auth' not in st.session_state: st.session_state.auth=False
if 'reg' not in st.session_state: st.session_state.reg=[]
st.set_page_config(page_title="LEGACY VAULT",layout="wide",initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='collapsedControl'],[data-testid='stSidebar']{display:none!important;}.stApp{background-color:#000;border:4px solid #d4af37;padding:10px;}h1,h2,h3,p,label,.stMetric{color:#d4af37!important;text-align:center!important;}.ticker-wrap{width:100%;overflow:hidden;border-bottom:1px solid #d4af37;padding:10px 0;margin-bottom:20px;}.ticker-move{display:inline-block;white-space:nowrap;padding-left:100%;animation:marquee 30s linear infinite;color:#d4af37;font-weight:bold;}@keyframes marquee{0%{transform:translateX(0);}100%{transform:translateX(-100%);}}.ws-link{display:block;color:#d4af37!important;font-weight:bold;text-decoration:none;text-align:center;margin-bottom:15px;font-size:1.2rem;}div.stButton > button{background:none!important;border:none!important;color:#d4af37!important;font-weight:bold!important;font-size:1.5rem!important;text-transform:uppercase;cursor:pointer;}.mail-link{display:block;color:#ffffff!important;font-size:0.9rem;text-align:center;text-decoration:none;margin-top:10px;opacity:0.7;}</style>",unsafe_allow_html=True)
if not st.session_state.auth:
	st.title("🏛️ LEGACY QUANTUM VAULT")
	reg_sel=st.selectbox("🌐 SELECT REGION / ELIJA REGIÓN:",["USA / GLOBAL","ARGENTINA"])
	_,col_c,_=st.columns([1,1.5,1])
	with col_c:
		st.write("---")
		ws="https://wa.me"
		if reg_sel=="USA / GLOBAL":
			st.markdown(f'<a href="{ws}I%20want%20the%205%20min%20DEMO" class="ws-link">⚡ REQUEST DEMO (WSP)</a>',unsafe_allow_html=True)
			st.markdown(f'<a href="{ws}I%20want%20to%20pay%20via%20PayPal" class="ws-link">🔵 PAY WITH PAYPAL (WSP)</a>',unsafe_allow_html=True)
			st.markdown('<a href="mailto:dylanelpromaster25@://gmail.com" class="mail-link">✉️ SUPPORT: dylanelpromaster25@gmail.com</a>', unsafe_allow_html=True)
			st.write("---")
			emp=st.text_input("COMPANY:").strip().upper()
			pw=st.text_input("KEY:",type="password")
			btn_txt="🔓 UNLOCK"
		else:
			st.markdown(f'<a href="{ws}Quiero%20la%20DEMO%20de%205%20minutos" class="ws-link">⚡ SOLICITAR DEMO (WSP)</a>',unsafe_allow_html=True)
			st.markdown(f'<a href="{ws}Quiero%20pagar%20via%20Mercado%20Pago" class="ws-link" style="color:#009ee3!important;">💳 MERCADO PAGO (WSP)</a>',unsafe_allow_html=True)
			st.markdown(f'<a href="{ws}Quiero%20pagar%20via%20Cuenta%20DNI" class="ws-link" style="color:#004d40!important;">🏦 CUENTA DNI (WSP)</a>',unsafe_allow_html=True)
			st.markdown('<a href="mailto:dylanelpromaster25@://gmail.com" class="mail-link">✉️ SOPORTE: dylanelpromaster25@gmail.com</a>', unsafe_allow_html=True)
			st.write("---")
			emp=st.text_input("FIRMA / EMPRESA:").strip().upper()
			pw=st.text_input("CLAVE MAESTRA:",type="password")
			btn_txt="🔓 ACCEDER"
		if st.button(btn_txt):
			if pw=="LEGACY2026" and (emp in VIP or emp=="DYLAN777"):
				st.session_state.emp_final=emp
				if emp!="DYLAN777":st.session_state.reg.append(f"🟢 {emp}-{time.strftime('%H:%M')}")
				st.session_state.auth=True
				st.rerun()
			else:st.error("🚫 DENEGADO / DENIED")
	st.stop()
# INTERIOR (TRADUCCIÓN SEGÚN REGIÓN)
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | NODE: {st.session_state.emp_final} | AES-256 ACTIVE 🏛️</div></div>',unsafe_allow_html=True)
if st.session_state.emp_final=="DYLAN777":
	with st.expander("🕵️‍♂️ RADAR"):
		for r in st.session_state.reg:st.info(r)
c1,c2,c3=st.columns(3)
with c1: st.metric("REAL ESTATE / PROPIEDADES", "$85,000,000")
with c2: st.metric("YACHTS / YATES", "$12,500,000")
with c3: st.metric("PRIVATE JETS / JETS", "$24,000,000")
st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER / ESCÁNER")
act=st.text_area("LISTA DE ACTIVOS:",key="sc_final_boss")
if st.button("🧬 SCAN / ESCANEAR"):
	if act:
		with st.spinner("..."):time.sleep(1)
		st.success("VALUACIÓN DETECTADA: $42,500,000 USD")
if st.button("🔒 LOGOUT / SALIR"):
	st.session_state.auth=False; st.rerun()
