import streamlit as st
import time

# --- 1. LÓGICA DE ESTADOS ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = "ARGENTINA"

# --- 2. DISEÑO IMPERIAL (DORADO Y NEGRO 100%) ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, h4, p, label { color: #d4af37 !important; text-align: center; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.1); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3em; }
    .stTextInput > div > div > input { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; }
    .stSelectbox > div > div > div { background-color: #1a1a1a !important; color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ACCESO (EL BÚNKER) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        st.session_state.reg = st.selectbox("📂 SELECT VAULT:", ["ARGENTINA", "USA"], key="v99")
        st.write("---")
        st.markdown("<div class='gold-card'>💎 ADQUIRIR TERMINAL CORPORATIVA</div>", unsafe_allow_html=True)
        # PAGOS RÁPIDOS
        c1, c2 = st.columns(2)
        with c1: st.markdown(f"<a href='mailto:dylanelpromaster25@gmail.com' style='text-decoration:none;'><div style='border:1px solid #d4af37; padding:10px; color:#d4af37; border-radius:5px;'>{'💳 MERCADO PAGO' if 'ARG' in st.session_state.reg else '🔵 PAYPAL'}</div></a>", unsafe_allow_html=True)
        with c2: st.markdown(f"<a href='mailto:dylanelpromaster25@gmail.com' style='text-decoration:none;'><div style='border:1px solid #d4af37; padding:10px; color:#d4af37; border-radius:5px;'>{'🏦 CUENTA DNI' if 'ARG' in st.session_state.reg else '🛡️ STRIPE'}</div></a>", unsafe_allow_html=True)
        
        st.write("---")
        emp = st.text_input("FIRMA / COMPANY:", key="e99")
        pw = st.text_input("MASTER KEY:", type="password", key="p99")
        if st.button("🔓 DESBLOQUEAR BÓVEDA"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp
                st.session_state.auth = True; st.rerun()
            else: st.error("Identificación requerida.")
    st.stop()

# --- 4. INTERIOR (IMPERIO RESTAURADO) ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final.upper()}")
st.write("---")

# ACTIVOS Y SCANNER
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$85M")
with c2: st.metric("YACHTS", "$12.5M")
with c3: st.metric("JETS", "$24M")

st.write("---")
st.subheader("🤖 ESTRATEGA IA & SCANNER")
lista = st.text_area("PEGUE SU LISTA DE ACTIVOS AQUÍ:", key="area99")
if st.button("🧬 ANALIZAR PATRIMONIO"):
    with st.spinner("Analizando..."):
        time.sleep(1)
        st.success(f"Análisis para {st.session_state.emp_final} completado.")

st.write("---")
# RELOJES
r1, r2, r3 = st.columns(3)
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:25 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:25 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:25 AM</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
