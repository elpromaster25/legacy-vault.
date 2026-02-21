import streamlit as st
import time

# --- 1. SEGURIDAD Y LISTA BLANCA ---
VIP = ["EMAAR", "GINEVRA", "REMAX", "THE AGENCY", "CARSO", "LEGACY", "DYLAN", "ADMIN", "SOTHEBYS"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'pago' not in st.session_state: st.session_state.pago = None
if 'reg' not in st.session_state: st.session_state.reg = []

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA (BOTONES RESTAURADOS) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        
        # BOTONES DE ACCESO Y DEMO
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("💎 BUY ACCESS ($12k)"): st.session_state.pago = "PAY"; st.rerun()
        with col_btn2:
            if st.button("📺 WATCH DEMO"): st.session_state.pago = "DEMO"; st.rerun()

        if st.session_state.pago == "PAY":
            st.success("Contacting OTC Desk... Use WhatsApp for instant VIP boarding.")
            st.markdown(f'<a href="https://wa.me" target="_blank" style="text-decoration:none;"><div style="background:#25d366; color:white; padding:10px; border-radius:10px; text-align:center; font-weight:bold;">🟢 WHATSAPP VIP</div></a>', unsafe_allow_html=True)
        
        st.write("---")
        emp = st.text_input("COMPANY:").strip().upper()
        pw = st.text_input("KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT"):
            if pw == "LEGACY2026" and emp in VIP:
                st.session_state.emp_final = emp
                st.session_state.auth = True; st.rerun()
            else: st.error("ACCESS DENIED")
    st.stop()

# --- 4. INTERIOR TOTAL (EL IMPERIO) ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")
st.metric("REAL ESTATE ASSETS", "$85,000,000")

# IA Y SCANNER (RESUMIDO PARA ESTABILIDAD)
st.subheader("🧬 QUANTUM ASSET SCANNER")
act = st.text_area("LISTA DE ACTIVOS:")
if st.button("🧬 SCAN"):
    with st.spinner("Escaneando..."):
        time.sleep(1)
        st.success("VALUACIÓN DETECTADA: $42,500,000 USD")

if st.sidebar.button("🔒 EXIT"):
    st.session_state.auth = False; st.rerun()
