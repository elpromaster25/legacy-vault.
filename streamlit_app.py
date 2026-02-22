import streamlit as st
import time

# --- 1. WHITELIST DE LOS 34 GIGANTES ---
VIP = ["EMAAR", "DAMAC", "NEOM", "GINEVRA", "REMAX", "SOTHEBYS", "THE AGENCY", "HINES", "JLL", "CARSO", "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS", "LEGACY", "DYLAN", "ADMIN", "TZIPINE"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []
if 'founder' not in st.session_state: st.session_state.founder = False

# --- 2. DISEÑO IMPERIAL (TEXTO VISIBLE + SIN FLECHA) ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    /* 1. MATA LA FLECHA (>) PERO NO EL CONTENIDO */
    [data-testid="collapsedControl"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    
    .stApp { background-color: #000; border: 2px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 20px; }
    
    /* 2. FORZAR TEXTO EN LOS BOTONES (PARA QUE DIGA 'ACCEDER') */
    div.stButton > button { 
        background-color: #d4af37 !important; 
        color: #000000 !important; 
        font-weight: bold !important; 
        width: 100% !important; 
        height: 3.5em !important; 
        border-radius: 8px !important;
        display: block !important;
    }
    
    /* 3. BOTONES DE PAGO (PARA QUE DIGA 'PAYPAL' O 'MP') */
    .btn-pay { 
        background-color: #1a1a1a; 
        color: #ffffff !important; 
        padding: 14px; 
        border-radius: 10px; 
        font-weight: bold; 
        text-decoration: none; 
        display: block; 
        text-align: center; 
        margin-bottom: 10px; 
        border: 1px solid #d4af37; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 SELECT REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        if reg_sel == "USA / GLOBAL":
            st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com" class="btn-pay">🔵 PAYPAL ACCESS (EMAIL)</a>', unsafe_allow_html=True)
        else:
            st.markdown(f'<a href="mailto:dylanelpromaster25@gmail.com" class="btn-pay" style="background:#009ee3; border-color:#fff;">💳 MERCADO PAGO / DNI (EMAIL)</a>', unsafe_allow_html=True)
        st.write("---")
        emp_in = st.text_input("COMPANY / FIRMA:").strip().upper()
        pw_in = st.text_input("KEY / CLAVE:", type="password")
        if st.button("🔓 UNLOCK VAULT / ACCEDER"):
            if emp_in == "DYLAN777" and pw_in == "LEGACY2026":
                st.session_state.founder = True; st.session_state.emp_final = "FOUNDER CONTROL"; st.session_state.auth = True; st.rerun()
            elif pw_in == "LEGACY2026" and emp_in in VIP:
                st.session_state.emp_final = emp_in; st.session_state.reg.append(f"🟢 {emp_in} - {time.strftime('%H:%M')}"); st.session_state.auth = True; st.rerun()
            elif emp_in != "":
                st.error("🚫 DENEGADO. Contact support: dylanelpromaster25@gmail.com")
    st.stop()

# --- 4. INTERIOR TOTAL (EL IMPERIO) ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
if st.session_state.founder:
    with st.expander("🕵️‍♂️ RADAR (SOLO DYLAN)"):
        for r in st.session_state.reg: st.info(r)

st.metric("REAL ESTATE ASSETS", "$85,000,000")
st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER")
if st.button("🧬 INICIAR ESCANEO"):
    with st.spinner("..."): time.sleep(1); st.markdown(f"<div class='gold-card'><h2>VALUACIÓN: $42,500,000 USD</h2></div>", unsafe_allow_html=True)

if st.button("🔒 LOGOUT (CERRAR NODO)"):
    st.session_state.auth = False; st.session_state.founder = False; st.rerun()
